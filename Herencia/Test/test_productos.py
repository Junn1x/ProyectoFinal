import sys
import os

path = os.path.abspath("clases/")
sys.path.append(path)

import pytest

import claseProductos as cp

def test_datos_vacios():
   with pytest.raises(TypeError, match='Debes ingresar todos los campos'):
      datos_cliente = cp.Producto(idProducto="", nombreProducto="",precio="")

