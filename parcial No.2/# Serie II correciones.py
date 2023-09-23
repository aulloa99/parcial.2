# Serie II correciones
mail = input("Ingrese su correo electrónico:")
cantidad = 0  
# Dar un valor inicial para 'cantidad'
x = 0  
# Dar un valor inicial para 'x'

while x < len(mail):  
    #'leng' debe ser reemplazado por 'len'
    if mail[x] == "@":
        cantidad += 1  
        # '+= 1' para incrementar 'cantidad'
    x += 1  
    # agregar'x' en lugar de 'X=x++1'

if cantidad == 1:
    print("El correo electrónico ingresado contiene solo un carácter '@'")
else:
    print("El correo electrónico es incorrecto")
