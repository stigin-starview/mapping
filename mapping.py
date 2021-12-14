import folium
import pandas

map = folium.Map(location = [20.5937, 78.9629], zoom_start = 5, tiles = "Stamen Terrain")

VolcanoData = pandas.read_json("resources/VolcanoList.json")
# VolcanoName = dict(VolcanoData("name":"name", "type":"type"))
VolcanoLat = list(VolcanoData["lat"])
VolcanoLon = list(VolcanoData["lon"])

fg = folium.FeatureGroup(name = "Indian Map")

for lat, lon in zip(VolcanoLat, VolcanoLon):
    fg.add_child(folium.Marker(location = [lat, lon], popup = "This is an example of a marker", icon = folium.Icon(color = 'red')))


map.add_child(fg)

map.save("IndianMap.html")
    