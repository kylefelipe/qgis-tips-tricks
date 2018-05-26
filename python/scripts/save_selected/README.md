# QGIS tips & tricks - PYTHON - save_selected
_QGIS VERSION:_ 2.18 (Not tested with new version)

This script makes a selection by using an qgis expression in all vectors layers within the QGIS project and then saves the selection to a shp file with the same name, plus "\_Dado_Filtrado", within the same layer folder.  
The new files will be added to the project within a group called "DADOS_FILTRADOS".  
__NOTE:__ All layers must have the same column used in the expression

USAGE:
exp > Qgis expression, you can make one using qgis field calculator and place it inside tree quotes (""" """)  
	Ex: """ "field_3" = 12.2253 or $id = 3 """  
