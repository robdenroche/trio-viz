import plotly.graph_objects as go

# plotting constants
MIN_SIZE = 10000

TOP = 1
BOTTOM = -1

STATE_COLOURS = {
    "boring": "grey",
    "mom": "red",
    "dad": "green",
    "hybrid": "blue",
}


def plot_trio(regions, output_file):
    # create empty plotly figure object
    fig = go.Figure()

    # add traces for each region
    for region in regions:
        start = int(region["start"])
        end = int(region["end"])
        state = region["state"]

        # skip regions that are too small
        if end - start < MIN_SIZE:
            continue

        # add a scatter trace for the region
        fig.add_trace(
            go.Scatter(
                x=[start, start, end, end, start],
                y=[BOTTOM, TOP, TOP, BOTTOM, BOTTOM],
                mode="lines",
                fill="toself",
                fillcolor=STATE_COLOURS[state],
                line=dict(width=0),
                name=state,
            )
        )

    fig.show()

    # write the plot
    fig.write_html(output_file)
