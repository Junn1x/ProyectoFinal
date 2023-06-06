import sys
import os

path = os.path.abspath("clases/")
sys.path.append(path)

import pytest

from Modelo import ProductosDeControl as cp


def test_datos_vacios_Pc():
   with pytest.raises(TypeError, match='Debes ingresar todos los campos'):
      datos_cliente = cp.ProductosControl(idProducto="", nombreProducto="",precio="",ica="",frecuenciaAplicacion="")

def test_idProductoPc():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.ProductosControl(idProducto="123a", nombreProducto="sapa",precio="123",ica="10",frecuenciaAplicacion="10")

def test_precio_productoPc():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.ProductosControl(idProducto="123", nombreProducto="sapa",precio="123a",ica="10",frecuenciaAplicacion="10")

def test_ica_productoPc():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.ProductosControl(idProducto="123", nombreProducto="sapa",precio="123",ica="10a",frecuenciaAplicacion="10")

def test_frecuencia_productoPc():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.ProductosControl(idProducto="123", nombreProducto="sapa",precio="123",ica="10",frecuenciaAplicacion="10a")
