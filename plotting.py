import plotly.graph_objects as go

# plotting constants
MIN_SIZE = 10000

TRIO_TOP = 8
TRIO_BOT = 1.5

KARYO_TOP = 1
KARYO_BOT = 0

STATE_COLOURS = {
    "boring": "grey",
    "mom": "red",
    "dad": "green",
    "hybrid": "blue",
}

BAND_COLOURS = {
    "gneg": "#DDDDDD",
    "gpos25": "#AAAAAA",
    "gpos50": "#777777",
    "gpos75": "#444444",
    "gpos100": "#111111",
    "acen": "darkred",
    "gvar": "#DDDDDD",
    "stalk": "#DDDDDD",
}


def plot_trio(fig, regions):

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
                y=[TRIO_BOT, TRIO_TOP, TRIO_TOP, TRIO_BOT, TRIO_BOT],
                mode="lines",
                fill="toself",
                fillcolor=STATE_COLOURS[state],
                line=dict(width=0),
                name=state,
            )
        )

    return fig


def plot_karyotype(fig, karyotype):

    # centromere count
    acen_count = 0

    # add traces for each region
    for region in karyotype:
        start = int(region["start"])
        end = int(region["end"])
        stain = region["stain"]
        name = region["name"]

        if stain == "acen":
            # plot as two triangles
            if acen_count % 2 == 0:
                # first triangle
                fig.add_trace(
                    go.Scatter(
                        x=[start, start, end],
                        y=[KARYO_BOT, KARYO_TOP, (KARYO_TOP + KARYO_BOT) / 2],
                        mode="lines",
                        fill="toself",
                        fillcolor=BAND_COLOURS[stain],
                        line=dict(width=0),
                        name=name,
                    )
                )
            else:
                # second triangle
                fig.add_trace(
                    go.Scatter(
                        x=[start, end, end],
                        y=[(KARYO_TOP + KARYO_BOT) / 2, KARYO_TOP, KARYO_BOT],
                        mode="lines",
                        fill="toself",
                        fillcolor=BAND_COLOURS[stain],
                        line=dict(width=0),
                        name=name,
                    )
                )
            acen_count += 1
        
        else:
            # add a scatter trace for the region
            fig.add_trace(
                go.Scatter(
                    x=[start, start, end, end, start],
                    y=[KARYO_BOT, KARYO_TOP, KARYO_TOP, KARYO_BOT, KARYO_BOT],
                    mode="lines",
                    fill="toself",
                    fillcolor=BAND_COLOURS[stain],
                    line=dict(width=0),
                    name=name,
                )
            )

    return fig
