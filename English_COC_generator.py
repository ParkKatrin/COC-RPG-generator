import random
import pandas as pd


# Data Base
dict_mania = {'Ablutomania': 'compulsion to wash oneself',
'Abulomania': 'pathological indecision',
'Achluomania': 'excessive fondness for darkness',
'Acromania': 'compulsion for high places',
'Agatomania': 'pathological kindness',
'Agromania': 'intense desire for open spaces',
'Aichmomania': 'obsession with sharp or pointed objects',
'Ailuromania': 'abnormal fondness for cats',
'Algomania': 'obsession with pain',
'Alliomania': 'obsession with garlic',
'Amaxomania': 'obsession with being in vehicles',
'Amenomania': 'irrational joy',
'Anthomania': 'obsession with flowers',
'Arithmomania': 'obsessive concern with numbers',
'Asoticamania': 'impulsive or reckless spending',
'Automania': 'excessive fondness for solitude',
'Balletomania': 'abnormal love for ballet',
'Bibliokleptomania': 'compulsion to steal books',
'Bibliomania': 'obsession with books and/or reading',
'Bruxomania': 'compulsion to grind teeth',
'Cacodemomania': 'belief that someone is inhabited by an evil spirit',
'Callomania': 'obsession with one's own beauty',
'Cartacoethes': 'uncontrollable compulsion to always look at maps',
'Catapedamania': 'obsession with jumping from high places',
'Cheimatomania': 'abnormal desire for cold and/or cold things',
'Coreomania': 'mania for dancing to the point of fainting',
'Clinomania': 'excessive desire to stay in bed',
'Coimetromania': 'obsession with cemeteries',
'Coloromania': 'obsession with a specific color',
'Coulromania': 'obsession with clowns',
'Countermania': 'compulsion to experience fear-inducing situations',
'Dacnomania': 'obsession with killing',
'Demonomania': 'belief that someone is possessed by demons',
'Dermatillomania': 'compulsion to pick at one's own skin',
'Dikemania': 'obsession with seeing justice',
'Dipsomania': 'abnormal desire for alcohol',
'Doramania': 'obsession with owning furs',
'Doromania': 'obsession with giving gifts',
'Drapetomania': 'compulsion to flee',
'Ecdemiomania': 'compulsion to wander',
'Egomania': 'irrational egocentric attitude or self-worship',
'Empleomania': 'insatiable desire to occupy the office',
'Enosimania': 'pathological belief that someone has sinned',
'Epistemomania': 'obsession with acquiring knowledge',
'Eremiomania': 'compulsion for silence',
'Etheromania': 'desire for ether',
'Gamomania': 'obsession with declaring strange marriages',
'Geliomania': 'uncontrollable compulsion to laugh',
'Goetomania': 'obsession with witches and witchcraft',
'Graphomania': 'obsession with writing everything',
'Gymnomania': 'compulsion for nudity',
'Habromania': 'abnormal tendency to create pleasant illusions (despite reality)',
'Helminthomania': 'excessive fondness for worms',
'Hoplomania': 'obsession with firearms',
'Hydromania': 'irrational desire for water',
'Ichthyomania': 'obsession with fish',
'Iconomania': 'obsession with icons or portraits',
'Idolomania': 'obsession or devotion to an idol',
'Infomania': 'excessive devotion to accumulating facts/information',
'Klazomania': 'irrational compulsion to shout',
'Kleptomania': 'irrational compulsion to steal',
'Ligyromania': 'uncontrollable compulsion to make loud or strident noises',
'Linonomania': 'obsession with strings',
'Lotterymania': 'extreme desire to participate in lotteries',
'Lypemania': 'abnormal tendency toward deep melancholy',
'Megalithomania': 'abnormal tendency to compose bizarre ideas when in the presence of stone circles/standing stones',
'Melomania': 'obsession with music or a specific melody',
'Metromania': 'insatiable desire to write verses',
'Misomania': 'hatred of everything, obsession with hating a subject or group',
'Monomania': 'abnormal obsession with a single thought or idea',
'Mythomania': 'abnormal lying or exaggeration',
'Nosomania': 'illusion of suffering from an imaginary illness',
'Notomania': 'compulsion to record everything (e.g., photography)',
'Onomamania': 'obsession with names (people, places, things)',
'Onomatomania': 'irresistible urge to repeat certain words',
'Onychotillomania': 'compulsive nail-biting',
'Opsomania': 'abnormal love for a specific type of food',
'Paramania': 'abnormal pleasure in complaining',
'Personamania': 'obsession with wearing masks',
'Phasmomania': 'obsession with ghosts',
'Phonomania': 'pathological tendency toward murder',
'Photomania': 'pathological desire for light',
'Planomania': 'abnormal desire to disobey social norms',
'Plutomania': 'obsessive desire for wealth',
'Pseudomania': 'irrational compulsion to lie',
'Pyromania': 'compulsion to start fires',
'Question-Asking Mania': 'compulsive desire to ask questions',
'Rhinotillexomania': 'compulsive desire to pick the nose',
'Scribbleomania': 'obsession with scribbles/doodles',
'Siderodromomania': 'intense fascination with trains and railway travel',
'Sophomania': 'illusion that someone is incredibly intelligent',
'Technomania': 'obsession with new technologies',
'Thanatomania': 'belief that someone is cursed by the magic of death',
'Theomania': 'belief that he or she is a god',
'Titillomaniac': 'compulsion to scratch oneself',
'Tomomania': 'irrational predilection for performing surgeries',
'Trichotillomania': 'desire to pull one's own hair',
'Typhlomania': 'pathological blindness',
'Xenomania': 'obsession with foreign things',
'Zoomania': 'insane affection for animals.'}

