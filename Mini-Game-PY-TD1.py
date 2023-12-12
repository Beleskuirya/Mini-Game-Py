import random



# Exemple de carte

carte_test =[[0, 0, 0, 1, 0, 3, 0, 0],

        [0, 3, 2, 0, 0, 1, 0, 0],

        [0, 1, 0, 0, 0, 0, 1, 0],

        [0, 0, 0, 1, 0, 0, 0, 0],

        [0, 1, 0, 0, 0, 0, 0, 0],

        [1, 0, 3, 0, 0, 1, 0, 0]]
#----------------------------------


dico = {0:'🌄', 1: '🌅', 3:'🗿', 2: '🌀'}

#La fonction qui permet de déplacer le personnages, et de restreindre ses déplacements en fonction des touches zqsd,avec commme paramètres l'input letter, le personnage personnage et la carte m
def update_p(letter,personnage, m) :

    

    if letter == 'z' :

        

        if personnage['y'] == 0:#si le perso sort de la map

                print('Vous ne pouvez pas sortir de la map')

        else : #sinon il monte

                personnage['y'] = personnage['y'] - 1

        if m[personnage['y']][personnage['x']] == 3 : #si le perso veut allez sur un mur

            print('Vous ne pouvez pas monter il n\'y a pas de chemin')

            personnage['y'] = personnage['y'] + 1    

                

    if letter == 's' :

        

        if personnage['y'] == len(m)-1 : #si le perso sort de la map

                print('Vous ne pouvez pas sortir de la map')

        else : #sinon il descend 

                personnage['y'] = personnage['y'] + 1

        if m[personnage['y']][personnage['x']] == 3 : #si le perso veut allez sur un mur

            print('Vous ne pouvez pas dessendre il n\'y a pas de chemin')

            personnage['y'] = personnage['y'] - 1  

            

    if letter == 'd' :

        if personnage['x']== len(m[0])-1 :

            print('Vous ne pouvez pas sortir de la map')

        else :

            personnage['x'] = personnage['x'] + 1

            

        if m[personnage['y']][personnage['x']] == 3 : #si le perso veut allez sur un mur

            print('Vous ne pouvez pas avancer il n\'y a pas de chemin')

            personnage['x'] = personnage['x'] - 1

            

    if letter == 'q' :

        if personnage['x']== 0 :

            print('Vous ne pouvez pas sortir de la map')

        else :

            personnage['x'] = personnage['x'] - 1

            

        if m[personnage['y']][personnage['x']] == 3 : #si le perso veut allez sur un mur

            print('Vous ne pouvez pas avancer il n\'y a pas de chemin')

            personnage['x'] = personnage['x'] + 1

    if letter == 'personnage'and m[personnage['y']][personnage['x']] != 2 :

        print("Vous n'êtes pas sur un portail")

    

    return personnage['x'],personnage['y']

#La fonction pour générer aléatoirement, la taille de la carte, et définir la récurrence d'apparition des plages et murs
def display_map(size_map, proportion_murs, proportion_palms):

   

    m=[]

    N_palms = 0

    N_t = 0

    N_p = 0

    for i in range(size_map[1]):

        m.append([0]*size_map[0])

    long=size_map[0]*size_map[1]

    n_v = int(proportion_murs*long)

    n_e = int(proportion_palms*long)

    n_t = int((proportion_murs-proportion_palms)*long)

    n_p = 1

    t = 0

    while t < len(m)-1 : # permet de mettre une plages par ligne si possible 

        for y in range(0,len(m)) :

            x = random.randint(1,len(m[0])-1)

            if not 1 in m[y] :

                if m[y][x] == 0 :

                    m[y][x] = 1

                    N_palms += 1

                    t+= 1

    while N_palms < N_palms : #rajoute les plages restantes

        x,y = random.randint(1,len(m[0])-1),random.randint(0,len(m)-1)

        if m[y][x] == 0 :

            m[y][x] = 1

            N_e += 1

        

    while N_t < n_t : 

        x,y = random.randint(1,len(m[0])-1),random.randint(0,len(m)-1)

        if m[y][x] == 0 :

            m[y][x] = 3

            N_t += 1

    while N_p < n_p :

        x,y = random.randint(1,len(m[0])-1),random.randint(0,len(m)-1)

        if m[y][x] == 0 :

            m[y][x] = 2

            N_p += 1

    

    return m



def clearConsole():

    #Pour sauter des lignes dans la console

    print('\n' * 20)

    
#La fonction pour créer notre bonhomme, et notamment sa position initiale quand le jeu est lancée, caractérisée par le parametre en tuple départ, qui si donné, renvoie le dico du personnage
def create_perso(depart) :

    d= {'repr' : '\U0001F9DA', 'x' : depart[0], 'y' : depart[1], 'score' : 0}

    return d



