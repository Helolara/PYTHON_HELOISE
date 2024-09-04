#Ordenação Total  

calçados = [
    {"tipo": "Tênis", "nome": "Nike Air"},
    {"tipo": "Sandália", "nome": "Ipanema"},
    {"tipo": "Bota", "nome": "Coturno"}, 
    {"tipo": "Sandália", "nome": "Havaianas"},
    {"tipo": "Sapatilha", "nome": "Melissa"},
]

calçados_ordenados = sorted(calçados, key=lambda x: (x["tipo"], x["nome"]))

print("Calçados ordenados por tipo e nome:")
for calçado in calçados_ordenados:
    print(f"Tipo: {calçado['tipo']}, Nome: {calçado['nome']}") 
