from cli import parse_args
from file_io import read_vcf, read_karyotype
from plotting import plot_trio, plot_karyotype

import plotly.graph_objects as go


def main():
    # do cli
    args = parse_args()

    vcf_file = args.vcf
    gt_names = {
        "mom": args.mom,
        "dad": args.dad,
        "child": args.child,
    }

    karyotype_file = args.karyotype
    output_file = args.output

    # the number of inheritance state changes to smooth over
    collapse_tolerance = 0

    mom_dad_match = 0
    mom_child_match = 0
    dad_child_match = 0

    # read vcf
    chrom, regions = read_vcf(vcf_file, gt_names)

    # read karyotype?
    karyotype = read_karyotype(karyotype_file, chrom)

    # collapse regions

    # create empty plotly figure object
    fig = go.Figure()

    # add trio plot
    fig = plot_trio(
        fig,
        regions,
        #    collapse_tolerance=collapse_tolerance,
    )

    # add karyotype plot
    fig = plot_karyotype(fig, karyotype)

    # save figure
    fig.write_html(output_file)
    fig.show()

if __name__ == "__main__":
    main()
