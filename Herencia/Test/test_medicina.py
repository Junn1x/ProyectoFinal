import sys
import os

path = os.path.abspath("clases/")
sys.path.append(path)

import pytest

from Modelo import medicina as cp

def test_datos_vacios_med():
   with pytest.raises(TypeError, match='Debes ingresar todos los campos'):
      datos_cliente = cp.Medicina(idProducto="", nombreProducto="",precio="",dosis="",tipoAnimal="")

def test_idProductoMd():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.Medicina(idProducto="123a", nombreProducto="sapa",precio="123",dosis="10",tipoAnimal="animal")

def test_precio_productoMd():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.Medicina(idProducto="123", nombreProducto="sapa",precio="123a",dosis="10",tipoAnimal="animal")

def test_nomProductoMd():
   with pytest.raises(ValueError, match='El nombre del producto debe tener solo letras'):
      datos_cliente = cp.Medicina(idProducto="123", nombreProducto="sapa1",precio="123",dosis="10",tipoAnimal="animal")

def test_dosis_productoMd():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.Medicina(idProducto="123", nombreProducto="sapa",precio="123",dosis="10a",tipoAnimal="animal")

def test_tipoAnimal_productoMd():
   with pytest.raises(ValueError, match='El tipo de animal solo debe tener letras'):
      datos_cliente = cp.Medicina(idProducto="123", nombreProducto="sapa",precio="123",dosis="10",tipoAnimal="animal123")