dict_fobia = {
'Ablutophobia': 'Fear of washing or bathing.',
'Acrophobia': 'Fear of heights.',
'Aerophobia': 'Fear of flying.',
'Agoraphobia': 'Fear of open and public (crowded) places.',
'Alektorophobia': 'Fear of chickens.',
'Alliumphobia': 'Fear of garlic.',
'Amaxophobia': 'Fear of being or traveling in vehicles.',
'Ancraophobia': 'Fear of wind.',
'Androphobia': 'Fear of men.',
'Anglophobia': 'Fear of England or English culture, etc.',
'Anthrophobia': 'Fear of flowers.',
'Apotemnophobia': 'Fear of people with amputations.',
'Arachnophobia': 'Fear of spiders.',
'Astraphobia': 'Fear of lightning.',
'Atephobia': 'Fear of ruin or ruins.',
'Aulophobia': 'Fear of flutes.',
'Bacteriophobia': 'Fear of bacteria.',
'Ballistophobia': 'Fear of missiles or bullets.',
'Basophobia': 'Fear of falling.',
'Bibliophobia': 'Fear of books.',
'Botanophobia': 'Fear of plants.',
'Caligynephobia': 'Fear of beautiful women.',
'Cheimaphobia': 'Fear of cold.',
'Chronomentrophobia': 'Fear of clocks.',
'Claustrophobia': 'Fear of confined spaces.',
'Coulrophobia': 'Fear of clowns.',
'Cynophobia': 'Fear of dogs.',
'Demonophobia': 'Fear of spirits or demons.',
'Demophobia': 'Fear of crowds.',
'Dentophobia': 'Fear of dentists.',
'Disposophobia': 'Fear of throwing things away (hoarding).',
'Doraphobia': 'Fear of fur.',
'Dromophobia': 'Fear of crossing streets.',
'Ecclesiophobia': 'Fear of the church.',
'Eisoptrophobia': 'Fear of mirrors.',
'Enetophobia': 'Fear of needles or pins.',
'Entomophobia': 'Fear of insects.',
'Felinophobia': 'Fear of cats.',
'Gephyrophobia': 'Fear of crossing bridges.',
'Gerontophobia': 'Fear of old people or aging.',
'Gynophobia': 'Fear of women.',
'Haemaphobia': 'Fear of blood.',
'Hamartophobia': 'Fear of sinning.',
'Haphophobia': 'Fear of touch.',
'Herpetophobia': 'Fear of reptiles.',
'Homichlophobia': 'Fear of fog.',
'Hoplophobia': 'Fear of firearms.',
'Hydrophobia': 'Fear of water.',
'Hypnophobia': 'Fear of sleep or being hypnotized.',
'Iatrophobia': 'Fear of doctors.',
'Ichthyophobia': 'Fear of fish.',
'Katsaridaphobia': 'Fear of cockroaches.',
'Keraunophobia': 'Fear of thunder.',
'Lachanophobia': 'Fear of vegetables.',
'Ligyrophobia': 'Fear of loud noises.',
'Limnophobia': 'Fear of lakes.',
'Mechanophobia': 'Fear of machines or machinery.',
'Megalophobia': 'Fear of big things.',
'Merinthophobia': 'Fear of being tied up or bound.',
'Meteorophobia': 'Fear of meteors or meteorites.',
'Monophobia': 'Fear of being alone.',
'Mysophobia': 'Fear of dirt or contamination.',
'Myxophobia': 'Fear of slime.',
'Necrophobia': 'Fear of dead things.',
'Octophobia': 'Fear of the figure 8.',
'Odontophobia': 'Fear of teeth.',
'Oneirophobia': 'Fear of dreams.',
'Onomatophobia': 'Fear of hearing a particular word or words.',
'Ophidiophobia': 'Fear of snakes.',
'Ornithophobia': 'Fear of birds.',
'Parasitophobia': 'Fear of parasites.',
'Pediophobia': 'Fear of dolls.',
'Phagophobia': 'Fear of swallowing, eating, or being eaten.',
'Pharmacophobia': 'Fear of drugs.',
'Phasmophobia': 'Fear of ghosts.',
'Phenogophobia': 'Fear of daylight.',
'Pogonophobia': 'Fear of beards.',
'Potamophobia': 'Fear of rivers.',
'Potophobia': 'Fear of alcohol or alcoholic drinks.',
'Pyrophobia': 'Fear of fire.',
'Rhabdophobia': 'Fear of magic.',
'Scotophobia': 'Fear of darkness or night.',
'Selenophobia': 'Fear of the moon.',
'Siderodromophobia': 'Fear of traveling by train.',
'Siderophobia': 'Fear of stars.',
'Stenophobia': 'Fear of narrow things or places.',
'Symmetrophobia': 'Fear of symmetry.',
'Taphephobia': 'Fear of being buried alive or of cemeteries.',
'Taurophobia': 'Fear of bulls.',
'Telephonophobia': 'Fear of telephones.',
'Teratophobia': 'Fear of monsters.',
'Thalassophobia': 'Fear of the sea.',
'Tomophobia': 'Fear of surgical operations.',
'Triskadekaphobia': 'Fear of the number 13.',
'Vestiphobia': 'Fear of clothes.',
'Wiccaphobia': 'Fear of witches and witchcraft.',
'Xanthophobia': 'Fear of the color yellow or the word "yellow".',
'Xenoglossophobia': 'Fear of foreign languages.',
'Xenophobia': 'Fear of strangers or foreigners.',
'Zoophobia': 'Fear of animals.'}


