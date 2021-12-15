import folium
import pandas

map = folium.Map(location = [20.5937, 78.9629], zoom_start = 5, tiles = "Stamen Terrain")

VolcanoData = pandas.read_json("resources/VolcanoList.json")
VolcanoName = list(VolcanoData["name"])
VolcanoType = list(VolcanoData["type"])
VolcanoElev = list(VolcanoData["elevation"])
VolcanoLat = list(VolcanoData["lat"])
VolcanoLon = list(VolcanoData["lon"])

html = """<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank"> <h3> %s:</h3> </a>
Type: %s <br>
Height: %s m
"""

fg = folium.FeatureGroup(name = "Indian Map")

for name, type, elev, lat, lon in zip(VolcanoName, VolcanoType, VolcanoElev, VolcanoLat, VolcanoLon):
    iframe = folium.IFrame(html = html % (name + " volcano", name, type , elev), width = 200, height = 100)
    # fg.add_child(folium.Marker(location = [lat, lon], popup = f"Name: {name}, Type: {type} , Elevation: {elev}m", icon = folium.Icon(color = 'green')))
    fg.add_child(folium.Marker(location = [lat, lon], popup = folium.Popup(iframe), icon = folium.Icon(color = 'green')))


map.add_child(fg)

map.save("IndianMap.html")
    