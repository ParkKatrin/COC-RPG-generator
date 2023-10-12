import random
import pandas as pd


# BASES DE DADOS
dict_mania = {'Ablutomania':'compulsão por se lavar',
'Abulomania':'indecisão patológica.',
'Achluomania':'gosto excessivo pela escuridão.',
'Acromania ':'compulsão por lugares altos.',
'Agatomania':'bondade patológica.',
'Agromania':'desejo intenso de estar em espaços abertos.',
'Aichmomania':'obsessão por objetos pontiagudos ou pontiagudos.',
'Ailuromania':'gosto anormal por gatos.',
'Algomania':'obsessão pela dor.',
'Alliomania':'obsessão por alho.',
'Amaxomania':'obsessão por estar em veículos.',
'Amenomania':'alegria irracional.',
'Anthomania':'obsessão por flores.',
'Arithmomania':'preocupação obsessiva com números.',
'Asoticamania':'gastos impulsivos ou imprudentes.',
'Automania':'um gosto excessivo pela solidão.',
'Balletomania':'gosto anormal pelo balé.',
'Bibliokleptomania':'compulsão por roubar livros.',
'Bibliomania':'obsessão por livros e/ou leitura.',
'Bruxomania':'compulsão por ranger os dentes.',
'Cacodemomania':'crença de que alguém é habitado por um espírito maligno.',
'Callomania':'obsessão com a própria beleza.',
'Cartacoethes':'compulsão incontrolável de estar sempre a ver mapas.',
'Catapedamania':'Obsessão por pular de lugares altos.',
'Cheimatomania':'desejo anormal de coisas frias e/ou frias.',
'Coreomania':'mania de dançar até desmaiar.',
'Clinomania':'Desejo excessivo de ficar na cama.',
'Coimetromania':'obsessão por cemitérios.',
'Coloromania':'obsessão por uma cor específica.',
'Coulromania':'obsessão por palhaços.',
'Countermania':'compulsão para experimentar situações de medo.',
'Dacnomania':'obsessão por matar.',
'Demonomania':'crença de que alguém está possuído por demônios.',
'Dermatillomania':'compulsão por beliscar a própria pele.',
'Dikemania':'obsessão de ver a justiça.',
'Dipsomania':'desejo anormal de álcool.',
'Doramania':'obsessão por possuir peles.',
'Doromania':'obsessão por dar presentes.',
'Drapetomania':'compulsão por fugir.',
'Ecdemiomania':'compulsão por vagiar.',
'Egomania':'atitude egocêntrica irracional ou auto-adoração.',
'Empleomania':'Vontade insasiavel de ocupar o escritorio.',
'Enosimania':'crença patológica de que alguém pecou.',
'Epistemomania':'obsessão por adquirir conhecimento.',
'Eremiomania':'compulsão pelo silencio.',
'Etheromania':'desejo de éter.',
'Gamomania':'obsessão em declarar casamentos estranhos.',
'Geliomania':'compulsão incontrolável de rir.',
'Goetomania':'obsessão por bruxas e feitiçaria.',
'Graphomania':'obsessão em escrever tudo.',
'Gymnomania':'compulsão pela nudez.',
'Habromania':'tendência anormal de criar ilusões agradáveis (apesar da realidade).',
'Helminthomania':'um gosto excessivo por minhocas.',
'Hoplomania':'obsessão por armas de fogo.',
'Hydromania':'desejo irracional de água.',
'Ichthyomania':'obsessão por peixes.',
'Iconomania':'obsessão por ícones ou retratos.',
'Idolomania':'obsessão ou devoção a um ídolo.',
'Infomania':'devoção excessiva a acumular factos/informação.',
'Klazomania':'compulsão irracional de gritar.',
'Kleptomania':'compulsão irracional para roubar.',
'Ligyromania':'compulsão incontrolável de fazer barulhos altos ou estridentes.',
'Linonomania':'obsessão por cordas.',
'Lotterymania':'um desejo extremo de participar de loterias.',
'Lypemania':'uma tendência anormal à melancolia profunda.',
'Megalithomania':'tendência anormal para compor idéias bizarras quando na presença de círculos de pedra/pedras em pé.',
'Melomania':'obsessão por música ou uma melodia específica.',
'Metromania':'desejo insaciável de escrever versos.',
'Misomania':'ódio de tudo, obsessão de odiar algum assunto ou grupo.',
'Monomania':'obsessão anormal com um único pensamento ou ideia.',
'Mythomania':'mentir ou exagerar de forma anormal.',
'Nosomania':'ilusão de sofrer de uma doença imaginária.',
'Notomania':'compulsão para registrar tudo (por exemplo, fotografia).',
'Onomamania':'obsessão por nomes (pessoas, lugares, coisas).',
'Onomatomania':'vontade irresistível de repetir certas palavras.',
'Onychotillomania':'roer compulsivamente as unhas.',
'Opsomania':'amor anormal por um tipo de comida.',
'Paramania':'um prazer anormal em reclamar.',
'Personamania':'obsessão no uso de máscaras.',
'Phasmomania':'obsessão por fantasmas.',
'Phonomania':'tendência patológica ao assassinato.',
'Photomania':'desejo patológico de luz.',
'Planomania':'desejo anormal de desobedecer as normas sociais.',
'Plutomania':'desejo obsessivo de riqueza.',
'Pseudomania':'compulsão irracional por mentir.',
'Pyromania':'Compulsão de iniciar incêndios.',
'Question-Asking Mania':'Desejo compulsivo de fazer perguntas.',
'Rhinotillexomania':'Desejo compulsivo de mexer no nariz.',
'Scribbleomania':'obsessão por rabiscos/rabiscos.',
'Siderodromomania':'intenso fascínio por trens e viagens ferroviárias.',
'Sophomania':'a ilusão de que alguém é incrivelmente inteligente.',
'Technomania':'obsessão por novas tecnologias.',
'Thanatomania':'crença de que alguém é amaldiçoado pela magia da morte.',
'Theomania':'crença de que ele ou ela é um deus.',
'Titillomaniac':'compulsão por se coçar.',
'Tomomania':'predileção irracional para a realização de cirurgias.',
'Trichotillomania':'desejo de arrancar o próprio cabelo.',
'Typhlomania':'cegueira patológica.',
'Xenomania':'obsessão por coisas estrangeiras.',
'Zoomania':'afeição insana pelos animais.'}

