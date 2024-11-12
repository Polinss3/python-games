import random

class GuessTheNumber:
    def __init__(self, min_number=1, max_number=100):
        self.min_number = min_number
        self.max_number = max_number
        self.target_number = random.randint(min_number, max_number)
        self.attempts = 0

    def guess(self, number):
        """Takes a guess from the player and returns a hint or success message."""
        self.attempts += 1
        if number < self.target_number:
            return "Higher"
        elif number > self.target_number:
            return "Lower"
        else:
            return "Correct!"

    def reset_game(self):
        """Resets the game with a new target number and resets attempts."""
        self.target_number = random.randint(self.min_number, self.max_number)
        self.attempts = 0

if __name__ == "__main__":
    game = GuessTheNumber()
    print(f"Welcome to 'Guess the Number'! Try to guess the number between {game.min_number} and {game.max_number}.")

    while True:
        try:
            player_guess = int(input("Enter your guess: "))
            result = game.guess(player_guess)
            print(result)
            if result == "Correct!":
                print(f"Congratulations! You've guessed the number in {game.attempts} attempts.")
                play_again = input("Do you want to play again? (yes/no): ").strip().lower()
                if play_again == "yes":
                    game.reset_game()
                    print("New game started. Try to guess the number again!")
                else:
                    print("Thank you for playing!")
                    break
        except ValueError:
            print("Please enter a valid number.")
