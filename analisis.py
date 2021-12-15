import time
def suma_lineal(n):
    suma = 0
    for i in range(n+1):
        suma += i
    return suma
def suma_constante(n):
    return (n/2) * (n+1)
cantidad = 1000000

for i in range(4):
    t0 = time.time()
    suma1 = suma_lineal(cantidad)
    t1 = time.time()
    suma2 = suma_constante(cantidad)
    t2 = time.time()
    print (f"Analisis del algoritmo entrada de: {cantidad}")
    print (f"Resultado en suma con complejidad lineal    ||cantidad->{round(suma1)} tiempo/s->{round(t1-t0)}")
    print (f"Resultado en suma con complejidad constante ||cantidad->{round(suma2)} tiempo/s->{round(t2-t1)}")
    cantidad *= 10
