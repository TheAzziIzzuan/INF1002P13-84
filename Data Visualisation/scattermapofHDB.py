import pandas as pd
sgdata = pd.read_csv("datasets/hdb-property-coords(FULL).csv")

import plotly.express as px

fig = px.scatter_mapbox(sgdata, lat="Latitude", lon="Longitude", hover_name="Address", hover_data=["blk_no","street"],
                        color_discrete_sequence=["rebeccapurple"],opacity=0.5)
fig.update_layout(mapbox_style="open-street-map")
fig.update_geos(resolution=50, fitbounds="locations")
fig.show()
# fig.write_html("scatter_map.html") 