# They always have a melee weapon (mellee)
# there may or may not be a firearm (adicionar x nadas)


weapons = {'melee': {
    'Small Knife': ['1D4+STR', 'Touch'],
    'Medium Knife': ['1D4+2+STR', 'Touch'],
    'Baseball Bat': ['1D8+STR', 'Touch'],
    'Bat': ['1D6+STR', 'Touch']  # Nightstick in the manual, it's similar
    },
    'firearms': {
        'Nothing0': ['0D0', '0m', '0', '100'],
        'AK-47 or AKM': ['2D6+1', '90m', '30', '100'],
        'Glock 17 9mm Auto': ['1D10', '14m', '17', '98'],
        'Nothing1': ['0D0', '0m', '0', '1'],
        'Galil Assault Rifle': ['2D6', '101m', '20', '98'],
        'Nothing2': ['0D0', '0m', '0', '1'],
        '.357 Magnum Revolver': ['1D8+1D4', '14m', '6', '100'],
        '.22 Bolt-Action Rifle': ['1D6+1', '28m', '6', '99'],
        '12-gauge Shotgun (2B)': ['1D6; 2D6; 4D6', '10m; 18m; 48m', '2', '100'],
        'Nothing3': ['0D0', '0m', '0', '1'],
        '.22 Short Automatic': ['1D6', '9m', '6', '100'],
        'Nothing4': ['0D0', '0m', '0', '1'],
        '.32 or 7.65mm Revolver': ['1D8', '14m', '6', '100']
    }
}


