# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '9'
texto_2 = '0'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print("el {} es mayor alfabeticamente que {}".format(texto_1, texto_2))
else: 
    print("el {} es mayor alfabeticamente que {}".format(texto_2, texto_1))

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.

texto_1_int = int(texto_1)
texto_2_int = int(texto_2)

# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

if texto_1_int > texto_2_int:
    print("el {} es mayor que {}".format(texto_1_int, texto_2_int))
else:
    if texto_1_int < texto_2_int: 
        print("el {} es mayor que {}".format(texto_2_int, texto_1_int))
    else: 
        print("ambas son de igual tamaño")
# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
