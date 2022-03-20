from abc import ABCMeta, abstractmethod
from .formapagamentoABS import FormaPagamento

class Divida(metaclass=ABCMeta):
  valor=0

  @abstractmethod
  def pagar(self, FormaPagamento):
    pass