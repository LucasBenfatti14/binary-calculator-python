import os
def limpar_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def inserir_binarios():
    numero_str1 = str(input("Digite o primeiro binário: "))
    numero_str2 = str(input("Digite o segundo binário: "))
    print("")
    return numero_str1, numero_str2

def igualar_tamanhos(numero_str1, numero_str2):
    tamanho_maximo = max(len(numero_str1), len(numero_str2))
    numero_str1_ajustado = numero_str1.zfill(tamanho_maximo)
    numero_str2_ajustado = numero_str2.zfill(tamanho_maximo)
    return numero_str1_ajustado, numero_str2_ajustado

def somar_binarios(binary1, binary2):
    carry = 0
    resultado = []
    for i in range(len(binary1) -1, -1, -1):
        soma = int(binary1[i]) + int(binary2[i]) + carry

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

        resultado.insert(0, soma)
    if carry == 1:
        resultado.insert(0, carry)
    return resultado

def exibir_resultado(resultado):
    print("".join(map(str, resultado)))

def main():
    limpar_terminal()
    numero_str1, numero_str2 = inserir_binarios()

    binary1 = []
    binary2 = []

    numero_str1_ajustado, numero_str2_ajustado = igualar_tamanhos(numero_str1, numero_str2)

    for i in range(len(numero_str1_ajustado)):
        digito1 = numero_str1_ajustado[i]
        binary1.append(digito1)

    for i in range(len(numero_str2_ajustado)):
        digito2 = numero_str2_ajustado[i]
        binary2.append(digito2)

    exibir_resultado(somar_binarios(binary1, binary2))

main()