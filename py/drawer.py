import folium
import os
# make feature group, to handle multiple layers in a folium BAM map
# even if we use only one layer here
print(os.getcwd())
feature_group = folium.FeatureGroup("my map")
feature_group.add_child(
	folium.GeoJson(
		data=(
			open('./data/india_states.json','r',encoding='utf-8-sig').read()
		)
	)
)

feature_group.add_child(
	folium.Marker(
		location=[27,78,],
		popup="<h1>Title</h1><p>This is a popup that appears when you click</p>",
		tooltip="Click for more.."
	)
)

map=folium.Map(
	location=[21,79],
	zoom_start=5,
)

map.add_child(feature_group)

map.save("./templates/test.html")