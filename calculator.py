# Limpando terminal
import os
def limpar_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Pedindo os números em binário para o usuário
def inserir_binarios():
    numero_str1 = str(input("Digite o primeiro binário: "))
    numero_str2 = str(input("Digite o segundo binário: "))
    print("")
    return numero_str1, numero_str2

# Definindo tamanho máximo para que os dois números digitados tenham o mesmo tamanho, evitando erro de loop
def igualar_tamanhos(numero_str1, numero_str2):
    tamanho_maximo = max(len(numero_str1), len(numero_str2))
    numero_str1_ajustado = numero_str1.zfill(tamanho_maximo)
    numero_str2_ajustado = numero_str2.zfill(tamanho_maximo)
    return numero_str1_ajustado, numero_str2_ajustado

# Criando loop com número de caracteres da lista, validando os números de trás para frente
def somar_binarios(binary1, binary2):
    carry = 0
    resultado = []
    for i in range(len(binary1) -1, -1, -1):
        soma = int(binary1[i]) + int(binary2[i]) + carry

        # Validando a soma e o carry comparado com o resultado da soma
        if soma == 2:
            soma = 0
            carry = 1
        elif soma == 3:
            soma = 1
            carry = 1
        elif soma == 0:
            soma = 0
            carry = 0
        elif soma == 1:
            soma = 1
            carry = 0

        # Adicionando o valor da soma na lista resultado usando insert (0) para adicionar de trás para frente (considerando o loop inverso)
        resultado.insert(0, soma)
    return resultado, carry

# Exibindo resultado juntando todos os itens da lista
def exibir_resultado(resultado):
    print("".join(map(str, resultado)))

# Executando todas as funções
def main():
    limpar_terminal()
    numero_str1, numero_str2 = inserir_binarios()

    # Criando uma lista para cada número digitado
    binary1 = []
    binary2 = []

    numero_str1_ajustado, numero_str2_ajustado = igualar_tamanhos(numero_str1, numero_str2)

    # Adicionando cada caractere na lista binary1
    for i in range(len(numero_str1_ajustado)):
        digito1 = numero_str1_ajustado[i]
        binary1.append(digito1)

    # Adicionando cada caractere na lista binary2
    for i in range(len(numero_str2_ajustado)):
        digito2 = numero_str2_ajustado[i]
        binary2.append(digito2)

    # Criando uma terceira lista para guardar o resultado da validação das listas binary1 e binary2
    resultado = []

    resultado, carry_final = somar_binarios(binary1, binary2)

    # Cobrindo a possibilidade de sobrar 1 no carry, fazendo com que ele seja inserido antes da lista
    if carry_final == 1:
        resultado = [carry_final] + resultado

    exibir_resultado(resultado)

main()
