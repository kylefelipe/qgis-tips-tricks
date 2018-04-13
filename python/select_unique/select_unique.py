# Python Version 2.7
# Author: Kyle Felipe
# e-mail: kylefelipe@gmail.com
# Date: 2018/05/12

col_name = "COMARCA"
layer = iface.activeLayer()
iter = layer.getFeatures()
at_data = {}
unique_id = []
for feature in iter:
    at_data[feature.id()]=feature[col_name]
for i in at_data.keys():
    if at_data.values().count(at_data[i]) ==1:
        uniqueid.append(i)

layer.setSelectedFeatures(uniqueid)
