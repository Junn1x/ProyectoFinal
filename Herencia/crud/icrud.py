from abc import ABC , abstractmethod

class ICrud ( ABC ) :
    
    @abstractmethod
    def crear ( self , ** kwargs ) :
      raise NotImplementedError
    
    @abstractmethod
    def mostrar ( self , ** kwargs ) :
      raise NotImplementedError
    
    @abstractmethod
    def relacion ( self , ** kwargs ) :
      raise NotImplementedError