dict_fobia = {
'Ablutophobia':'Medo de se lavar ou tomar banho.',
'Acrophobia':'Medo de alturas.',
'Aerophobia':'Medo de voar.',
'Agoraphobia':'Medo de lugares abertos e públicos (lotados).',
'Alektorophobia':'Medo de galinhas.',
'Alliumphobia':'Medo de alho',
'Amaxophobia':'Medo de estar ou andar em veículos.',
'Ancraophobia':'Medo do vento.',
'Androphobia':'Medo dos homens.',
'Anglophobia':'Medo da Inglaterra ou da cultura inglesa, etc.',
'Anthrophobia':'Medo de flores.',
'Apotemnophobia':'Medo de pessoas com amputações.',
'Arachnophobia':'Medo de aranhas.',
'Astraphobia':'Medo de raio.',
'Atephobia':'Medo de ruína ou ruínas.',
'Aulophobia':'Medo de flautas.',
'Bacteriophobia':'Medo de bactérias.',
'Ballistophobia':'Medo de mísseis ou balas.',
'Basophobia':'Medo de cair.',
'Bibliophobia':'Medo de livros.',
'Botanophobia':'Medo de plantas.',
'Caligynephobia':'Medo de mulheres bonitas.',
'Cheimaphobia':'Medo de frio.',
'Chronomentrophobia':'Medo de relógios.',
'Claustrophobia':'Medo de espaços confinados.',
'Coulrophobia':'Medo de palhaços.',
'Cynophobia':'Medo de cães.',
'Demonophobia':'Medo de espíritos ou demônios.',
'Demophobia':'Medo de multidões.',
'Dentophobia':'Medo de dentistas.',
'Disposophobia':'Medo de jogar coisas fora (acumular).',
'Doraphobia':'Medo de pelo.',
'Dromophobia':'Medo de atravessar ruas.',
'Ecclesiophobia':'Medo de igreja.',
'Eisoptrophobia':'Medo de espelhos.',
'Enetophobia':'Medo de agulhas ou alfinetes.',
'Entomophobia':'Medo de insetos.',
'Felinophobia':'Medo de gatos.',
'Gephyrophobia':'Medo de cruzar pontes.',
'Gerontophobia':'Medo de velhos ou de envelhecer.',
'Gynophobia':'Medo de mulheres.',
'Haemaphobia':'Medo de sangue.',
'Hamartophobia':'Medo de pecar.',
'Haphophobia':'Medo de toque.',
'Herpetophobia':'Medo de répteis.',
'Homichlophobia':'Medo de neblina.',
'Hoplophobia':'Medo de armas de fogo.',
'Hydrophobia':'Medo de água.',
'Hypnophobia':'Medo de dormir ou de ser hipnotizado.',
'Iatrophobia':'Medo de médicos.',
'Ichthyophobia':'Medo de peixe.',
'Katsaridaphobia':'Medo de baratas.',
'Keraunophobia':'Medo de trovão.',
'Lachanophobia':'Medo de vegetais.',
'Ligyrophobia':'Medo de barulhos altos.',
'Limnophobia':'Medo de lagos.',
'Mechanophobia':'Medo de máquinas ou máquinas.',
'Megalophobia':'Medo de coisas grandes.',
'Merinthophobia':'Medo de ser amarrado ou amarrado.',
'Meteorophobia':'Medo de meteoros ou meteoritos.',
'Monophobia':'Medo de ficar sozinho.',
'Mysophobia':'Medo de sujeira ou contaminação.',
'Myxophobia':'Medo de lodo.',
'Necrophobia':'Medo de coisas mortas.',
'Octophobia':'Medo da figura 8.',
'Odontophobia':'Medo de dentes.',
'Oneirophobia':'Medo dos sonhos.',
'Onomatophobia':'Medo de ouvir uma determinada palavra ou palavras.',
'Ophidiophobia':'Medo de cobras.',
'Ornithophobia':'Medo de pássaros.',
'Parasitophobia':'Medo de parasitas.',
'Pediophobia':'Medo de bonecas.',
'Phagophobia':'Medo de engolir, de comer ou de ser comido.',
'Pharmacophobia':'Medo de drogas.',
'Phasmophobia':'Medo de fantasmas.',
'Phenogophobia':'Medo da luz do dia.',
'Pogonophobia':'Medo de barba.',
'Potamophobia':'Medo de rios.',
'Potophobia':'Medo de álcool ou bebidas alcoólicas.',
'Pyrophobia':'Medo de fogo.',
'Rhabdophobia':'Medo de magia.',
'Scotophobia':'Medo da escuridão ou da noite.',
'Selenophobia':'Medo da lua.',
'Siderodromophobia':'Medo de viajar de trem.',
'Siderophobia':'Medo de estrelas.',
'Stenophobia':'Medo de coisas ou lugares estreitos.',
'Symmetrophobia':'Medo da simetria.',
'Taphephobia':'Medo de ser enterrado vivo ou de cemitérios.',
'Taurophobia':'Medo de touros.',
'Telephonophobia':'Medo de telefones.',
'Teratophobia':'Medo de monstros.',
'Thalassophobia':'Medo do mar.',
'Tomophobia':'Medo de operações cirúrgicas.',
'Triskadekaphobia':'Medo do número 13.',
'Vestiphobia':'Medo de roupas.',
'Wiccaphobia':'Medo de bruxas e feitiçaria.',
'Xanthophobia':'Medo da cor amarela ou da palavra “amarelo”.',
'Xenoglossophobia':'Medo de línguas estrangeiras.',
'Xenophobia':'Medo de estranhos ou estrangeiros.',
'Zoophobia':'Medo de animais.'
}
# vai haver sempre uma faca (mellee)
# pode haver ou nao uma de fogo (adicionar x nadas)
armas = {'branca': {
            'Faca Pequena' : ['1D4+DB', 'Toque'], 
            'Faca Media'   : ['1D4+2+DB', 'Toque'],
            'Taco Basebol' : ['1D8+DB', 'Toque'],
            'Bastão'     : ['1D6+DB', 'Toque'] # Nightstick no manual, é semelhante
            },
        'fogo':{
            'Nada0'                   : ['0D0', '0m', '0', '100'],
            'AK-47 or AKM'           : ['2D6+1' , '90m' , '30' , '100'],
            'Glock 17 9mm Auto'      : ['1D10' , '14m' , '17' , '98'],
            'Nada1'                   : ['0D0', '0m', '0', '1'],
            'Galil Assault Rifle'    : ['2D6' , '101m' , '20' , '98'],
            'Nada2'                   : ['0D0', '0m', '0', '1'],
            '.357 Magnum Revolver'   : ['1D8+1D4' , '14m' , '6' , '100'],
            '.22 Bolt-Action Rifle'  : ['1D6+1' , '28m' , '6' , '99'],
            '12-gauge Shotgun (2B)'  : ['1D6; 2D6; 4D6' , '10m; 18m; 48m' , '2' , '100'],
            'Nada3'                   : ['0D0', '0m', '0', '1'],
            '.22 Short Automatic'    : ['1D6' , '9m' , '6' , '100'],
            'Nada4'                   : ['0D0', '0m', '0', '1'],
            '.32 or 7.65mm Revolver' : ['1D8' , '14m' , '6' , '100']
            }
        }

