# Criar uma string com a frase
frase = 'Aqui está um teste para checar as letras "A" na frase.'
print(frase)

# Criar a função para contar
def contar_a(frase):
    conta_a = frase.lower().count('a')
    if conta_a > 0:
        return f'A letra "A" aparece {conta_a} vezes na frase'
    else:
        return f'A letra "A" não aparece na frase'
# Chamar a função

print(contar_a(frase))