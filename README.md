# Piedra-papel-o-tijera
JUGAR PIEDRA PAPEL O TIJERA CON PY

### Analisis

### variables de entrada
compuer_number = random.randint(1,3)

compuer_number = random(input("¿que escoges?: "))

### procesamiento
if(compuer_number == user_number):
    print("  ")
    print("empate")
elif((user_number == 3 and compuer_number == 2 )or(user_number == 1 and compuer_number == 3)or(user_number == 2 and compuer_number == 1)):
    print(" ")
    print(" ganaste")
else:
    print(" ")
    print("la computadora gana")

## Diseño

![diagrama de flujo](diagrama.png)
