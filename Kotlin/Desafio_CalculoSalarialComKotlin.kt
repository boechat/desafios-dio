######################################### Calculo Salarial KOTLIN ############################################
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

## Em KOTLIN 

object ReceitaFederal {
    fun calcularImposto(salario: Double): Double{
        val aliquota = when{
            (salario >= 0 && salario <= 1100) -> 0.05
            (salario >= 1100.01 && salario <= 2500.00) -> 0.1
            else -> 0.15
        }
    }
}

fun main() {
    val valorSalario = readLine()!!.toDouble();
    val valorBeneficios = readLine()!!.toDouble();
    
    val valorImposto = ReceitaFederal.calcularImposto(valorSalario);
    val saida = valorSalario - valorImposto + valorBeneficios;
    
    println(String.format("%.2f",saida));
}