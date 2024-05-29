import os

location = '/Users/steve/Desktop/proyecto_parcial/python/dataset'

#####VALIDAR SI LA CARPETA EXISTE###

if not os.path.exists(location):
    #####SI LA CARPETA NO EXISTE, LA CREO
    os.mkdir(location)
else: ##CARPETA EXISTE
    ##BORRAR CONTENIDO
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
            
from kaggle.api.kaggle_api_extended import KaggleApi

## AUTENTICARNOS ##

api = KaggleApi()
api.authenticate()

##DESCARGAR DATASET
#print(api.dataset_list(search=''))# listo los datasets disponibles

#api.dataset_download_file('chopper53/data-engineer-salary-in-2024','salaries_(2).csv',path=location, force=True, quiet=False)#
api.dataset_download_files('chopper53/data-engineer-salary-in-2024', path=location, force=True, quiet=False, unzip=True)