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

def VolcanoColors(type):
    if type == "Stratovolcano":
        return "red"
    elif type == "Submarine":
        return "lightblue"
    else:
        return "green"

fg = folium.FeatureGroup(name = "Indian Map")

for name, type, elev, lat, lon in zip(VolcanoName, VolcanoType, VolcanoElev, VolcanoLat, VolcanoLon):
    iframe = folium.IFrame(html = html % (name + " volcano", name, type , elev), width = 200, height = 100)
    # fg.add_child(folium.Marker(location = [lat, lon], popup = f"Name: {name}, Type: {type} , Elevation: {elev}m", icon = folium.Icon(color = 'green')))
    fg.add_child(folium.Marker(location = [lat, lon], popup = folium.Popup(iframe), icon = folium.Icon(color = VolcanoColors(type))))

    #  To add the popup as circle use the code below
    # fg.add_child(folium.CircleMarker(location = [lat, lon], radius= 10, popup = folium.Popup(iframe), color = VolcanoColors(type), fill = True, fill_color = VolcanoColors(type)))


map.add_child(fg)

map.save("IndianMap.html")
    


"""" Below is a function that i used to find out how many different 
    types of volcanoes are listed in the json file 

def testing():
    result = []                          
    for ty in VolcanoType:
            if any(ty in s for s in result):
                continue
            else:
                result.append(ty)
    
    print(result)


testing()

"""
