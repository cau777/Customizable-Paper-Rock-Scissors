from random import choice


def read_possible_options():
    default_options = ['rock', 'paper', 'scissors']
    while True:
        s = input('Game objects [Press enter to default]: ').replace(' ', '')
        if s == '':
            return default_options
        else:
            separated = s.split(',')
            if len(separated) >= 3:
                if len(separated) % 2 != 0:
                    return separated
                else:
                    print('The game needs an odd number of objects to start')
            else:
                print('The game needs at least 3 objects to start')


def generate_options(start, increment):
    total = len(possibleOptions)
    index = start
    while True:
        index += increment
        yield possibleOptions[(index + total) % total]


def load_ratings():
    result = {}
    f = open('rating.txt', 'r')
    for line in f:
        parts = line.split()
        result[parts[0]] = int(parts[1])
    f.close()
    return result


def save_ratings():
    s = ''
    f = open('rating.txt', 'w')
    for key, value in ratings.items():
        s += key + ' ' + str(value) + '\n'
    f.write(s)
    f.close()


def computer_choose():
    return choice(possibleOptions)


def compute_loss():
    print(f"Sorry, but the computer chose {computer_choice}")


def compute_draw():
    ratings[user_name] += 50
    print(f'There is a draw ({computer_choice})')


def compute_win():
    ratings[user_name] += 100
    print(f'Well done. The computer chose {computer_choice} and failed')


def analyse_game():
    if user_input == computer_choice:
        compute_draw()
    else:
        option_index = possibleOptions.index(user_input)
        for weaker, stronger in zip(generate_options(option_index, -1), generate_options(option_index, 1)):
            if computer_choice is weaker:
                compute_win()
                return
            elif computer_choice is stronger:
                compute_loss()
                return


print('!rating to see your rating', '!exit to stop playing', sep='\n')
user_name = input('Enter your name: ')
print(f'Hello, {user_name}')

ratings = load_ratings()
if user_name not in ratings.keys():
    ratings[user_name] = 0

possibleOptions = read_possible_options()
print("Okay, let's start with", possibleOptions)

while True:
    user_input = input('You choice: ')

    if user_input == '!exit':
        print('Bye!')
        break
    elif user_input == '!rating':
        print(f'Your rating: {ratings[user_name]}')
    elif user_input in possibleOptions:
        computer_choice = computer_choose()
        analyse_game()
        save_ratings()
    else:
        print('Invalid input')
