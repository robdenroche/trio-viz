from cli import parse_args
from plotting import plot_trio
import gzip


def main():
    # do cli
    args = parse_args()

    vcf_file = args.vcf
    mom = args.mom
    dad = args.dad
    child = args.child
    karyotype_file = args.karyotype
    output_file = args.output

    # the number of inheritance state changes to smooth over
    collapse_tolerance = 0

    mom_dad_match = 0
    mom_child_match = 0
    dad_child_match = 0

    # region elements are dicts of (start, end and inheritance state)
    regions = []

    # read trio vcf
    open_func = gzip.open if vcf_file.endswith(".gz") else open
    with open_func(vcf_file, "rt") as fh:

        current_pos = 0
        current_start = 0
        current_end = None
        current_state = None

        for line in fh:
            line = line.rstrip()

            if line.startswith("##"):
                # header
                continue
            elif line.startswith("#"):
                # column names
                columns = line.split("\t")

                # establish sample genotype columns
                mom_col = columns.index(mom)
                dad_col = columns.index(dad)
                child_col = columns.index(child)
            else:
                # data lines
                fields = line.split("\t")
                # chrom = fields[0]
                # assume one chromosome
                pos = fields[1]

                mom_genotype = fields[mom_col]
                dad_genotype = fields[dad_col]
                child_genotype = fields[child_col]

                # collect and collapse states
                if mom_genotype == dad_genotype:
                    mom_dad_match += 1
                    state = "boring"
                elif mom_genotype == child_genotype:
                    state = "mom"
                elif dad_genotype == child_genotype:
                    state = "dad"
                else:
                    state = "hybrid"

                # if the state is the same as the current state, update the end
                # position
                if state == current_state:
                    current_end = pos
                else:  # store the previous region
                    if current_state is not None:
                        regions.append(
                            {
                                "start": current_start,
                                "end": current_end,
                                "state": current_state,
                            }
                        )

                    current_state = state
                    current_start = pos
                    current_end = pos

    # read karyotype?

    # collapse regions

    # plot
    plot_trio(
        regions,
        #    karyotype_file=karyotype_file,
        output_file=output_file,
        #    collapse_tolerance=collapse_tolerance,
    )


if __name__ == "__main__":
    main()
