from dominio.formapagamentoABS import FormaPagamento

class Calote(FormaPagamento):
  
  def usar(quantia):
    print("levou calote")
    return 0