dicti_name = {'Man': 
['GEORGE CARVALHO',
'MANUEL RAMOS',
'BERNARDO AGUIAR',
'ADAM GORDON',
'VALTER BOTELHO',
'JOÃO SILVA',
'FRANCISCO DIAS',
'PERRY STANLEY',
'ALVIN MENDES',
'HENRIQUE CLIFFORD',
'BILLY GUERRA',
'XAVIER CORREIA',
'ALFREDO MIGUEL',
'ELDER CORTE-REAL',
'SIMÃO FREITAS',
'LOURENÇO SALGADO',
'CHAD TERRY',
'DANIEL VIDAL',
'DAVID MAURICIO',
'KEVIN SAPATINHO',
'CARLITOS BARBOSA',
'NICOLAU MORAIS',
'ALBERTO GARCIA',
'JOEL RESENDES',
'LUCAS PIRES',
'JAY BATISTA',
'VICENTE NEVES',
'ANDRÉ VIEIRA',
'MARCELO BRAGA',
'JIMMY LAKE',
'EMILIO CARNEIRO',
'MARTIM LAPA',
'MATIAS JESUS ',
'JUSTINO JERRY',
'TELMO FIGUEIRA',
'GUILHERME OLIVEIRA',
'EDGAR VAZ',
'TOMÁS LUZ',
'TIAGO MOREIRA',
'RODRIGO VIZELA',
'RENATO CAETANO',
'MATEUS RAMOS',
'ANGELO GOUVEIA',
'DIONISIO ALCANTRA',
'ARMANDO SILVESTRE',
'TEOFILO COSTA',
'ELIAS VENÂNCIO',
'RAUL ALBUQUERQUE',
'PEDRO QUEIROZ'],
'Woman':
['DOLORES LEITE',
'AURORA SOUSA',
'ALICE MORENO',
'RAFAELA LIMA',
'ARIANA NUNES',
'TERESA DIXON',
'SARA RESENDES',
'JOANA BETTENCOURT',
'REGINA BARRETO',
'FLORINDA GONÇALVES',
'TELMA COIMBRA',
'ÚRSULA NOGUEIRA',
'VICTORIA SOARES',
'LETICIA NASCIMENTO',
'KATIE SARAIVA',
'AMANDA VENTURA',
'LARA ROSÁRIO',
'AUGUSTA CERQUEIRA',
'MAGDA PIRES',
'LILIANA ANTUNES',
'JULIA PIMENTINHA',
'JESSICA SANTOS',
'ESTER GOUVEIA',
'MARGARIDA METEUS',
'LUCIA CARRIÇO',
'PAULA CARVALHO',
'IRIS MENEZES',
'KIM POSSIBEL',
'IRINA PUMBA',
'PALOMA REGO',
'ALÍCIA FREITAS',
'CÍNTIA AGOSTINHO',
'PAMELA SOUSA',
'DULCE BOTELHO',
'ANGÉLICA GOMES',
'CLOÉ GONÇALVES',
'MARIA ABREU',
'JOSEFA PINHO',
'SAMANTA CUNHA',
'FERNANDAS VARELA',
'REGINA SEIXAS',
'VITÓRIA ROSA',
'CATARINA PINHO',
'MAFALDA LUZ',
'ROSA TEIXEIRA',
'MADALENA CORTE-REAL',
'ANITA MOREIRA',
'TATIANA MATOS',
'CÉLIA RODRIGUES']}

#https://thestoryshack.com/pt/geradores/gerador-de-nomes-portugueses/?v=1

