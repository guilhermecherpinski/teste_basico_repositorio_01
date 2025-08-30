def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def main():
    print("Calculadora Básica")
    print("Operações disponíveis: +, -, *, /")
    a = float(input("Digite o primeiro número: "))
    op = input("Digite a operação (+, -, *, /): ")
    b = float(input("Digite o segundo número: "))

    if op == '+':
        resultado = soma(a, b)
    elif op == '-':
        resultado = subtrai(a, b)
    elif op == '*':
        resultado = multiplica(a, b)
    elif op == '/':
        resultado = divide(a, b)
    else:
        resultado = "Operação inválida"

    print("Resultado:", resultado)

if __name__ == "__main__":
    main()