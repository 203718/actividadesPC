import requests
import time

#investigar sobre la libreria threading 

import psycopg2

# Investigar sobre la libreria threading 

try:
    conexion = psycopg2.connect(database='pokebase', user='postgres', password='gerson')
    cursor1=conexion.cursor()
    cursor1.execute('select version()')
    version=cursor1.fetchone()
except Exception as err:
        print('Error al conecta a la base de datos')

def closeConexion():
    conexion.close()
    pass

def get_service():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-03-05&limit=5000"
    r = requests.get(url)
    data = r.json()
    lugares = data['features']
    for lugar in lugares:
        write_db(lugar['properties']['place'])
    pass


def write_db(x):
    try:
        cursor1.execute("insert into pokemons (name) values ('"+x+"')")
    except Exception as err:
        print('Error en la inserción: '+ err)
    else:
        conexion.commit()
    pass

if __name__ == "__main__":
    init_time = time.time()
    get_service()
    end_time = time.time() - init_time
    print(end_time)
    closeConexion()