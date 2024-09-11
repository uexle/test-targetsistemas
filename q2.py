entrada = input()
entrada = entrada.lower()
listaCaracteres = list(entrada)

ocorrencia = 0

for caractere in listaCaracteres:
    if caractere == "a":
        ocorrencia += 1

if ocorrencia == 0:
    print("a string nao possui nenhuma letra a")
elif ocorrencia == 1:
    print(f"a string possui {ocorrencia} letra a")
else:
    print(f"a string possui {ocorrencia} letras a")