arquivo = "npcs.csv"
SEPARADOR = ","

def create_open_file(name, status, weapon_melee, caracteristicas_arma_branca, skill_knife, weapon_firearms,caracteristicas_arma_fogo,skill_gun):
    #SEPARADOR = SEPARADOR
    #arquivo = "npcs.csv"
    try:       
        pd.read_csv(arquivo) # Checker, ve se existe ficheiro      
        # Formatação dos dados em colunas
        row_data = [name, status['AGE'], status['HP'], status['SAN'], status['STR'], status['CON'], status['SIZ'],
            status['DEX'], status['APP'], status['EDU'], status['INT'], status['POW'], status['MOV'],status['DB'],
            weapon_melee, skill_knife, caracteristicas_arma_branca[0], caracteristicas_arma_branca[1], weapon_firearms, 
            skill_gun, caracteristicas_arma_fogo[0], caracteristicas_arma_fogo[1], caracteristicas_arma_fogo[2], 
            caracteristicas_arma_fogo[3]]

        # Escreve os dados no arquivo CSV
        with open(arquivo, 'a+', encoding='utf-8') as fh:
            fh.write(",".join(map(str, row_data)) + "\n")
            print('g')  

        # Exibe os NPCs presentes no arquivo CSV
        npcs = pd.read_csv(arquivo, sep=SEPARADOR, on_bad_lines='skip')
        print("\nFicheiro de NPCs encontrado, estes são os NPCs:")
        print(npcs)
            
        choice = input('Do you wish to continue?\n\t1 : Create a random NPC\n\t2 : Return to home menu\n\t3 : Exit\n')
        if int(choice) == 1:
                npc_criation(0)
        elif int(choice) == 2:
                choices()
        else:
            exit
    except FileNotFoundError:
        print("Ficheiro nao encontrado, a criar um de raiz...")
        with open(arquivo, 'w', encoding='utf-8') as fh:
            fh.write("name,AGE,HP,SAN,STR,CON,SIZ,DEX,APP,EDU,INT,POW,MOV,DB,Arma melee,Habilidade Arma melee,Dano,Distancia,Arma firearms,Habilidade Arma firearms,Dano,Distancia,N_Balas,Defeito\n")

        row_data = [name, status['AGE'], status['HP'], status['SAN'], status['STR'], status['CON'], status['SIZ'],
            status['DEX'], status['APP'], status['EDU'], status['INT'], status['POW'], status['MOV'],status['DB'],
            weapon_melee, skill_knife, caracteristicas_arma_branca[0], caracteristicas_arma_branca[1], weapon_firearms, skill_gun, caracteristicas_arma_fogo[0], caracteristicas_arma_fogo[1],
            caracteristicas_arma_fogo[2], caracteristicas_arma_fogo[3]]
        print('j') 
        # Escreve os dados no arquivo CSV
        with open(arquivo, 'a+', encoding='utf-8') as fh:
            fh.write(",".join(map(str, row_data)) + "\n")

        # Exibe os NPCs presentes no arquivo CSV
        npcs = pd.read_csv(arquivo, sep=SEPARADOR, on_bad_lines='skip')
        print("\nFicheiro de NPCs encontrado, estes são os NPCs:")
        print(npcs)
            
        choice = input('Do you wish to continue?\n\t1 : Create a random NPC\n\t2 : Return to home menu\n\t3 : Exit\n')
        if int(choice) == 1:
                npc_criation(0)
        elif int(choice) == 2:
                choices()
        else:
            exit

def visualize_file():
    try:
        # Carrega os dados do arquivo CSV em um DataFrame
        df = pd.read_csv(arquivo, sep=SEPARADOR)

        # Exibe o DataFrame completo sem truncar as linhas
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(df)

        choice = input('Do you wish to continue?\n\t1 : Return to home menu\n\t2 : Exit\n')
        if int(choice) == 1:
            choices()
        else:
            exit
            
    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não foi encontrado.")
        choices()

