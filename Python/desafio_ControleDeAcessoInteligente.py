### DESAFIO - CONTROLE DE ACESSO INTELIGENTE ###
'''
Uma biblioteca está implementando um sistema automatizado para liberar o acesso à área de livros raros. 
O sistema deve permitir a entrada apenas para visitantes autorizados e com idade mínima de 18 anos. 
Para isso, é necessário utilizar operadores lógicos, estruturas condicionais (if, else, else if) e conceitos básicos como tipos primitivos e palavras-chave. 
Desenvolva um programa que verifique se o visitante pode acessar a sala especial.
'''
################################# RESPOSTA CORRETA PELA PLATAFORMA #######################################################
def age_permission_check(*,age,permission):
  if permission == False and age != 16:
    msg = 'Acesso negado'
  elif permission == True and age <= 18:
    msg = 'Idade insuficiente'
  elif permission == True and age >= 18:
    msg = 'Acesso permitido'
  return msg

def main():
    # Entrada de dados do usuário
    has_permission = input().lower() == "true"  
    age = int(input()) 
    
    system_msg = age_permission_check(age=age,permission = has_permission)
    print(system_msg)

if __name__ == "__main__":
    main()

##################################################### RESOLUÇÃO #######################################################

def age_permission_check(*,age,permission):
  if permission == False and age != 16:
    msg = 'Acesso negado'
  elif permission == True and age <= 18:
    msg = 'Idade insuficiente'
  elif permission == True and age >= 18:
    msg = 'Acesso permitido'
  return msg

def main():
    # Entrada de dados do usuário
    has_permission = input().lower() == "true"  
    age = int(input()) 
    
    system_msg = age_permission_check(age=age,permission = has_permission)
    print(system_msg)

if __name__ == "__main__":
    main()
