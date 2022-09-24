'1)Criar uma lista e percorrer seu conteúdo inteiro'

listadenomes = ["Juan", "Marcio", "Israel","Pedro", "Samuel"]
print(listadenomes)
listaidades = [40, 20, 30, 25, 35]
print(listaidades)

'2)Acrescentar a lista criada acima mais dois nomes'

listadenomes.append(["Matheus", "Jhenifer"])
print(listadenomes)

'3 Receber um nome e 3 notas calcular a média final se a média  for maior que 7 aprovado se não reprovado'

nota1= float(input("Digite nota 1"))
nota2=float(input("Digite nota 2"))
nota3=float(input("Digite nota 3"))
media_final = float(nota1 + nota2 + nota3)/3

if media_final >= 7.0:
  print(f'Sua média é {media_final:>= 7} - Aprovado')

else:
  print(f'Sua média é {media_final:>= 7} - Reprovado')

'4) Criar um algoritmo que receba o salario de um funcionário e informe a ele o valor de desconto do INSS e seu salário liquido'

salario_fixo = float(input ('Digite o sálario fixo: '))
Percentual_inss = 7.5/100
Percentual_inss2 = 9/100
Percentual_inss3 = 12/100
Percentual_inss4 = 14/100
desconto_INSS = salario_fixo * Percentual_inss
desconto_INSS2 = salario_fixo * Percentual_inss2
desconto_INSS3 = salario_fixo * Percentual_inss3
desconto_INSS4 = salario_fixo * Percentual_inss4
salario_liquido= salario_fixo - desconto_INSS
salario_liquido2= salario_fixo - desconto_INSS2
salario_liquido3= salario_fixo - desconto_INSS3;
salario_liquido4= salario_fixo - desconto_INSS;

if salario_fixo<=1212:
  print(f'O valor descontado do INSS foi:{desconto_INSS}')
  print(f'Salário liquido é:{salario_liquido}')

if salario_fixo>= 1212.01 and salario_fixo<= 2427.35:
  print(f'O valor descontado do INSS foi:{desconto_INSS2}')
  print(f'Salário liquido é:{salario_liquido2}')

if salario_fixo>=2427.36 and salario_fixo<= 3641.03:
  print(f'O valor descontado do INSS foi:{desconto_INSS3}')
  print(f'Salário liquido é:{salario_liquido3}')

if salario_fixo>=3641.04 and salario_fixo<=7087.22:
  print(f'O valor descontado do INSS foi:{desconto_INSS4}')
  print(f'Salário liquido é:{salario_liquido4}')

'5) Criar um algoritmo que receba dois valores e pergunte ao usuário qual tipo de cálculo deseja que seja feito. (soma Subtração, multiplicação ou divisão) com a indicação do usuário efetuar a operação matemática'
valor1 = float(input("Digite um valor:"))
valor2 = float(input("Digite um segundo valor:"))
operacao = input("Digite a operação a realizar: (soma,subtração,multiplicação ou divisão):")

if operacao == "soma":
    print("O resultado é:" , valor1 + valor2)
if operacao == "subtração":
    print("O resultado é:", valor1 - valor2)
if operacao == "multiplicação":
    print("O resultado é:" , valor1 * valor2)
if operacao == "divisão":
    print("O resultado é:" , valor1/valor2)

'6)criar um programa que calcule celsius para farenheit e ao contrário também'

def menu_inicial():
  print('Programa para Conversão de Temperaturas')
  print('1. Converter de Celsius para Fahrenheit')
  print('2. Converter de Fahrenheit para Celsius')

def cel_fahr():
  C = float(input('Entre com a temperatura em graus Celsius: '))
  F = C * (9 / 5) + 32
  print('Valor em Fahrenheit: {0}°F'.format(F))

def fahr_cel():
  F = float(input('Entre com a temperatura em graus Fahrenheit: '))
  C = (F - 32) * (5 / 9)
  print('Valor em Celsius: {0}°C'.format(C))

if __name__ == '__main__':
  menu_inicial()
  escolha = input('Escolha o tipo de conversão que deseja realizar: ')

  if escolha == '1':
    cel_fahr()

  if escolha == '2':
    fahr_cel()

'7) Receba o nome do aluno, três notas (trab(4), teste(3), prova(5))vai calcular média poderada exibir a média'

nome= input("Digite o nome do aluno:")
trabalho= float(input("Digite a nota do trabalho:"))
teste= float(input("Digite a nota do teste:"))
prova= float(input("Digite a nota da prova:"))
media_ponderada = (trabalho*4) + (teste*3) + (prova*5)/12
print(f'A média do aluno foi:{media_ponderada}')

'8 tabuada de acordo com a escolha do cliente e ao final perguntar se ele deseja uma nova tabuada'

tabuada=int(input("Tabuada do numero: "))

for count in range(10):
  print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
pergunta = input("Deseja uma nova tabuada?")
while pergunta== 'Sim':
   tabuada=int(input("Tabuada do numero: "))
   for count in range(10):
     print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
   pergunta = input("Deseja uma nova tabuada?")
else:
  print("Encerrou")









