# programa para jugar piedra o tijera en python

#libreria
from curses import user_number
import random
import math

#
#imput
print("                                         ")
print("             piedra papel o tijera       ")
print("                                         ")
print("   pi = piedra pa = papel t = tijera     ")

compuer_number = random.randint(1,3)

compuer_number = random(input("¿que escoges?: "))

#
#processing
#

if(compuer_number == user_number):
    print("  ")
    print("empate")
elif((user_number == 3 and compuer_number == 2 )or(user_number == 1 and compuer_number == 3)or(user_number == 2 and compuer_number == 1)):
    print(" ")
    print(" ganaste")
else:
    print(" ")
    print("la computadora gana")

#
#output
#

print("  ")
print(" la computadora eligio: " + str(compuer_number))
print("  ")
