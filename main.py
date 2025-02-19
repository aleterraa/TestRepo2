#Inizializzo una variabile di prova
x = 10

#Stampo il valore di x
print(f"Il valore di x è: {x}")

#Aggiungo una seconda variabile y = 2 * x
y = 2 * x

#Stampo il valore di y
print(f"Il valore di y è: {y}")

with open("test.txt", "a") as file:
    file.write("Hello World!")
    file.close()