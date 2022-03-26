def palindromo(palabra):
    palabra=palabra.lower().replace(' ','')
    palabrainversa=palabra[::-1]
    if palabrainversa==palabra:
        return True
    else:
        return False
   


def run():
    palabra=input("Ingrese una palabra: ")
    if palindromo(palabra)==True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')
if __name__=='__main__':
    run()