import random

class Move:
    def __str__(self):
        return self.NAME
    def wins_against(self, other_move):
        return other_move.NAME in self.BEATS
class Rock(Move):
    NAME = 'rock'
    BEATS = ['scissors', 'lizard']
class Paper(Move):
    NAME = 'paper'
    BEATS = ['rock','spock']
class Scissors(Move):
    NAME = 'scissors'
    BEATS = ['paper','lizard']
class Spock(Move):
    NAME = 'spock'
    BEATS = ['scissors','rock']
class Lizard(Move):
    NAME = 'lizard'
    BEATS = ['spock', 'paper']
class Player:
    CHOICES = {'rock': Rock, 'paper': Paper, 'scissors': Scissors, 'lizard': Lizard, 'spock': Spock}

    def __init__(self):
        self.move = None
        self.score = 0

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock, paper, scissors, lizard or spock: '

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = Player.CHOICES[choice]()

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(list(Player.CHOICES.values()))()


class RPSGame:
    ROUNDS = 5

    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!")

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!")

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return human_move.wins_against(computer_move)

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return computer_move.wins_against(human_move)

    def _display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins(): 
            self._human.score += 1        
            print('You win!')
        elif self._computer_wins():
            self._computer.score += 1
            print('Computer wins!')
        else:
            print("It's a tie")

    def _grand_winner(self):
        return self._human.score == RPSGame.ROUNDS or self._computer.score == RPSGame.ROUNDS
    
    def _display_grand_winner(self):
        winner = 'You won the match!' if self._human.score == RPSGame.ROUNDS else 'Computer won the match!'
        print(winner)

    def _play_again(self):
        answer = input("Would you like to play again? (y/n) ")
        return answer.lower().startswith('y')

    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if self._grand_winner():
                self._display_grand_winner()
                break
            if not self._play_again():
                break
        self._display_goodbye_message()

RPSGame().play()