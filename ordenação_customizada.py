#Ordenação Customizada

calçados = ["Tênis", "Sandália", "Bota", "Chinelo", "Sapatilha"]

calçados_ordenados = sorted(calçados, key=len)

print("Calçados ordenados por comprimento do nome:")
for calçado in calçados_ordenados:
    print(calçado)
