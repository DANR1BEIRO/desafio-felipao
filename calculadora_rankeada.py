class PlayerClass:
    def __init__(self, victory, loss):
        self.victory = victory
        self.loss = loss
        self.balance = self.victory - self.loss
        self.rank = self.calculate_rank()

    def calculate_rank(self):
        if self.balance < 10:
            return "iron"
        elif self.balance < 20:
            return "bronze"
        elif self.balance < 50:
            return "silver"
        elif self.balance < 80:
            return "gold"
        elif self.balance < 90:
            return "diamond"
        elif self.balance < 100:
            return "legendary"
        else:
            return "immortal"
            
def get_integer_input(a):
    while True:
        try:
            value = int(input(a))
            if value < 0:
                print("Number can't be negative!")
                continue
            return value

        except ValueError:
            print("Only integer positive numbers are allowed!")
            
def main():
    wins = get_integer_input("Number of wins: ")
    loss = get_integer_input("Number of loss: ")
    player = PlayerClass(wins, loss)

    print(f"The player has a balance of {player.balance} and is at the {player.rank} rank")

main()