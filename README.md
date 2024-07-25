# data-engineer-2k25

Anotações referente aos estudos sobre engenharia de dados:


## Roadmap

1. SQL
2. PYTHON



# Bootcamp

## Módulo 00

### SQL - Introdução

### Python - Introdução

- Com o Python podemos automatização de tarefas, realizar analises de dados, otimizar processos, buscar dados em banco de dados, web scraping

- Python é uma linguagem de programação interpretada, orientada a objeto, tem uma sintax simples, suporta modulos e pacotes(pandas/spark)

- Python possui Peps para melhorias da linguagem (pep:8 - 20 e 257) são as coringas

- Python tem duas versões 2(não recebe atualizações desde 2020) e 3 

- Podemos utilizar pYhton no terminal, ides(vscode-pycharm) ou com pacotes(tras mais bibliotecas) como o anacondas


### Python - Variáveis e tipos

- Variaveis são responsaveis por guardar um determinado valor/tipo no nosso programa


#### Tipos Escalares

Os dados de tipos escalares são:

- int
- float
- string
- bool

#### Tipos variaveis

- llist : []
- tuple : ()
- set : 
- dict : Conjunto de chave valores {'id':1010}
- range : range(1:10)

#### Operadores

Dentro do python e outras linguagem existe dois tipos de operadores: Numericos (retornam um int/float) e lógicos(retornam um boleano(True / False))

- Numericos: + , -  , * , ** , / , %

- Logicos: &(and) , |(or) , == (igual) , !=(diferente), > (maior) , < (menor) , is (referencia o mesmo valor) , is not (referencia valores diferente)


### Python - Manipulação de strings

Quando trabalhamos com strings temos alguns métodos e propriedades que facilitam o trabalho com esse tipo de dado

- Concatenação de strings: hoje usamos o ***F strings** que falicita juntar textos e variaveis

```python:

print(textos.split("_"))
print(textos.upper())
print(textos.lower())
print(textos.islower())

```
### Python - Dicionarios

Dicionarios é uma estrutura de dados compostas por chave e valor 

Concatenação de strings: hoje usamos o ***F strings** que falicita juntar textos e variaveis

```python:

cardapio =  {"salada":20,"macarrão: 10","sorvete:":10}

```

- keys(): retorna todas as chaves unicas dos nossos dicionarios (salada,macarrao)
- values(): retorna todos os valores dos nossos dicionarios (20,10,30)
- items(): retorna uma tupla dos nossos chaves e valores

### Python - Listas

listas é um conjunto de valores que podemos armazenar qualquer tipo de dado (mas por convensão) fazemos isso com apenas um tipo, seus valores são acessados através de index(base zero). 

```python:
lista = [1, 2, 3, 4, 5, 600, 800]
lista2 = [1, 2, 3, 4, 5, 56]
tudo = [lista + lista2]

```

- pop(): remove o ultimo elemento de uma lista
- reverse(): inverte a ordem da nossa lista
- insert(): podemos adicionar um determinado valor no index passado
- sort() : ordena a lista de
- append(): insere uma lista na nossa lista
- max() : retorna o valor maximo de uma lista
- remove(): remove um valor especifico da nossa lista

### Python - Range

Com o range podemos criar um sequencia de valores de acordo com o range passado

Concatenação de strings: hoje usamos o ***F strings** que falicita juntar textos e variaveis

```python:

intervalo = range(1, 10)
list(intervalo)

```
- range(1,10):cria um sequencia de valores de 1 a 9 (não inclusivo)
- range (10,0,-1) : cria uma sequencia descrecente




## Módulo 01

### Introdução à Engenharia de Dados