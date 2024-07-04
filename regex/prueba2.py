import re


nombre = input("Ingrese su nombre")

nombreReg = re.compile(r"^[A-Z][a-z]*$")

if nombreReg.match(nombre):
    print("Nombre Valido")
else:
    print("Nombre no valido")