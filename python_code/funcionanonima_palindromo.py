def run():
    palabra=input('Ingrese una palabra: ')
    pal = lambda palabra : palabra==palabra[::-1]
    if pal(palabra)==True:
        print("Es Palíndromo")
    else:
        print("No es palíndromo")
if __name__=='__main__':
    run()