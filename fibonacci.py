number = int(input("Entre com o número para verificar se ele faz parte da Fibonecci: "))
list_fibonacci = [0, 1]

def fibonacci(number):
    n_antes, n_depois = 0, 1
    while n_depois <= number:
        temp = n_antes
        n_antes = n_depois
        n_depois = temp + n_depois
        list_fibonacci.append(n_depois)
        
    return n_depois >= number

fibonacci(number)

print(f"Lista Fibonacci: {list_fibonacci}")

if number in list_fibonacci:
    print(f"O número {number} faz parte da sequência de Fibonacci")
else:
    print(f"O número {number} não faz parte da sequência de Fibonacci")