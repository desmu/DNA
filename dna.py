import csv
from sys import argv, exit

arr = []#on initialise le tableau qui va stocker le nombre concécutif maximal de chaque nucléotide pour la séquence argv[2] entrée

db = open(argv[1],"r")
data = list(csv.reader(db))#ouverture de la base de donnée et stockage dans un tableau à 2 dimensions découpé au niveau des virgules par reader()
x = data[0]#première ligne correspondante aux séquences

s = open(argv[2],"r")
seq = s.read()#ouverture et stockage de la base de donnée de la base de donnée lecture

for i in range(1,len(x)):#on passe une fois dans la boucle pour chaque groupe de nucléotide
    nbm = 0#nombre d'itération consécutive maximale d'une séquence type dans la séquence analysée
    nb = 0#nombre d'itération consécutive d'une séquence type dans la séquence analysée
    a = 0#indice de la position de la boucle dans l'analyse de la grande séquence
    prec = 0#indice de la séquence précédente
    while a < len(seq):#on scanne toute la séquence à la recherche du nombre maximal consécutif de la séquence type "i" que l'on est entrain de chercher
        a = seq.find(x[i], a)#on retourne la position de l'itération suivante de la séquence type "i" recherchée
        if a == -1: #retourne -1 si non trouvé/si aucune itération de la séquence cherchée à partir de "a" n'est trouvée
            nb = 0#réinitialisation
            break#fin de l'analyse pour la séquence "i"
        else:#itération trouvée aprés "a"
            if prec == 0:#si c'est la première itération de la séquence "i" trouvée dans la chaîne analysée
                nb += 1#on ajoute 1 au nombre d'itérations consécutives
                prec = a#on sauvegarde la position de cette trouvaille dans "prec"
                nbm = nb#nb d'itération est assigné au max à retourner dans le tableau arr
            elif ((a - len(x[i])) == prec):#si la séquence type trouvée est consécutive à la précédente
                nb += 1#on ajoute 1 au nombre d'itérations consécutives
                prec = a#on sauvegarde la position de cette trouvaille dans "prec"
                if nbm < nb:#si la chaîne de séquence type consécutives en cours de dénombrement se trouve être plus longue que la suite précédente
                    nbm = nb#nb d'itération est assigné au max à retourner dans le tableau arr
            elif ((a - len(x[i])) != prec):#si la séquence type trouvée n'est pas consécutive à la précédente
                nb = 1#nb repasse à une seule séquence trouvée
                prec = a#nb d'itération est assigné au max à retourner dans le tableau arr
                #prec étant != 0 ce n'est pas la première occurence de la séquence type recherchée "nbm" est donc forcément >= nb
                #donc pas d'assignation au max à retourner
        a += 1
    arr.append(nbm)#on inserre le nombre de la plus longue chaîne consécutive de la séquence analysée
arr = list(map(str, arr))#change le tableau de valeurs int en string pour que celui-ci puisse être comparé aux montants inscrits dans la base de donnée pour chaque personne
#make a new list to preserve reader
data.pop(0)#on retire la ligne correspondant aux séquences types de nucléotides
for i in data:#pour chaque ligne de la base de données
    if i[1:] == arr:#si toute la ligne de valeurs max vaut celle de "arr"
        print("C'est : ",i[0])#c'est lui
    else:
        print("Ce n'est pas : ",i[0])#sinon : ce n'est pas lui