def lancar_dados(n_dice, lados, show=False):
    soma = 0 
    for i in range(n_dice):
        resultado = random.randint(1, lados)
        if show == True:
            print(f"Lançamento {i+1} - Resultado : {resultado}")
        soma += resultado
    
    if show == True:
        print('Valor dos dados:', soma)
        choice = input('Do you wish to continue?\n\t1 : Lançar novamente os dados\n\t2 : Return to home menu\n\t3 : Exit\n')
        if int(choice) == 1:
            show = True
            n_dice = int(input("How many dice do you want to roll? "))
            n_sides = int(input("How many sides? "))
            lancar_dados(n_dice, n_sides, show)
        elif int(choice) == 2:
            choices()
        else:
            exit
    
    return soma

def phobias_choose():
    phobia = random.choice(list(dict_fobia.keys()))
    print(phobia, '-->', dict_fobia[phobia])
    choice = input('Do you wish to continue?\n\t1 : Fazer nova phobia\n\t2 : Return to home menu\n\t3 : Exit\n')
    if int(choice) == 1:
        phobias_choose()
    elif int(choice) == 2:
        choices()
    else:
        exit

def mania_choose():
    mania = random.choice(list(dict_mania.keys()))
    print(mania, '-->', dict_mania[mania])
    choice = input('Do you wish to continue?\n\t1 : Fazer nova mania\n\t2 : Return to home menu\n\t3 : Exit\n')
    if int(choice) == 1:
        mania_choose()
    elif int(choice) == 2:
        choices()
    else:
        exit

def gerar_stats(number):
    if number == 0:
        STR = int(lancar_dados(3,6) * 5) # Força
        CON = int(lancar_dados(3,6) * 5) # Constituição
        SIZ = int((lancar_dados(2,6) + 6) * 5) # Tamanho
        DEX = int(lancar_dados(3,6) * 5) # Destreza
        APP = int(lancar_dados(3,6) * 5) # Aparência
        EDU = int((lancar_dados(2,6) + 6) * 5) # Educação 
        INT = int((lancar_dados(2,6) + 6) * 5) # Inteligência
        POW = int(lancar_dados(3,6) * 5) # Poder
        HP  = int(((CON + SIZ)/10)+lancar_dados(1,4))
        SAN = POW

        if STR + SIZ >= 2 and STR + SIZ  <= 64:
            DB = '-2'
        elif STR + SIZ >= 65 and STR + SIZ  <= 84:
            DB = '-1'
        elif STR + SIZ >= 85 and STR + SIZ  <= 124:
            DB = '0'
        elif STR + SIZ >= 125 and STR + SIZ  <= 164:
            DB = '+1D4'
        elif STR + SIZ >= 165 and STR + SIZ  <= 204:
            DB = '+1D6'
        elif STR + SIZ >= 205 and STR + SIZ  <= 284:
            DB = '+2D6'
        else:
            DB = 'Not Human'

        if DEX < SIZ and STR < SIZ:
            MOV = 7
        elif  DEX >= SIZ or STR >= SIZ:
            MOV = 8
        else:
            MOV = 9

        AGE = random.randint(25,50)

        stats = {
            "AGE"   : AGE,
            "HP"    : HP,
            "SAN"   : SAN,
            "STR"   : STR,
            "CON"   : CON,
            "SIZ"   : SIZ,
            "DEX"   : DEX,
            "APP"   : APP,
            "EDU"   : EDU,
            "INT"   : INT,
            "POW"   : POW,
            "MOV"   : MOV,
            "DB"        :DB
        }
    else:
        STR = int(input('Força/STR:\n')) 
        CON = int(input('Constituição/CON:\n'))
        SIZ = int(input('Tamanho/SIZ:\n') )
        DEX = int(input('Destreza/DEX:\n')) 
        APP = int(input('Aparencia/APP:\n')) 
        EDU = int(input('Educação/EDU:\n'))  
        INT = int(input('Inteligencia/INT:\n')) 
        POW = int(input('Poder/POW:\n'))
        HP  = int(input('Vida/HP:\n'))
        SAN = POW

        if STR + SIZ >= 2 and STR + SIZ  <= 64:
            DB = '-2'
        elif STR + SIZ >= 65 and STR + SIZ  <= 84:
            DB = '-1'
        elif STR + SIZ >= 85 and STR + SIZ  <= 124:
            DB = '0'
        elif STR + SIZ >= 125 and STR + SIZ  <= 164:
            DB = '+1D4'
        elif STR + SIZ >= 165 and STR + SIZ  <= 204:
            DB = '+1D6'
        elif STR + SIZ >= 205 and STR + SIZ  <= 284:
            DB = '+2D6'
        else:
            DB = 'Not Human'

        if DEX < SIZ and STR < SIZ:
            MOV = 7
        elif  DEX >= SIZ or STR >= SIZ:
            MOV = 8
        else:
            MOV = 9

        AGE = int(input('Age/AGE:\n'))

        stats = {
            "AGE"   : AGE,
            "HP"    : HP,
            "SAN"   : SAN,
            "STR"   : STR,
            "CON"   : CON,
            "SIZ"   : SIZ,
            "DEX"   : DEX,
            "APP"   : APP,
            "EDU"   : EDU,
            "INT"   : INT,
            "POW"   : POW,
            "MOV"   : MOV,
            "DB"    : DB
        }
    return stats

