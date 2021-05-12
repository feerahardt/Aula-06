def salarioAtualizado(valorhora, horaextra, salario):
    salario = valorhora * horaextra + salario
    print(f'Seu salário é {salario}')


salarioAtualizado(15.50, 10, 1500.00)
