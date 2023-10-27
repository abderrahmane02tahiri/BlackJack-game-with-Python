import os


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def draw_blackjack_logo():
    clear_screen()
    logo = """
████████     ███     ██       ██     ██      ███████     ██
   ██      ██   ██   ██       ██             ██    ██    
   ██      ██   ██   ██       ██     ██      ██    ██    ██
   ██      ███████   ███████████     ██      ████████    ██
   ██      ██   ██   ██       ██     ██      ██    ██    ██
   ██      ██   ██   ██       ██     ██      ██    ██    ██
   ██      ██   ██   ██       ██     ██      ██    ██    ██ 
   
    """
    print(logo)


if __name__ == "__main__":
    draw_blackjack_logo()
