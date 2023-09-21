def multiplicacion(a,b):
  x= a*b
  return  x

def division (a,b):
  x= a/b
  return x

print ("Dame el primer número:")
a= int  (input())
print ("Dame el segundo número:")
b= int (input())
print ("La multiplicación da", multiplicacion (a,b), "y la division da", division (a,b))

def conversion (k,m):

  x= k*m
  return x

print("¿Cuantos kilometros recorriste?")
k= int(input())
m=1000
print("Recorriste:",conversion (k,m),"metros")

def area_triangulo (b,a):
  x= (a*b)/2
  return x

print("¿Cual es la base?")
b= int(input())
print("¿Cual es la altura?")
a= int(input())
print("La área del triagulo es:", area_triangulo (b,a), "m^2")
