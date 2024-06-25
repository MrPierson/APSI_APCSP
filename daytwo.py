import random

goat = "🐐"
car = "🚗"
closed_door = "🚪"


class Game:
    def __init__(self):
        self.doors = [goat, goat, car]
        random.shuffle(self.doors)
        self.contestant_choice = None
        self.host_reveal = None

    def pick_door(self, choice=None):
        if choice is None:
            self.contestant_choice = random.randint(0, 2)
        else:
            self.contestant_choice = choice

        remaining_doors = [i for i in range(3) if i != self.contestant_choice and self.doors[i] == goat]
        self.host_reveal = random.choice(remaining_doors)
        
        remaining_choices = [i for i in range(3) if i != self.contestant_choice and i != self.host_reveal]
        self.switch_choice = remaining_choices[0]

    def get_switch_choice(self):
        return self.switch_choice

    def get_contestant_choice(self):
        return self.contestant_choice

    def is_switch_winner(self):
        return self.doors[self.switch_choice] == car

    def is_stay_winner(self):
        return self.doors[self.contestant_choice] == car
    

def monty_hall_simulation(num_trials):
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_trials):
        game = Game()
        game.pick_door()

        if game.is_switch_winner():
            switch_wins += 1
        if game.is_stay_winner():
            stay_wins += 1

    return switch_wins, stay_wins


def print_results(num_trials, switch_wins, stay_wins):
    print(f"After {num_trials} trials:")
    print(f"Switching wins: {switch_wins} ({(switch_wins / num_trials) * 100:.1f}%)")
    print(f"Staying wins: {stay_wins} ({(stay_wins / num_trials) * 100:.1f}%)")


def display_doors(doors, contestant_choice=None, host_reveal=None, reveal_all=False):
    display = []
    for i in range(3):
        if reveal_all:
            display.append(f"[{doors[i]}]")
        elif i == contestant_choice:
            display.append(f"[{closed_door}] (Your choice)")
        elif i == host_reveal:
            display.append(f"[{doors[i]}] (Host reveal)")
        else:
            display.append(f"[{closed_door}]")
    print(" ".join(display))


def interactive_mode():
    while True:
        game = Game()
        display_doors(game.doors)
        choice = int(input("Choose a door (0, 1, or 2): "))
        game.pick_door(choice)
        
        display_doors(game.doors, contestant_choice=game.get_contestant_choice(), host_reveal=game.host_reveal)
        print(f"Host reveals a goat behind door {game.host_reveal}.")
        
        switch = input(f"Do you want to switch to door {game.get_switch_choice()}? (yes/no): ").strip().lower()
        if switch == "yes":
            final_choice = game.get_switch_choice()
        else:
            final_choice = game.get_contestant_choice()
        
        display_doors(game.doors, reveal_all=True)
        if game.doors[final_choice] == car:
            print(f"Congratulations! You won the car! It was behind door {final_choice}.")
        else:
            print(f"Sorry, you got a goat. It was behind door {final_choice}.")

        play_again = input("Do you want to play another game? (yes/no): ").strip().lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    mode = input("Choose mode: interactive or simulation: ").strip().lower()
    
    if mode == "interactive":
        interactive_mode()
    elif mode == "simulation":
        num_trials = int(input("Enter the number of trials for simulation: "))
        switch_wins, stay_wins = monty_hall_simulation(num_trials)
        print_results(num_trials, switch_wins, stay_wins)
    else:
        print("Invalid mode. Please choose either 'interactive' or 'simulation'.")
