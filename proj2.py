import random
#start game
def roll_dice():
    """Simulate rolling three dice."""
    return [random.randint(1, 6) for _ in range(2)]

def is_tupled_out(dice):
    """Check if the rolled dice constitute a 'tupled out' scenario."""
    return len(set(dice)) == 1

def fix_dice(dice):
    """Fix dice with the same value."""
    fixed_dice = []
    for die in dice:
        if dice.count(die) >= 2:
            fixed_dice.append(die)
        else:
            fixed_dice.append(None)
    return fixed_dice

def main():
    num_players = int(input("Enter the number of players: "))
    target_score = int(input("Enter the target score: "))
    
    scores = [0] * num_players
    
    while max(scores) < target_score:
        for player in range(num_players):
            print(f"Player {player + 1}'s turn:")
            current_score = scores[player]
            dice = roll_dice()
            print("Dice:", dice)
            
            if is_tupled_out(dice):
                print("Tupled out! Score for this turn: 0")
                continue
            
            fixed_dice = fix_dice(dice)
            print("Fixed dice:", fixed_dice)
            
            while True:
                choice = input("Do you want to re-roll any dice? (y/n): ")
                if choice.lower() == 'n':
                    break
                elif choice.lower() == 'y':
                    indices = input("Enter indices of dice to re-roll (e.g., 0 2): ").split()
                    indices = [int(idx) for idx in indices if idx.isdigit() and int(idx) < 3]
                    for idx in indices:
                        dice[idx] = random.randint(1, 6)
                    print("New dice:", dice)
                    fixed_dice = fix_dice(dice)
                    print("Fixed dice:", fixed_dice)
            
            score = sum(d for d in dice if d is not None)
            print("Score for this turn:", score)
            scores[player] += score
            print("Total score:", scores[player])
            print()
            
            if is_tupled_out(dice):
                scores[player] = 0
                
            if scores[player] >= target_score:
                print(f"Player {player + 1} wins!")
                break
            #game over

                
if __name__ == "__main__":
    main()
