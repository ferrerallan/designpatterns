from infraestrutura.mercado import Mercado
from infraestrutura.cartaocredito import CartaoCredito

from factories.dividafactory import DividaFactory
from factories.formapagamentofactory import FormaPagamentoFactory


def main():
  '''Desta primeira forma, nosso codigo fica endurecido e nao escalavel,
  com acoplamento forte e o recurso chamador, (neste caso um main,
  mas poderia ser uma outra classe ou serviço)
  precisa sempre ser reescrito quando houver mudanças
  '''
  print("*** pagamento com acoplamento forte ***")
  mercado = Mercado()
  mercado.pagar(CartaoCredito)


  print("*** pagamento escalável, com factorys ***")
  divida = DividaFactory.criarDivida("mercado")
  formaPagamento = FormaPagamentoFactory.criar("rico")
  divida.pagar(formaPagamento)

  '''
  esses parametros poderiam vir de interação com usuario ou arquivos de configuração,
  desta maneira, o main nunca precisaria ser recompilado
  e implementamos o principio OPEN/CLOSED do SOLID
  '''
  divida = DividaFactory.criarDivida("mercado")
  formaPagamento = FormaPagamentoFactory.criar("ladrao")
  divida.pagar(formaPagamento)

if __name__ == '__main__':
  main()