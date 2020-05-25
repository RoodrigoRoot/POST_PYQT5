import psycopg2
import logging
import funcArchivo
import funcjson
import funcGrales
import Globales

logging.basicConfig(
    level=logging.DEBUG
)
def fnConexionDB(object):
    try:

        if funcArchivo.fnArchivoExiste(Globales.gsInit):
            data = funcjson.fnObtenerDato(Globales.gsInit)
            servidor = data["server"]
            usuario = data["user"]
            password = data["paswd"]
            database = data["db"]
            Globales.gsConnPost = psycopg2.connect(host=servidor,
                                           user="rod",
                                           password="forever11",
                                           database=database)
            
            
            if Globales.gsConnPost is not None:
                funcGrales.fnMensaje("Exito", "Conexión Exitosa")
        else:
            print("Error", "no existe el archivo")
            funcGrales.fnMensaje("Error", "no existe el archivo")           
    except Exception as e:        
        logging.debug("fnConexionDb", e)
        return False

def fnCerrarConexion():
    Globales.gsConnPost.close()

def fnExecutesql(sQuery):
    Globales.gCursor = Globales.gsConnPost.cursor()
    try:
        Globales.gCursor.execute(sQuery)
        return True
    except Exception as e:
        logging.debug("Error al ejecutar", sQuery, e)
        return False

if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    fnConexionDB()
    fnExecutesql("select * from usuarios")
    print(Globales.gCursor.rowcount)
    while True:
        registro = Globales.gCursor.fetchone()
        if registro is None:
            break
        print(registro)
    fnCerrarConexion()