from dominio.formapagamentoABS import FormaPagamento

class CartaoCredito(FormaPagamento):
  
  def usar(quantia):
    valorAPagar = quantia/10
    print(f"pagando com cartao de credito {valorAPagar}")

    return (valorAPagar)
    