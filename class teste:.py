"""Classe Bola: 
Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor 
"""

"""class ball:
    def __init__(self,color,tam,tipo_de_material):
        self.cor = color
        self.tamanho = ((tam * tam)  * 3,14)
        self.type = tipo_de_material

    def trocar_cor(self,color):
        self.cor = color
        return(self.cor)
    
    def mostra_cor(self):
        #self.cor = color
        return (print(self.cor))

bolas = ball('Vermelha',2,'pelota')
bolas.trocar_cor("azul marinho")
#print(f"cor = {bolas.cor} tamanho = {bolas.tamanho}cm² tipo da bola = {bolas.type}")
bolas.mostra_cor()"""


"""Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; 
"""

"""class square:
    def __init__ (self,l1,l2):
        self.lado1 = l1
        self.lado2 = l2
        print(self.lado1,self.lado2)

    def mudar_lado(self):
        mudança = int(input("Digite qual lado voce deseja mudar,se L1 == 1 ou L2 == 2\n"))
        while(True):
            if(mudança == 1):
                self.lado1 = int(input("Digite o valor do seu lado:\n"))
                break
            elif(mudança == 2):
                self.lado2 = int(input("Digite o valor do seu lado:\n"))
                raise("fodase")
            else:
                print("invalido,tente novamente\n")
                mudança = int(input("Digite qual lado voce deseja mudar,se L1 ou L2"))

    def calcula_area(self):
        total = self.lado1 * self.lado2
        print(total)
        return (print(f"A area total foi de = {total}"))
        
quadrado = square(2,4)
quadrado.calcula_area()"""

""" Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer.
    Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, 
    ela deve crescer 0,5 cm.""" 

class Pessoa:
    def __init__(self,name,age,weight,heigth):
        self.nome = name
        self.idade = age
        self.peso = weight
        self.altura = heigth

    def get_old(self):
        tempo = int(input("Digite a idade do individuo(a)\n"))
        tempo_de_crescimento = (self.idade + tempo) - self.idade
        
        self.idade = tempo
    