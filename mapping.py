import folium
map = folium.Map(location = [20.5937, 78.9629], zoom_start = 5, tiles = "Stamen Terrain")
map.save("IndianMap.html")
