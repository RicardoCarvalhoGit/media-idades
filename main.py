import os 
import datetime

today = datetime.date.today().year
ano = today

continua = 's'
totIdade = 0
contador = 0
idade = 0
maiorIdade = idade
menorIdade = 999
menor18 = 0
entre18e25 = 0
maior25 = 0
nomes = []
idades = []


while continua == 's':


  nome = input ("Qual o seu nome? \n")
  anoNasc = int (input ("Que ano você nasceu? \n"))
  idade = ano - anoNasc
  nomes.append(nome)
  idades.append(idade)
  totIdade = totIdade + idade
  contador = contador + 1
  continua = input ("Tem mais alguém no local (Responda com 's' para sim e 'n' para não) \n")


  os.system("cls")


  if contador == 1:
    print (contador, "pessoa já respondeu")
    print ("********************")
  else:
    print (contador, "pessoas já responderam")
    print ("********************")


  if idade > maiorIdade:
    maiorIdade = idade
  if idade < menorIdade:
    menorIdade = idade
  if idade < 18:
    menor18 = menor18 + 1
  if idade >= 18 and idade <= 25:
    entre18e25 = entre18e25 + 1
  if idade > 25:
    maior25 = maior25 + 1


  media = totIdade / contador
  menorPorcento = menor18 / contador
  entrePorcento = entre18e25 / contador
  maiorPorcento = maior25 / contador


print ("Lista de dados")
print ("********************")
for i in range (len(nomes)):
  print(nomes [i]," tem ", idades[i])
print ("********************")
print ("Média das idades = ", media)
print ("********************")
print ("Quantidade de alunos = ", contador)
print ("********************")
print ("Maior idade = ", maiorIdade)
print ("Menor idade = ", menorIdade)
print ("********************")
print ("Pessoas com menos de 18 anos = ", menor18)
print ("Pessoas entre 18 e 25 anos = ", entre18e25)
print ("Pessoas com mais de 25 anos = ", maior25)
print ("********************")
print ("Percentual de pessoas com menos de 18 = ", menorPorcento * 100, "%")
print ("Percentual de pessoas entre 18 e 25 = ", entrePorcento * 100, "%")
print ("Percentual de pessoas com mais de 25 = ", maiorPorcento * 100, "%")


continua = 'n'


while continua == 'n':
  
  print ("********************")
  nomespesq = input("Deseja saber a idade do(a):\n")
  for i in range(len(nomes)):
    if nomespesq == nomes[i]:
      break
  if nomespesq == nomes[i]:
    continua = 's'
    print("A idade de ", nomespesq, " é ",idades[i])
  else:
    continua = 'n'
    print ("********************")
    print ('Erro! Pessoa não encontrada.')
    input ('Aperte enter para pesquisar novamente.')
    os.system('cls')
