import sys
import os

path = os.path.abspath("clases/")
sys.path.append(path)

import pytest

from Modelo import ControlDeFertilizantes as cf

def test_datos_vacios_Fertilizantes():
   with pytest.raises(TypeError, match='Debes ingresar todos los campos'):
      datos_cliente = cf.ControlDeFertelizantes(idProducto="", nombreProducto="",precio="",ica="",frecuenciaAplicacion="",ultimaAplicaion="")

def test_idProductoFertilizantes():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cf.ControlDeFertelizantes(idProducto="123a", nombreProducto="sapa",precio="123",ica="10",frecuenciaAplicacion="10",ultimaAplicaion="10")

def test_precio_productoFertilizantes():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cf.ControlDeFertelizantes(idProducto="123", nombreProducto="sapa",precio="123a",ica="10",frecuenciaAplicacion="10",ultimaAplicaion="10")

def test_ica_productoFertilizantes():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cf.ControlDeFertelizantes(idProducto="123", nombreProducto="sapa",precio="123",ica="10a",frecuenciaAplicacion="10",ultimaAplicaion="10")
