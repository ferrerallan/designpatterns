from infraestrutura.cartaocredito import CartaoCredito 
from infraestrutura.cartaodebito import CartaoDebito 
from infraestrutura.calote import Calote 


class FormaPagamentoFactory(object):
  def criar(condicao):
    if condicao == "pobre": 
      return CartaoCredito
    elif condicao == "rico":
      return CartaoDebito
    elif condicao == "ladrao":
      return Calote
    else:
      return CartaoCredito