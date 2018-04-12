col_name = "comarca"
uniqueid = []
attribute_data = []
layer = iface.activeLayer()
iter = layer.getFeatures()
for feature in iter:
    attrs = feature.attributes()
    attribute_data.append(feature[col_name])
    if attribute_data.count(feature[col_name]) == 1:
        uniqueid.append(feature.id())
    
layer.select(uniqueid)
    