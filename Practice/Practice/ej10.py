def letra_mas_comun(palabra:str)->str:
    letras_dic = dict()  #Guarda repetición de letras
    contador = 0 #Caracteres que se repiten

    for letra in palabra: #Por cada letra
        if letra==" " or  letra=="." or letra==",":
            continue
        if letra in letras_dic: #Si ya estaba en el dic() significa que se repite
            if letras_dic[letra] == 1: 
                contador += 1 #Se agrega al contador
            letras_dic[letra] += 1 #Continua el conteo
        else:
            letras_dic[letra] = 1 #Si la letra no esta en el diccionario, la agrega
        

    mayor = 0
    for letter, count in letras_dic.items():
        if (count >= mayor):
            mayor = count
            llave_maximo = letter

    return llave_maximo