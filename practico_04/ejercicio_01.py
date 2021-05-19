"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    con = sqlite3.connect("bd1.db")
    cursorObj = con.cursor()
    
    cursorObj.execute("""CREATE TABLE Persona (
	                    IdPersona INTEGER PRIMARY KEY autoincrement
	                    ,descripcion TEXT
	                    ,precio REAL
	                    )""")
    con.commit()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    con = sqlite3.connect("bd1.db")
    cursorObj = con.cursor()
    cursorObj.execute('drop table if exists Persona')
    con.commit()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
