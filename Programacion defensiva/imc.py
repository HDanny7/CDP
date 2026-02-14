def calcular_imc(peso, altura):
    assert peso > 0, 'El peso debe ser mayor a cero'
    assert altura >0, 'La altura debe ser mayor que cero'

    imc= peso / (altura ** 2)
    return imc



