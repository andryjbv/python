def run():
    import random
    import os
    
    os.system("cls")
    def alleatory():
        return random.choice(words)
    
    def normalize(s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.lower(), b.lower())
        return s

    words=[]
    with open("./data.txt","r",encoding="utf-8") as f:
        for line in f:
            words.append(line)
    challenge=alleatory()
    print(challenge)  
    challenge=normalize(challenge)

  
    n=len(challenge)
   
    print(challenge)      
    hidden=[]
    chal=[]
    z=0
    picture=[("       \n       \n       \n       \n       \n       \n       \n  ________   "),("       \n      | \n      |       \n      |       \n      |       \n      |       \n      |       \n  ____|___   "),("      _______    \n      |/       \n      |       \n      |       \n      |       \n      |       \n      |           \n  ____|___       "),("      _______    \n      |/     |   \n      |     (_)  \n      |       \n      |       \n      |       \n      |           \n  ____|___       "),("      _______    \n      |/     |   \n      |     (_)  \n      |      |   \n      |      |   \n      |           \n      |           \n  ____|___       "),("      _______    \n      |/     |   \n      |     (_)  \n      |      | \n      |      |   \n      |     / \  \n      |           \n  ____|___       "),("      _______    \n      |/     |   \n      |     (x)  \n      |     \|/  \n      |      |   \n      |     / \  \n      |           \n  ____|___       ")]
    for i in range (0,n-1):
        hidden.append("_")
    
    for k in range (0,n-1):
        chal.append(challenge[k])

 
    while hidden!=chal or z!=2:
        found=False
        print("Adivina la palabra o serás eliminado: ")
        print(" " .join(hidden))
        print("")
        print(picture[z])
        a=str(input("Ingresa una letra: "))
        for j in range (0,n):
            if a==challenge[j]:
                hidden[j]=a
                found=True
        if found==False:
            z=z+1   
        os.system("cls")
    if z!=6:
        print("Felicidades! Te has salvado!")
    if z==4:    
        print("Perdiste miserablemente perro.")

if __name__=='__main__':
    run()