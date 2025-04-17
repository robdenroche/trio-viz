from cli import parse_args
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

    mom_dad_match = 0
    mom_child_match = 0
    dad_child_match = 0

    # read trio vcf
    open_func = gzip.open if vcf_file.endswith(".gz") else open
    with open_func(vcf_file, "rt") as fh:
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
                chrom = fields[0]
                pos = fields[1]
                ref = fields[3]
                alt = fields[4]
                mom_genotype = fields[mom_col]
                dad_genotype = fields[dad_col]
                child_genotype = fields[child_col]

                # do something with the data
                if mom_genotype == dad_genotype:
                    mom_dad_match += 1
                if mom_genotype == child_genotype:
                    mom_child_match += 1
                if dad_genotype == child_genotype:
                    dad_child_match += 1

    # read karyotype?

    # collapse regions

    # plot
    print(f"Mom and Dad match: {mom_dad_match}")
    print(f"Mom and Child match: {mom_child_match}")
    print(f"Dad and Child match: {dad_child_match}")


if __name__ == "__main__":
    main()
