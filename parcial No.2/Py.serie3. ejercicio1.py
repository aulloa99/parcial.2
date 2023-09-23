def contar_letras(texto, letra):
    texto = texto.lower()
    letra = letra.lower()
    
    cantidad = texto.count(letra)
    
    return cantidad

texto = input("Ingrese un texto: ")
letra = input("Ingrese una letra: ")

cantidad = contar_letras(texto, letra)

print(f"La letra '{letra}' aparece {cantidad} veces en el texto.")
