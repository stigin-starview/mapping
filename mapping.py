import folium

map = folium.Map(location = [20.5937, 78.9629], zoom_start = 5, tiles = "Stamen Terrain")

""" below is the standard way of doing this:

map.save("IndianMap.html")  """

# below is the clean way of doing.

#add for loop for automate the list

fg = folium.FeatureGroup(name = "Indian Map")
fg.add_child(folium.Marker(location = [20.5937, 78.9629], popup = "This is an example of a marker", icon = folium.Icon(color = 'green')))
map.add_child(fg)

map.save("IndianMap.html")
    