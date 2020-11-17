import random
import textwrap

def print_bold(msg, end='\n'):
    """Print a string in 'bold' font"""
    print("\033[1m" + msg + "\033[0m", end=end)


def print_dotted_line(width=72):
    """Print a dotted (rather 'dashed') line"""
    print('-'*width)

def show_theme_message(width):
    """Print the game theme in the terminal window"""
    print_dotted_line()
    print_bold("Attack of The Orcs v0.0.5:")
    msg = (
        "The war between humans and their arch enemies, Orcs, was in the "
        "offing. Sir Eggy, one of the brave knights guarding the southern "
        "plains began a long journey towards the east through an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decided to take"
        " a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he  decided to enter..")

    print(textwrap.fill(msg, width=width))


def show_game_mission():
    """Print the game mission in the terminal window"""
    print_bold("Mission:")
    print("\tChoose a hut where Sir Eggy can rest...")
    print_bold("TIP:")
    print("Be careful as there are enemies lurking around!")
    print_dotted_line()


def reveal_occupants(idx, huts):
    """Print the occupants of the hut"""
    msg = ""
    print("Revealing the occupants...")
    for i in range(len(huts)):
        occupant_info = "<%d:%s>" % (i+1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "

    print("\t" + msg)
    print_dotted_line()

def occupy_huts():
    """Randomly populate the `huts` list with occupants"""
    huts = []
    occupants = ['enemy', 'friend', 'unoccupied']
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts


def process_user_choice():
    """Accepts the hut number from the user"""
    msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx

def attack(health_meter):
    targets = 4 * ['player'] + 6 * ['enemy']
    injured_target = random.choice(targets)
    life = health_meter[injured_target]
    injury = random.randint(10, 15)
    health_meter[injured_target] = max(life - injury, 0)
    print("Attack! ", end='')
    show_health(health_meter)

def play_game(health_meter):
    huts = occupy_huts()
    index = process_user_choice()
    reveal_occupants(index, huts)

    print("\033[1m" + "Entering hut %d... " % index + "\033[0m", end=' ')
    if huts[index - 1] != 'enemy':
        print_bold("Congratulations! YOU WIN!!!")
    else:
        print_bold("ENEMY SIGHTED! ", end='')
        show_health(health_meter, bold=True)
        continue_attack = True
        
        while continue_attack:
            continue_attack = input('.......Continue attack? (y/n): ')
            if continue_attack == 'n':
                print_bold('RUNNING AWAY with following health status...')
                show_health(health_meter, bold=True)
                print_bold("GAME OVER")
                break
            
            attack(health_meter)

            if(health_meter['enemy'] <= 0):
                print_bold('GOOD JOB! Enemy defeated, you win!')
                break
            
            if(health_meter['player'] <= 0):
                print_bold("YOU LOSE  :(  Better luck next time")
                break
            
        

def show_health(health_meter, bold=True):
    """Show the remaining hit points of the player and the enemy"""
    msg = "Health: Sir Eggy: %d, Enemy: %d" % (health_meter['player'], health_meter['enemy'])

    if bold:
        print_bold(msg)
    else:
        print(msg)

def reset_health_meter(health_meter):
    health_meter['enemy'] = 30
    health_meter['player'] = 40

def run_application():
    keep_playing = 'y'
    width = 72
    health_meter = {}
    reset_health_meter(health_meter)

    show_theme_message(width)
    show_game_mission()

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        
        play_game(health_meter)
        keep_playing = input("Play again? Yes(y)/No(n):")

if __name__ == '__main__':
    run_application()