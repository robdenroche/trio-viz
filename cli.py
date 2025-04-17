import argparse

# from . import __version__


def parse_args():
    """Define and parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Trio Viz CLI Tool")
    parser.add_argument(
        "-v", "--vcf", type=str, required=True, help="Path to the input vcf file"
    )

    parser.add_argument(
        "-m", "--mom", type=str, required=True, help="Mother's sample name"
    )

    parser.add_argument(
        "-d", "--dad", type=str, required=True, help="Father's sample name"
    )

    parser.add_argument(
        "-c", "--child", type=str, required=True, help="Child's sample name"
    )

    parser.add_argument(
        "-k", "--karyotype", type=str, help="Path to the karyotype file"
    )

    parser.add_argument("-o", "--output", type=str, help="Path to the output file")

    return parser.parse_args()
