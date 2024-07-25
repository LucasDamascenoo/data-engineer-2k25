cardapio = {"salada": 20, "macarrão": 10, "sorvete:": 10}

print(cardapio.keys())
print(type(cardapio.values()))


# podemos alterar o valor de uma chave do nosso cardapío

cardapio['salada'] = 30

# adicionando um novo par de chave valor

cardapio['chocolate'] = 6


nome = {'maria': 18,
        'jose': 50,
        'ana': 39,
        'fernanda': 22}


print(dict(sorted(nome.items())))

print(nome.items())
