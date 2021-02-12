from infraestrutura.mercado import Mercado 

class DividaFactory(object):
  def criarDivida(tipo):
    return eval(tipo.capitalize())()