def npc_criation(number):
    if number == 0:
        try:    
            weapon_melee = random.choice(list(guns['melee'].keys()))            
            weapon_firearms = random.choice(list(guns['firearms'].keys()))
            gender = input('\t1 : Man\n\t2 : Woman\n\t3 : Exit\n')
            if int(gender) == 1:
                name = random.choice(dicti_names['Man'])
            elif int(gender) == 2:
                name = random.choice(dicti_names['Woman'])
            else:
                choices()
            
            stats = gerar_stats(0)
            skill_gun, skill_knife = values_skill()
            create_open_file(name, stats, weapon_melee, guns['melee'][weapon_melee],skill_knife,weapon_firearms, guns['firearms'][weapon_firearms],skill_gun)
            
        except:
            print('The value entered does not exist. Try again.')
            npc_criation(0)
    elif number == 1:
        weapon_melee = random.choice(list(guns['melee'].keys()))
        weapon_firearms = random.choice(list(guns['firearms'].keys()))
        name = str(input('name:\n'))
        stats = gerar_stats(1)
        skill_gun, skill_knife = values_skill()
        create_open_file(name, stats, weapon_melee, guns['melee'][weapon_melee],skill_knife,weapon_firearms, guns['firearms'][weapon_firearms],skill_gun)
        
def values_skill():
    firearms_gun = random.randint(25,66)
    
    melee_weapon = random.randint(25,66)

    return firearms_gun, melee_weapon

def choices():
    try:
        escolha = int(input('What do you want to do?\n\t1 : Choose a phobia.\n\t2 : Choose a mania.\n\t3 : Create a random NPC.\n\t4 : Roll the dices\n\t5 : Dice number division\n\t6 : Add a NPC manualy\n\t7 : Open que CSV file with all NPC's\n\t8 : Exit\n'))
        if escolha == 1 :
            phobias_choose()
        elif escolha == 2 :
            mania_choose()
        elif escolha == 3 :
            npc_criation(0)
        elif escolha == 4 :
            show = True
            n_dice = int(input("How many dice do you want to roll? "))
            n_sides = int(input("How many sides? "))
            lancar_dados(n_dice, n_sides, show)
        elif escolha == 5 :
            division()
        elif escolha == 6 :
            npc_criation(1)
        elif escolha == 7 :
            visualize_file()
        elif escolha == 8 :
            exit
        else:
            print('Erro')
            choices()
    except Exception as e:
        print('The value entered does not exist. Try again.', e)
        choices()

def division():
    number = int(input('Colocar numero:\n'))
    print('1\t:\t',number,'\n1/2\t:\t' , int(number/2), '\n1/5\t:\t', int(number/5))
    choice = input('Do you wish to continue?\n\t1 : Make new division\n\t2 : Return to home menu\n\t3 : Exit\n')
    if int(choice) == 1:
        division()
    elif int(choice) == 2:
        choices()
    else:
        exit


if __name__ == '__main__':
    choices()
