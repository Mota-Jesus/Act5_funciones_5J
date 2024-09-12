print("Ejemplo de funciones")
# declarando funciones
def hola():
    print("Alguien uso la funcion hola")
    
def chat(mensa):
    print(f"VATO: {mensa}")
    
def ellacontesta(mensa):
    print(f"MORRA: {mensa}")
    
def escribenombre(ap,n):
    print(f"Tu nombre completo es: {n} {ap}")
    
def suma(a,b):
    s=a+b
    return s

def resta(a,b):
    r=a-b
    return r

def multiplicacion(a,b):
    m=a*b
    return m

def division(a,b):
    d=a/b
    return d
    
    
## llamadas a funciones
hola()
chat("Que bonita estas")
ellacontesta("Gracias")
escribenombre("Mota","Jesus")
print("Operaciones Basicas")
print("SUMA")
c1=int(input("Ingresa un numero: "))
c2=int(input("Ingresa otro numero: "))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")
print("RESTA")
c1=int(input("Ingresa un numero: "))
c2=int(input("Ingresa otro numero: "))
dameresta=resta(c1,c2)
print(f"La resta de {c1} - {c2} = {dameresta}")
print("MULTIPLICACION")
c1=int(input("Ingresa un numero: "))
c2=int(input("Ingresa otro numero: "))
damemultiplicacion=multiplicacion(c1,c2)
print(f"La multiplicacion de {c1} * {c2} = {damemultiplicacion}")
print("DIVISION")
c1=int(input("Ingresa un numero: "))
c2=int(input("Ingresa otro numero: "))
damedivision=division(c1,c2)
print(f"La division de {c1} / {c2} = {damedivision}")
