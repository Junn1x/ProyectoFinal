import sys
import os

path = os.path.abspath("clases/")
sys.path.append(path)

import pytest

from Modelo import claseFacturas

def test_datos_vacios():
   with pytest.raises(TypeError, match='Debes ingresar todos los campos'):
      datos_cliente = claseFacturas.Factura(productos=None, fechaCompra="",costo="")
      return datos_cliente

def test_costo():
   with pytest.raises(ValueError, match="El costo solo debe contener numeros"):
      datos = claseFacturas.Factura(productos=[],fechaCompra="1/06/01",costo="1123sa")
      return datos

def test_productos():
   with pytest.raises(TypeError, match="La factura debe tener productos"):
      datos = claseFacturas.Factura(productos=None,fechaCompra="1/06/01",costo="1123")
      return datos
