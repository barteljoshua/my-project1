from game.die import Die

class Director:

    def __init__(self):
        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            die = Die()
            self.dice.append(die)
    def start_game(self):
        while self.is_playing:
            self.input()
            self.update()
            self.output()


    def input(self):
        playGame = input("do you want to roll the dice? [y/n] ")
        self.is_playing = (playGame == "y")
    
    def update(self):
        if not self.is_playing:
            return
        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points
        self.total_score += self.score
    
    def output(self):
        if not self.is_playing:
            return
        
        values = ""
        
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "
        
        print(f"You rolled: {values}")
        print(f"You score is: {self.total_score}")
        self.is_playing == (self.score > 0)
    
