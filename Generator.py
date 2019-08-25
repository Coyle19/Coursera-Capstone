import folium
import urllib, json
import pandas as pd

url = "https://raw.githubusercontent.com/jordanstreiff/atlanta-city-council-search/master/public/NPU.geojson"
response = urllib.request.urlopen(url)
districtNPU_data = json.loads(response.read())

csvUrl = "https://raw.githubusercontent.com/Coyle19/Coursera-Capstone/master/df_atl.csv"
csvResponse = urllib.request.urlopen(csvUrl)
districtNpuCsv =  pd.read_csv(csvResponse)

atlanta_location = [33.7490, -84.3880]
world_map = folium.Map(location=atlanta_location, zoom_start=11, tiles='Stamen Terrain')
#generate a choropleth map using the population density information
world_map.choropleth(
    geo_data = districtNPU_data,
    data = districtNpuCsv,
    columns = ['NPU', 'AVG SQ MILE'],
    key_on = 'feature.properties.NPU',
    fill_color = 'YlGn',
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name='Some Legend'
)

folium.LayerControl().add_to(world_map)

#display the map
world_map