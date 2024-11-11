class Hero():
    def __init__(self, name=None, age=None, heroClass=None):
        self.name = name
        self.age = age
        self.heroClass = heroClass
        self.attack_Description = ""

    def createHeroName(self):
        while True:
            name = input("Enter your caracter's name: ").strip()
            if name.isalpha():
                self.name = name
                break
            else:
                print("Only letters are allowed for the name. Please, try again!")

    def createHeroAge(self):
        while True:
            try:
                age = int(input("Enter your caracter's age: "))
                if age > 0:
                    self.age = age
                    break
                else:
                    print("Only integer numbers are allowed for the caracter's age. Please, try again!")
            except ValueError:
                print("Only integer numbers are allowed for the character's age!")

    classDescription = {
        "Knight": "The Knight class often represents a strong, heavily-armored warrior who excels at \nclose-range combat and acts as the frontline defender of the party.",
        "Wizard": "The Wizard is a classic character class known for using magic to cast powerful spells",
        "Archer": "An Archer is a character class specializing in ranged attacks, typically using bows, \ncrossbows, or other long-range weapons. Archers are often associated with agility, precision, and speed, \nand they excel in attacking enemies from a distance rather than close combat.",
        "Bard": "The Bard class is a unique and versatile character type, often serving as a support or `jack-of-all-trades`.",
        "Druid": "The Druid is a unique class, often blending the abilities of magic users with the traits of nature-themed classes"
    }   
    def createHeroClass(self):
            availableClass = {
                1: "Knight",
                2: "Wizard",
                3: "Archer",
                4: "Bard",
                5: "Druid"
            }
            while True:
                try: 
                    choose = int(input("""
[1] Knight
[2] Wizard
[3] Archer
[4] Bard
[5] Druid
select your caracter's class: """))
                    if choose in availableClass:
                        self.heroClass = availableClass[choose]
                        print(f"You chose: {self.heroClass} - {self.classDescription[self.heroClass]}")
                        break
                    else: print("Select one of the five available options!")
                except ValueError:
                    print("Only integer numbers between 1 and 5 are allowed!")
    
    def setAttack(self):
        attackDescription = {
            "Knight": "The knight struck with his sword!",
            "Wizard": "The wizard used a fireball!",
            "Archer": "The archer shot an arrow!",
            "Bard": "The bard plays a song that damages the enemies!",
            "Druid": "The druid transforms into a rhino and charges at the enemies!"
        }
        if self.heroClass in attackDescription:
            self.attack_Description = attackDescription[self.heroClass]

def main():
    hero = Hero()
    hero.createHeroName()
    hero.createHeroAge()
    hero.createHeroClass()
    hero.setAttack()
    print(f"Caracter created:\nName: {hero.name}\nAge: {hero.age}\nClass: {hero.heroClass}\n{hero.attack_Description}")
main()
