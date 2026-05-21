# Exercício 18 – Conversão de Unidades Encadeada

metros = float(input("Digite a distância em metros: "))

print()
print(f"Metros   : {metros:.4f} m")
print(f"Km       : {metros / 1000:.4f} km")
print(f"Cm       : {metros * 100:.4f} cm")
print(f"Mm       : {metros * 1000:.4f} mm")
print(f"Polegadas: {metros * 39.3701:.4f} pol")
print(f"Pés      : {metros * 3.28084:.4f} pés")