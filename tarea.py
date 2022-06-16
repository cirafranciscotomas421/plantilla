num1=int(input("ingrese el primer número"))
num2=int(input("ingrese el segundo número"))
suma=num1+num2
resta=num1-num2
multiplicación=num1*num2
if num2==0:
    print(f"La suma es={suma},\n La resta es= {resta},\n La multiplicación es:,{multiplicación},\n divisió no se puede dividir entre cero")
else:
    division=num1/num2
    print(f"La suma es={suma} \n La resta es={resta} \n La multiplicación es:{multiplicación},\n La división es: {division}")