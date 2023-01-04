chaine = "nikana"
nombre_de_carac = len(chaine)
nom_a_lenvers = ""

i = 1
while i <= nombre_de_carac:
    lettre = ""
    lettre = chaine[-i]
    nom_a_lenvers = nom_a_lenvers + lettre
    i = i + 1

print(nom_a_lenvers)