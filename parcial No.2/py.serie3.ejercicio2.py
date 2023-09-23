import sys

def sumar_valores(valores):
    suma = sum(valores)
    return suma

def calcular_promedio(valores):
    suma = sum(valores)
    promedio = suma / len(valores)
    return promedio

def main():
    valores_str = sys.argv[1].split(",")
    valores = [float(valor) for valor in valores_str] 
    suma = sumar_valores(valores)
    promedio = calcular_promedio(valores)
    
    print(f"La suma es {suma}")
    print(f"El promedio es {promedio}")

if __name__ == "__main__":main()
