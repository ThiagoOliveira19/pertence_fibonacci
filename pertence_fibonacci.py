def pertence_fibonacci(numero):
    if numero < 0:
        return False
    
    
    a, b = 0, 1
    
    
    if numero == a or numero == b:
        return True
    
    
    while b <= numero:
        a, b = b, a + b
        if b == numero:
            return True
    
    return False

def main():
    
    try:
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    except ValueError:
        print("Por favor, insira um número inteiro.")
        return
    
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
