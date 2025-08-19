######################################### Calculo Salarial Com C# ############################################
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

## Em C#

using System;

public class Desafio 
{
    public static void Main()
    {        
        float valorSalario = float.Parse(Console.ReadLine());
        float valorBeneficios = float.Parse(Console.ReadLine());
        
        float valorImposto = 0;
        if (valorSalario >= 0 && valorSalario <= 1100){
            valorImposto = 0.05F * valorSalario;
        } else if (valorSalario = 1100 && valorSalario <= 2500){
            valorImposto = 0.1F * valorSalario;
        } else (valorSalario >2500){
            valorImposto = 0.15F * valorSalario;
        }
        
        float saida = valorSalario - valorImposto + valorBeneficios;
        Console.WriteLine(sida.ToString("0.00"));
    }
}