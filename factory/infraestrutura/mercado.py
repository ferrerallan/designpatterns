from dominio.dividaABS import Divida
from dominio.formapagamentoABS import FormaPagamento

class Mercado(Divida):
  valor = 100

  def pagar(self, FormaPagamento):
    valorRestante = self.valor - FormaPagamento.usar(self.valor)
    print(f"valor restante {valorRestante}")