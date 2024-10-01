# Definindo a sequência de Fibonacci

def fibonacci(n):
    seq = [0, 1]
    while seq [-1] < n:
        seq.append(seq[-1] + seq[-2])
    return seq

# validação do número informado

def pert_seq(n1):
    seq = fibonacci(n1)
    if n1 in seq:
        return f"O numero {n1} faz parte da sequência fibonacci."
    else:
        return f"o número {n1} não faz parte da sequência fibonacci."

# Requisição do informe de número para a função

n1 = int(input("Escolha um número: "))
print(pert_seq(n1))