#Fonction créant les objets, à partir de la carte donnée et de many_obj le nombre d'objets, renvoie la postion sur la carte de n-objets
def create_obj(many_obj,m) :

    obj=[]

    N_obj = 0

    while N_obj < many_obj:

        x,y = random.randint(0,len(m[0])-1),random.randint(0,len(m)-1)

        if (x,y) == (0,0) :

            x,y = random.randint(0,len(m[0])-1),random.randint(0,len(m)-1)

        if m[y][x] == 0 :

            if not (x,y) in obj :

                obj.append((x,y))

                N_obj += 1

    return obj


#Crée des propriétés par rapport à l'objec
def update_objects(personnage,objs) :

    

    if (personnage['x'],personnage['y']) in objs :

        temp = objs.index((personnage['x'],personnage['y']))

        objs.pop(temp)

        personnage['score'] += 1



def display_map_and_char_and_obj(m,d,personnage,objs) :

    print("●/"," "*len(m[0]),"\●")

    for y in range (len(m)): # Les lignes

        for x in range (len(m[0])): # Les colonnes, donc toute la map est couverte

            if m[y][x] == 0 : # si à la case y,x il y a une plaine alors :

                if (y,x) == (personnage['y'],personnage['x']): # si la case y,x égale au coordonné du perso :

                    if personnage['x'] == len(m[0])-1 : #si le perso en fin de ligne saut de ligne

                        print(personnage['repr']) 

                    else :#sinon à la ligne

                        print(personnage['repr'],end="")

                elif (x,y) in objs:

                    temp = objs.index((x,y))

                    if objs[temp][0] == len(m[0])-1 : #si l'obj en fin de ligne, saut de ligne

                        print("🟡") 

                    else :#sinon à la ligne

                        print("🟡",end="")

                else :

                    print(dico[0], end="") #On affiche la ligne

                    if x == len(m[0])-1 : #si ligne écrite saut de ligne

                        print("")

                        

            if m[y][x] == 1 : # si à la case y,x il y a une plage alors :

                if (y,x) == (personnage['y'],personnage['x']): # si la case y,x égale au coordonné du perso :

                    if personnage['x'] == len(m[0])-1 : #si le perso en fin de ligne saut de ligne

                        print(personnage['repr']) 

                    else :#sinon à la ligne

                        print(personnage['repr'],end="") 

                else :

                    print(d[1], end="") #On affiche la ligne

                    if x == len(m[0])-1  : #si ligne écrite saut de ligne

                        print("")

            if m[y][x] == 3 : # si à la case y,x il y a un mur alors :

                if (y,x) == (personnage['y'],personnage['x']): # si la case y,x égale au coordonné du perso :

                    if personnage['x'] == len(m[0])-1 : #si le perso en fin de ligne saut de ligne

                        print(personnage['repr']) 

                    else :#sinon à la ligne

                        print(personnage['repr'],end="") 

                else :

                    print(d[3], end="") #On affiche la ligne

                    if x == len(m[0])-1  : #si ligne écrite saut de ligne

                        print("")

            if m[y][x] == 2 : # si à la case y,x il y a un portail alors :

                if (y,x) == (personnage['y'],personnage['x']): # si la case y,x égale au coordonné du perso :

                    if personnage['x'] == len(m[0])-1 : #si le perso en fin de ligne saut de ligne

                        print(personnage['repr']) 

                    else :#sinon à la ligne

                        print(personnage['repr'],end="") 

                else :

                    print(d[2], end="") #On affiche la ligne

                    if x == len(m[0])-1  : #si ligne écrite saut de ligne

                        print("")

            

                        

    print("●\ "," "*(len(m[0])-1),"/●")

    print("y :", personnage['y'], "x :", personnage['x'])

    print('Score : ',personnage['score'])

    print('(r), pour relancer une carte')

    lettre = input('Quel direction (z,q,s,d,personnage) ? ')

    clearConsole()

    update_p(lettre,personnage, m)

    update_objects(personnage,objs)

    return lettre





size= (8,6)

nb_pieces = 10

carte = display_map(size,0.25,0.15)

personnage = create_perso((0,0))

objs = create_obj(nb_pieces,carte)

finish = True



while finish :

    if display_map_and_char_and_obj(carte,dico,personnage,objs) == 'r':

        print("Jeu relancé")

        personnage = create_perso((0,0))

        carte = display_map(size,0.25,0.15)

        objs = create_obj(nb_pieces,carte)

    if display_map_and_char_and_obj(carte,dico,personnage,objs) == 'personnage' and carte[update_p(None,personnage, carte)[1]][update_p(None,personnage, carte)[0]] == 2 : #si le joueur presse personnage et est sur un portail

        print("Nouveau monde!")

        personnage['x'],personnage['y'] = (0,0)

        carte = display_map(size,0.25,0.15)

        objs = create_obj(nb_pieces,carte)

    if len(objs) == 0 :

        print("Partie Terminé","Score Atteint :",personnage['score'])

        Question = str(input("Voulez Vous Relancer ? (y/n) : "))

        if Question == "y" :

            personnage = create_perso((0,0))

            objs = create_obj(nb_pieces,carte)

            print("New game")

        if Question == "n" :

            finish = False

