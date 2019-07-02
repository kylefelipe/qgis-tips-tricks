""" Export all vectors layers attributes to a txt.
Qgis Version: 2.18
"""
import json
campos = {}
file = "C:\Temp\campos.txt" # file path
for lyr in QgsMapLayerRegistry.instance().mapLayers().values():
    if type(lyr) == QgsVectorLayer:
        fs = []
        for f in lyr.pendingFields():
            fs.append((f.name().encode('utf-8'), f.typeName().encode('utf-8')))
        campos[lyr.name().encode('utf-8')] = fs

base = json.dumps(campos, indent=4, sort_keys=False, ensure_ascii=False, encoding="utf-8")
#print base
with open(file, 'w') as f:
    f.write(base)
print "Arquivo Salvo!"    
