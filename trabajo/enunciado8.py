igual, aux = 0, 0
print("Recomendacion: Omita los espacios al ingresar")
texto = input("Ingrese la palabra que desea evaluar: ")
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  print("El texto es palindromo!")
else:
  print("El texto no es palindromo!")

print("Largo del texto: ",len(texto))