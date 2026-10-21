# Lista de convidados VIP (pode ser modificada nos testes)
convidados_vip = ["Alice", "Bob", "Carol"]

# Função para verificar se a idade permite entrada
def verificar_idade(idade):
    if idade >= 18:
        return "Entrada permitida. Bem-vindo ao evento!"
    else:
        return "Entrada negada. Este evento é apenas para maiores de idade."

# Função para verificar se o nome está na lista VIP
def verificar_vip(nome):
    if nome.lower() in [c.lower() for c in convidados_vip]:
        return "Você é um convidado VIP! Aproveite o evento com acesso especial."
    else:
        return None

# Programa principal
def main():
    while True:
        idade_input = input("Qual a sua idade? ")

        if idade_input.lower() == "sair":
            break

        try:
            idade = int(idade_input)
        except ValueError:
            print("Por favor, digite uma idade válida.")
            continue

        menssagem = verificar_idade(idade)
        print(menssagem)

        if idade >= 18:
            nome = input("Qual o seu nome? ")
            if nome.lower() == "sair":
                break
            menssagem_vip = verificar_vip(nome)
            if menssagem_vip:
                print(menssagem_vip)

        # ---- NOVO: pergunta se quer repetir ----
        repetir = input("Deseja repetir o processo? (s/n): ")
        if repetir.lower() != "s":
            print("Programa encerrado. Até logo!")
            break

if __name__ == "__main__":
    main()


# while True:
#     ├─ pede idade
#     ├─ "sair"? → break (sai)
#     ├─ não é número? → aviso + continue (volta ao topo)
#     ├─ imprime mensagem de idade
#     └─ idade >= 18?
#           ├─ pede nome
#           ├─ "sair"? → break
#           ├─ é VIP? → imprime mensagem VIP
#           └─ (se não VIP, não imprime nada)