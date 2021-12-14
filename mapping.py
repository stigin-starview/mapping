import folium
import pandas

map = folium.Map(location = [20.5937, 78.9629], zoom_start = 5, tiles = "Stamen Terrain")

VolcanoData = pandas.read_json("resources/VolcanoList.json")
VolcanoName = list(VolcanoData["name"])
VolcanoType = list(VolcanoData["type"])
VolcanoLat = list(VolcanoData["lat"])
VolcanoLon = list(VolcanoData["lon"])

fg = folium.FeatureGroup(name = "Indian Map")

for name, type, lat, lon in zip(VolcanoName, VolcanoType, VolcanoLat, VolcanoLon):
    fg.add_child(folium.Marker(location = [lat, lon], popup = f"name: {name}, type: {type}", icon = folium.Icon(color = 'green')))


map.add_child(fg)

map.save("IndianMap.html")
    