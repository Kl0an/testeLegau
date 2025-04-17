from datetime import date
import time as t

# ULTIMOS CONTEUDOS PYTHON
# DESAFIOS

# 1. Bem-vindo
user = input("Digite seu nome de Usuário: ")
print(f"Bem-vindo {user.title()}, você está terminando de estudar Python")  # aprovado

# 2. Quantos dias ele já viveu e quantos dias ele vai viver até os 90 anos
dia = date.today()
idade = int(input("Digite sua idade: "))

##(IMPORTANTE LER) #altere a data em "meuDia", para que as informações não saiam erradas, usei meu aniversário como exemplo!!!
meuDia = date(2008, 5, 22)
calcular = dia - meuDia
print(f"{calcular} vividos, aproximadamente.")  # aprovado
t.sleep(1)

dias_restantes = (90 - idade) * 365
print(f"Você tem {dias_restantes} dias até os seus 90 anos, aproximadamente.")  # aprovado
t.sleep(1)

# 3. Lista de desejos
desejos = ["nadar", "trabalhar", "namorar", "programar", "desenhar"]
for desejo in desejos:
    print(f"Gostaria de um dia poder {desejo.title()}.")
    t.sleep(1)  # aprovado

t.sleep(1)

# 4. Lista de comidas
comidas = ["banana", "pippo's", "laranja", "monster", "fígado"]
for comida in comidas:
    print(f"Eu irei comer {comida}")
    t.sleep(1)

print("Trocando 'fígado' por 'frango'...")
t.sleep(2)

for i in range(len(comidas)):
    if comidas[i] == "fígado":
        comidas[i] = "frango"
    print(f"Eu irei comer {comidas[i]}")
    t.sleep(1)  # aprovado

# 5. Mostrar apenas os pares, soma de tudo, maior e menor número
numeros = [1, 3, 7, 80, 23, 11, 24, 48]
numeros2 = []
print(f"Lista {numeros}")
t.sleep(2)

print("Pares: ")
t.sleep(2)
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        t.sleep(1)

# Soma total
print("Somando tudo...")
t.sleep(2)
somaTotal = sum(numeros)
print(somaTotal)
t.sleep(2)

# Maior e menor número
maiorNumero = max(numeros)
menorNumero = min(numeros)
print(f"Maior: {maiorNumero}")
print(f"Menor: {menorNumero}")
t.sleep(3)  # aprovado

# 6. Lista com cubos de 1 a 10. Mostrar os 3 primeiros, os 3 últimos e o meio
cubos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
aoCubo = [x ** 3 for x in cubos]
print(f"Números normais: {cubos}")
t.sleep(2)
print(f"Números ao cubo: {aoCubo}")
t.sleep(1)

primeiros = aoCubo[:3]
ultimos = aoCubo[-3:]
meio = aoCubo[4]
print(f"Os primeiros cubos são: {primeiros}")
print(f"Os últimos cubos são: {ultimos}")
print(f"O número do meio é: {meio}")  # aprovado

# 7. Faixa etária
idadeEtaria = int(input("Digite sua idade: "))
print("Analisando se você já pode arrumar emprego...")
t.sleep(3)
if idadeEtaria < 5:
    print("É uma criança ainda.")
elif idadeEtaria < 18:
    print("Já pode trabalhar, mas como menor aprendiz.")
elif idadeEtaria <= 60:
    print("Você já pode trabalhar.")
else:
    print("Saia daqui, múmia.")

t.sleep(2)

# 8. Validador de login
login = input("Usuário: ")
senha = input("Senha: ")
print(f"Bem-vindo, {login}")
if senha == 'admin':
    print("Você está em modo administrador")  # aprovado

# 9. Dicionários
animais = {'nome': 'banana', 'especie': 'cachorro', 'idade': 3}
print(animais)  # aprovado
t.sleep(2)

# Mini-glossário
glossario = {'Palavras Reservadas': 'True, False, If, Elif, Else...',
             'Funções embutidas': 'print(), len(), lower(), max(), min()',
             'Tipos numéricos': 'int, float',
             'Estrutura de dados': 'Usados para armazenar dados',
             'Strings': 'caracteres'}
print(glossario)  # aprovado
t.sleep(2)

# 10. Sonhos
while True:
    sonho = input("Qual seu maior sonho? (digite 'sair' para parar): ")
    if sonho == 'sair':
        break

# 11. Média final
soma = 0
contador = 0
print("Digite 'ok' para encerrar")
while True:
    entrada = input("Digite um número: ")
    if entrada == 'ok':
        break
    numeroMedio = float(entrada)
    soma += numeroMedio
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média é: {media:.2f}")
else:
    print("Nenhum número foi inserido.")  # reprovado (usei IA para me ajudar)

# 12. Funções
# Gerar frases
def trabalho(nome, profissao):
    carreira = f"{nome} está estudando {profissao}"
    return carreira

print(trabalho('Fabinho', 'Java'))  # aprovado

# Função de desconto
t.sleep(2)
print("Vamos calcular o desconto de um produto!")
t.sleep(2)
preco = float(input("Digite um preço: "))
desconto = float(input("Digite quantos % de desconto ele terá: "))
precoFinal = preco - (desconto * preco) / 100
print(f"Este produto vai custar R${precoFinal:.2f}")  # aprovado

t.sleep(3)

# 13. Classes
# Nome, idade e cidade de 3 pessoas
class Pessoa:
    def __init__(self, nome, idade, cidade, saudacao):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.saudacao = saudacao

    def exibirDados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nCidade: {self.cidade}\nEle se apresenta como: {self.saudacao}\n\n")
        # aprovado

# Classe de carro. Modelo, marca, ano. Métodos de acelerar e frear.
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def carroDados(self):
        print("="*10)
        print(f"Carro: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}")
        print("="*10)

    def acelera(self):
        print("Este carro está loucamente rápido")

    def freia(self):
        print("Este carro está parado")  # aprovado

# 14. Arquivos
# Pedir metas/sonhos e mostrar no txt (input)
sonhador = input("Seu sonho de vida: ")
comedor = input("Digite sua comida favorita: ")

with open("sonhos.txt", "w") as arquivo:
    ler = f"Sonho: {sonhador}\nComida favorita: {comedor}"

with open("sonhos.txt", "w") as arquivo:
    arquivo.write(ler)  # reprovado (não sabia o conteúdo e tive que pesquisar)

# 15. Exceções
# Pedir dois números e dividir
try:
    perguntinha = float(input("Digite um número: "))
    perguntinha2 = float(input("Digite um número: "))
    resultadoDivide = perguntinha / perguntinha2
    print(resultadoDivide)
except ZeroDivisionError:
    print("Impossível dividir por zero.")

# 16. Desafio Final para o avançado
# Abrir um arquivo .txt, pedir uma palavra e contar quantas vezes ela aparece

with open("lobo.txt", "r", encoding= 'utf-8') as lobo:
    ler = lobo.read()
    print(ler)
    t.sleep(5)
    pedirPalavra = input("Digite uma palavra do texto: ")
    contarPalavra = ler.lower().count(pedirPalavra.lower())

print(f"A palavra '{pedirPalavra}' aparece {contarPalavra} vezes.")  # aprovado
