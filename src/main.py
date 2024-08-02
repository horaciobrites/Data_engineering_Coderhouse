from decouple import config
from modulos.conexion_api import *
from modulos.grabar_datos import *


def main():
    try:
        data=extraccion_API(url=url_API)
        grabar_datos(host=config('host'),
                    port=config('port'),
                    dbname=config('dbname'),
                    user=config('user'),
                    password=config('password'),
                    schema=config('schema'),
                    tabla=config('tabla'),
                    data=data)
    except Exception as e :
        print(f'Error {e}')




if __name__=='__main__':
    main()