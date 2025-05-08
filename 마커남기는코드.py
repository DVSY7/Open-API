import folium

map = folium.Map(location=[37,127],zoom_start=7)

marker = folium.Marker([35.183778757, 126.880647243],
                       popup='한국폴리텍대학교 광주캠퍼스',
                       icon = folium.Icon(color='blue'))

marker.add_to(map)

map.save(r'uni_map2.html')
