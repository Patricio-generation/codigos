lista=[]
añadir= (input("Añade los numeros que quieras separados por un espacio: "))
listanum=[float(num)for num in añadir.split(" ")]

def addmultiplenumbers(x):
  suma = sum(x)
  return suma
print(f"{addmultiplenumbers(listanum)}")