# programa para invertir numeros de 4 digitos 1234 a 4321
print("-----------------------------")
print("digite su numero de 4 digitos")
print("-----------------------------")

# input
n= int(input("digite su numero de 4 digitos"))

# processing

d1= ((n%10)*1000)
pe= n//10
d2= ((pe%10)*100)
pe= pe//10
d3= ((pe%10)*10)
d4= pe//10

ni= (d1+d2+d3+d4)

# output
print("-----------------------------")
print("resultados numeros invertidos")
print("-----------------------------")
print("el numero inverso es" + str(ni))