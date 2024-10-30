""" 1 Crie uma variável para armazenar o nome e a quantidade de XP de um herói
 2 Utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

 Se XP < 1000: Ferro
 Se XP > 1000 e < 2000: Bronze
 Se XP > 2000 e < 5000: Prata
 Se XP > 5000 e < 7000: Ouro
 Se XP > 7000 e < 8000: Platina
 Se XP > 8000 e < 9000: Ascendente
 Se XP > 9000 e < 10000: Imortal
 Se XP > 10000 = Radiante
 
 saída:
 
 O herói de nome {nome} está no nível {nivel}
 """
class Heroi:
    def __init__(self, nome, xp, nivel):
        self.nome = nome
        self.xp = xp
        self.nivel = nivel

def heroi_nome():
    while True:
        nome = input("Informe o nome do herói: ").strip().title()
        if nome.isalpha():
            return nome
        else:
            print("Só são permitidas letras para nome.")
    
def heroi_xp():
    while True:
        try:
            xp = int(input("Informe a quantidade de XP: "))
            if xp > 0:
                return xp
            else:
                print("A quantidade de XP não pode ser igual ou menor do que 0!")
        except ValueError:
            print("Use apenas números para a XP!")
            
def heroi_nivel(xp):
    if xp < 1000:
        return "ferro"
    elif xp < 2000:
        return "bronze"
    elif xp < 5000:
        return "prata"
    elif xp < 7000:
        return "ouro"
    elif xp < 8000:
        return "platina"
    elif xp < 9000:
        return "ascendente"
    elif xp < 10000:
        return "imortal"
    else:
        return "radiante"
            
def main():
    nome = heroi_nome()
    xp = heroi_xp()
    nivel = heroi_nivel(xp)
    
    print(f"O herói de nome {nome} tem {xp} de XP e está no nível {nivel}")
    
main()
     


        
