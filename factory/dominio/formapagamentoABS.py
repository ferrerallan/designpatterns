from abc import ABCMeta, abstractmethod

class FormaPagamento(metaclass=ABCMeta):
  saldo=0

  @abstractmethod
  def usar(self):
    pass