dicti_nomes = {'Homem': 
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
'Mulher':
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

def criar_abrir_file(nome, status, arma_branca, caracteristicas_arma_branca, skill_faca, arma_fogo,caracteristicas_arma_fogo,skill_arma):
    #SEPARADOR = SEPARADOR
    #arquivo = "npcs.csv"
    try:       
        pd.read_csv(arquivo) # Checker, ve se existe ficheiro      
        # Formatação dos dados em colunas
        row_data = [nome, status['AGE'], status['HP'], status['SAN'], status['STR'], status['CON'], status['SIZ'],
            status['DEX'], status['APP'], status['EDU'], status['INT'], status['POW'], status['MOV'],status['DB'],
            arma_branca, skill_faca, caracteristicas_arma_branca[0], caracteristicas_arma_branca[1], arma_fogo, 
            skill_arma, caracteristicas_arma_fogo[0], caracteristicas_arma_fogo[1], caracteristicas_arma_fogo[2], 
            caracteristicas_arma_fogo[3]]

        # Escreve os dados no arquivo CSV
        with open(arquivo, 'a+', encoding='utf-8') as fh:
            fh.write(",".join(map(str, row_data)) + "\n")
            print('g')  

        # Exibe os NPCs presentes no arquivo CSV
        npcs = pd.read_csv(arquivo, sep=SEPARADOR, on_bad_lines='skip')
        print("\nFicheiro de NPCs encontrado, estes são os NPCs:")
        print(npcs)
            
        choice = input('Deseja continuar?\n\t1 : Criar um npc aleatorio\n\t2 : Voltar ao menu inicial\n\t3 : Exit\n')
        if int(choice) == 1:
                criação_npc(0)
        elif int(choice) == 2:
                escolhas()
        else:
            exit
    except FileNotFoundError:
        print("Ficheiro nao encontrado, a criar um de raiz...")
        with open(arquivo, 'w', encoding='utf-8') as fh:
            fh.write("Nome,AGE,HP,SAN,STR,CON,SIZ,DEX,APP,EDU,INT,POW,MOV,DB,Arma Branca,Habilidade Arma Branca,Dano,Distancia,Arma Fogo,Habilidade Arma Fogo,Dano,Distancia,N_Balas,Defeito\n")

        row_data = [nome, status['AGE'], status['HP'], status['SAN'], status['STR'], status['CON'], status['SIZ'],
            status['DEX'], status['APP'], status['EDU'], status['INT'], status['POW'], status['MOV'],status['DB'],
            arma_branca, skill_faca, caracteristicas_arma_branca[0], caracteristicas_arma_branca[1], arma_fogo, skill_arma, caracteristicas_arma_fogo[0], caracteristicas_arma_fogo[1],
            caracteristicas_arma_fogo[2], caracteristicas_arma_fogo[3]]
        print('j') 
        # Escreve os dados no arquivo CSV
        with open(arquivo, 'a+', encoding='utf-8') as fh:
            fh.write(",".join(map(str, row_data)) + "\n")

        # Exibe os NPCs presentes no arquivo CSV
        npcs = pd.read_csv(arquivo, sep=SEPARADOR, on_bad_lines='skip')
        print("\nFicheiro de NPCs encontrado, estes são os NPCs:")
        print(npcs)
            
        choice = input('Deseja continuar?\n\t1 : Criar um npc aleatorio\n\t2 : Voltar ao menu inicial\n\t3 : Exit\n')
        if int(choice) == 1:
                criação_npc(0)
        elif int(choice) == 2:
                escolhas()
        else:
            exit

def visualize_file():
    try:
        # Carrega os dados do arquivo CSV em um DataFrame
        df = pd.read_csv(arquivo, sep=SEPARADOR)

        # Exibe o DataFrame completo sem truncar as linhas
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(df)

        choice = input('Deseja continuar?\n\t1 : Voltar ao menu inicial\n\t2 : Exit\n')
        if int(choice) == 1:
            escolhas()
        else:
            exit
            
    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não foi encontrado.")
        escolhas()

def lancar_dados(n_dados, lados, mostrar=False):
    soma = 0 
    for i in range(n_dados):
        resultado = random.randint(1, lados)
        if mostrar == True:
            print(f"Lançamento {i+1} - Resultado : {resultado}")
        soma += resultado
    
    if mostrar == True:
        print('Valor dos dados:', soma)
        choice = input('Deseja continuar?\n\t1 : Lançar novamente os dados\n\t2 : Voltar ao menu inicial\n\t3 : Exit\n')
        if int(choice) == 1:
            mostrar = True
            n_dados = int(input("Quantos dados queres lançar? "))
            n_lados = int(input("Quantos lados? "))
            lancar_dados(n_dados, n_lados, mostrar)
        elif int(choice) == 2:
            escolhas()
        else:
            exit
    
    return soma

def fobias_escolha():
    fobia = random.choice(list(dict_fobia.keys()))
    print(fobia, '-->', dict_fobia[fobia])
    choice = input('Deseja continuar?\n\t1 : Fazer nova fobia\n\t2 : Voltar ao menu inicial\n\t3 : Exit\n')
    if int(choice) == 1:
        fobias_escolha()
    elif int(choice) == 2:
        escolhas()
    else:
        exit

def mania_escolha():
    mania = random.choice(list(dict_mania.keys()))
    print(mania, '-->', dict_mania[mania])
    choice = input('Deseja continuar?\n\t1 : Fazer nova mania\n\t2 : Voltar ao menu inicial\n\t3 : Exit\n')
    if int(choice) == 1:
        mania_escolha()
    elif int(choice) == 2:
        escolhas()
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
        STR = int(input('Força/STR:\n')) # Força
        CON = int(input('Constituição/CON:\n')) # Constituição
        SIZ = int(input('Tamanho/SIZ:\n') )# Tamanho
        DEX = int(input('Destreza/DEX:\n')) # Destreza
        APP = int(input('Aparencia/APP:\n')) # Aparência
        EDU = int(input('Educação/EDU:\n')) # Educação 
        INT = int(input('Inteligencia/INT:\n')) # Inteligência
        POW = int(input('Poder/POW:\n'))# Poder
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

        AGE = int(input('Idade/AGE:\n'))

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
    return stats

def criação_npc(number):
    if number == 0:
        try:    
            arma_branca = random.choice(list(armas['branca'].keys()))            
            arma_fogo = random.choice(list(armas['fogo'].keys()))
            genero = input('\t1 : Homem\n\t2 : Mulher\n\t3 : Sair\n')
            if int(genero) == 1:
                nome = random.choice(dicti_nomes['Homem'])
            elif int(genero) == 2:
                nome = random.choice(dicti_nomes['Mulher'])
            else:
                escolhas()
            
            stats = gerar_stats(0)
            skill_arma, skill_faca = valores_skill()
            criar_abrir_file(nome, stats, arma_branca, armas['branca'][arma_branca],skill_faca,arma_fogo, armas['fogo'][arma_fogo],skill_arma)
            
        except:
            print('O valor introduzido não existe. Tente novamente.')
            criação_npc(0)
    elif number == 1:
        arma_branca = random.choice(list(armas['branca'].keys()))
        arma_fogo = random.choice(list(armas['fogo'].keys()))
        nome = str(input('Nome:\n'))
        stats = gerar_stats(1)
        skill_arma, skill_faca = valores_skill()
        criar_abrir_file(nome, stats, arma_branca, armas['branca'][arma_branca],skill_faca,arma_fogo, armas['fogo'][arma_fogo],skill_arma)
        
def valores_skill():
    fogo_arma = random.randint(25,66)
    
    fogo_faca = random.randint(25,66)

    return fogo_arma, fogo_faca

def escolhas():
    try:
        escolha = int(input('O que pretende?\n\t1 : Escolher uma fobia.\n\t2 : Escolher uma mania.\n\t3 : Criar um npc aleatorio.\n\t4 : Lançar dados\n\t5 : Divisão dos numeros\n\t6 : Adicionar um NPC\n\t7 : Abrir ficheiro\n\t8 : Sair\n'))
        if escolha == 1 :
            fobias_escolha()
        elif escolha == 2 :
            mania_escolha()
        elif escolha == 3 :
            criação_npc(0)
        elif escolha == 4 :
            mostrar = True
            n_dados = int(input("Quantos dados queres lançar? "))
            n_lados = int(input("Quantos lados? "))
            lancar_dados(n_dados, n_lados, mostrar)
        elif escolha == 5 :
            divisao()
        elif escolha == 6 :
            criação_npc(1)
        elif escolha == 7 :
            visualize_file()
        elif escolha == 8 :
            exit
        else:
            print('Erro')
            escolhas()
    except Exception as e:
        print('O valor introduzido não existe. Tente novamente.', e)
        escolhas()

def divisao():
    number = int(input('Colocar numero:\n'))
    print('1\t:\t',number,'\n1/2\t:\t' , int(number/2), '\n1/5\t:\t', int(number/5))
    choice = input('Deseja continuar?\n\t1 : Fazer nova divisão\n\t2 : Voltar ao menu inicial\n\t3 : Exit\n')
    if int(choice) == 1:
        divisao()
    elif int(choice) == 2:
        escolhas()
    else:
        exit


if __name__ == '__main__':
    escolhas()
