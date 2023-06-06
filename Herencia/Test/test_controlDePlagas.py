import sys
import os

path = os.path.abspath("clases/")
sys.path.append(path)

import pytest

from Modelo import ControlDePlagas as cp


def test_datos_vacios_Plagas():
   with pytest.raises(TypeError, match='Debes ingresar todos los campos'):
      datos_cliente = cp.ControlDePlagas(idProducto="", nombreProducto="",precio="",ica="",frecuenciaAplicacion="",periodoCarencia="")

def test_idProductoPlagas():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.ControlDePlagas(idProducto="123a", nombreProducto="sapa",precio="123",ica="10",frecuenciaAplicacion="10",periodoCarencia="10")

def test_precio_productoPlagas():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.ControlDePlagas(idProducto="123", nombreProducto="sapa",precio="123a",ica="10",frecuenciaAplicacion="10",periodoCarencia="10")

def test_ica_productoPlagas():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.ControlDePlagas(idProducto="123", nombreProducto="sapa",precio="123",ica="10a",frecuenciaAplicacion="10",periodoCarencia="10")

def test_frecuencia_productoPlagas():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.ControlDePlagas(idProducto="123", nombreProducto="sapa",precio="123",ica="10",frecuenciaAplicacion="10a",periodoCarencia="10")

def test_periodo_productoPlagas():
   with pytest.raises(ValueError, match='El dato debe contener solo numeros'):
      datos_cliente = cp.ControlDePlagas(idProducto="123", nombreProducto="sapa",precio="123",ica="10",frecuenciaAplicacion="10",periodoCarencia="10a")
