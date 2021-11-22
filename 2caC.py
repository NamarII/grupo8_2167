#Cambiar Mayusculas por Minusculas. (Ejemplo: "Hola Mundo" -> "hOLA mUNDO").
#Tiene como limite 100 caracteres.
string='Hola Mundo hola mundo HOLA MUNDO Hola Mundo hola mundo HOLA MUNDO Hola Mundo hola mundo HOLA MUNDO Hola Mundo hola mundo HOLA MUNDO Hola Mundo hola mundo HOLA MUNDO Hola Mundo hola mundo HOLA MUNDO Hola Mundo hola mundo HOLA MUNDO'
string_swaped=string.swapcase()
i=0
for i in range(101):
    i+=1
print(string_swaped)


