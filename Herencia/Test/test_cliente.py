import sys
import os

path = os.path.abspath("clases/")
sys.path.append(path)

import pytest

from Modelo import claseClientes

def test_datos_vacios():
   with pytest.raises(TypeError, match='Debes ingresar todos los campos'):
      datos_cliente = claseClientes.Cliente(cedula="",nombre="",facturas=None)


def test_nombre():
   with pytest.raises(ValueError, match="El nombre debe tener solo letras"):
      datos = claseClientes.Cliente(cedula="12312",nombre="sam1r",facturas=[])

def test_cedula():
   with pytest.raises(ValueError, match="La cedula solo debe contener numeros"):
      datos = claseClientes.Cliente(cedula="12312sq",nombre="samir",facturas=[])

