texto = input("Digite um texto para verificar se há a letra (A) nele: ")
count = 0

for i in texto:
    if i.lower() == "a":
        count += 1

if count == 0:
    print("Nenhuma letra 'A' foi encontrada")
else:
    print(f"A letra 'A' foi encontrada {count} vezes, não importando se é maiúscula ou minúscula!")


## Pode ser feito assim também:

# texto = input("Digite um texto para verificar se há a letra (A) nele: ")
# count = texto.lower().count("a")
# print(f"A letra 'A' foi encontrada {count} vezes, não importando se é maiúscula ou minúscula!")
# Não sabia se poderia usar o método count() para contar as letras, então fiz de outra forma.