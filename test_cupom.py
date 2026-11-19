from cupom import desconto_valido

def test_t1_aceita_percentual_exatamente_limite():
    percentual = 21
    resultado = desconto_valido(percentual)
    assert resultado is True

def test_t2_rejeita_percentual_limite_mais_um():
    percentual = 22
    resultado = desconto_valido(percentual)
    assert resultado is False

def test_t3_rejeita_percentual_zero():
    percentual = 0
    resultado = desconto_valido(percentual)
    assert resultado is False
