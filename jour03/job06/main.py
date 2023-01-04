chaine = "abcdefghijklmnopqrstuvwxyz" 
chaine_de_caractere = chaine * 10 
nb = 0 

while len(chaine_de_caractere) != 0:

    print(chaine_de_caractere[:nb]) 
    chaine_de_caractere = chaine_de_caractere[nb:] 
    
    nb = nb + 1