import os 

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
  idade = int (input ("Qual a sua idade? \n"))
  nomes.append(nome)
  idades.append(idade)
  totIdade = totIdade + idade
  contador = contador + 1
  continua = input ("Tem mais alguém no local (Responda com 's' para sim e 'n' para não) \n")

  os.system("cls")

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

print ("Nome")
print ("********************")
for i in range (len(nomes)):
  print(nomes [i]," tem ", idades[i])
print ("Média = ", media)
print ("Quantidade de alunos = ", contador)
print ("Maior idade = ", maiorIdade)
print ("Menor idade = ", menorIdade)
print ("Pessoas com menos de 18 anos = ", menor18)
print ("Pessoas entre 18 e 25 anos = ", entre18e25)
print ("Pessoas com mais de 25 anos = ", maior25)
print ("Percentual de pessoas com menos de 18 = ", menorPorcento * 100, "%")
print ("Percentual de pessoas entre 18 e 25 = ", entrePorcento * 100, "%")
print ("Percentual de pessoas com mais de 25 = ", maiorPorcento * 100, "%")


nomespesq = input("Deseja saber a idade do(a):")
for i in range(len(nomes)):
  if nomespesq == nomes[i]:
    break
if nomespesq == nomes[i]:
    print("A idade é: ",idades[i])
else:
    print ("Pessoa não incontrada!!")