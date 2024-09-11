# int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

# O resultado final da variável SOMA é 77

i = 12
soma = 0
k = 1

iteracao = 1

while (k < i):
    k += 1
    soma += k

print(soma)