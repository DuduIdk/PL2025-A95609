def somador(texto):
    soma = 0
    on = True
    
    palavras = texto.split()
    
    for palavra in palavras:
        if palavra.lower() == "off":
            on = False
        elif palavra.lower() == "on":
            on = True
        elif palavra == "=":
            print(soma)
        elif palavra.isdigit() and on:
            soma += int(palavra)

texto_exemplo = "abcd oFF 52 4 ON 25 45 = 2 OFf = on & & $ | ? 8 = off 8145678193265248 # @ 223 ="  

somador(texto_exemplo)  