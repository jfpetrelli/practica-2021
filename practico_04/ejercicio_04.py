"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3
from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""

    con = sqlite3.connect("bd1.db")
    cursorObj = con.cursor()
    row = cursorObj.execute("SELECT IDPersona, Nombre, FechaNacimiento, DNI, Altura FROM Persona WHERE IdPersona = ?",(id_persona,))    
    if row.fetchone() == None:
        return False
    fila = list(row.fetchone())
    date_fn = datetime.datetime.strptime(fila[2], "%d %B, %Y")
    fila[2] = date_fn
    return tuple(fila)


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
