

def main():
    import random
    dice_rolls = int(input('Number of Dice? '))
    dice_sides = int(input('Sides on the Dice? '))
    dice_sum = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1, dice_sides)
        dice_sum += roll
        if roll == 1:
            print(f'Fail: Rolled a {roll}')
        elif roll == dice_sides:
            print(f'Success: Rolled a {dice_sides}')
        else:
            print(f'You rolled a {roll}')
    print(f'The sum of the dice is {dice_sum}');


if __name__ == "__main__":
    main()
