
conjunto = {'ana', 'maria', 'jose'}
conjunto2 = {'ana', 'joao', 'marta'}


# verificar os valores iguais nos conjuntos/interserção

print(conjunto.intersection(conjunto2))

# {ana}

# unindo 2 conjuntos

total = conjunto.union(conjunto2)
print(total)

# {'jose', 'joao', 'maria', 'marta', 'ana'}


# verificando o que tem no conjunto 1 e não no conjunnto 2
