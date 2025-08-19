######################################### Calculo Salarial PYTHON  ############################################
# Programa que calcule e imprima o salario a ser transferido para um funcionario
# Receba o valor bruto do salario e o adicional dos beneficios
# O Salaro a ser transferido deve ser calculado da seguinte maneira:
#           (valor bruto do salario - percentual de imposto mediante ao salario ) + adicional dos beneficios
#
# O percentual de imposto segue as aliquotas:
#
#    5.00% --- entre 0 e 1100.00
#   10.00% --- 1100.01 a 2500.00
#   15.00% --- Maior que 2500.00
#
### ENTRADA:
# Consiste em vários arquivos de teste, que conterá o VALOR BRUTO DO SALARIO e ADICIONAL DOS BENEFICIOS.
#
## SAIDA
# Para cada arquivo de entrada, terá um arquivo de saida.
# Será gerado uma linha com um numero que será a diferença entre o valor bruto do salario e o percentual de 
# imposto mediante a faixa salarial somado com o adicional dos beneficios.
#
#############################################################################################################

## Em PYTHON#

def calcula_imposto(salario):
    aliquota = 0.00
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05
    elif(salario >1100 and salario <=2500):
        aliquota = 0.1
    else:
        aliquota = 0.15
    print(f'Alíquota de {int(aliquota*10)}%')
    return aliquota * salario 
    
#####
valor_salario = float(input('Entre com o Valor do Salario Bruto'))
valor_beneficios = float(input('Entre com o Valor de Beneficios'))

valor_imposto = calcula_imposto(valor_salario)

valor_liquido = (valor_salario - valor_imposto) + valor_beneficios

print(f'O Salário vai cair na conta com R${valor_liquido:.2f} liquidos!')
