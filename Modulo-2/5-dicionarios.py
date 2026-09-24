# HashMap

dicionario_pessoa = {
    "nome":"Marina",
    "idade":34,
    "cidade":"Fortaleza"
}

print("=== Dicionário original ===")
print(dicionario_pessoa)

# Adicionando nova chave: altura
dicionario_pessoa.update({"altura": 1.60})
print("=== Dicionário com adição de chave altura ===")
print(dicionario_pessoa)