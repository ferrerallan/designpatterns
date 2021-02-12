from dominio.formapagamentoABS import FormaPagamento

class CartaoDebito(FormaPagamento):
  
  def usar(quantia):
    print(f"pagando com cartao de débito {quantia}")
    return quantia