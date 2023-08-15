import random


MAX_LINES = 3
MAX_BET = 50000
MIN_BET = 1

ROWS = 3
COLS = 3


symbol_count = {
    'C': 4,
    'B': 4,
    'L': 4,
    'O': 4
    }

symbol_values= {
    'C': 5,
    'B': 4,
    'L': 3,
    'O': 2
    }

def check_winnings(columns, lines, bet, values):
    '''This function will check if the player won'''
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol_check != symbol:
                break
        else:
            winning += bet * values[symbol]
            winning_lines.append(line + 1)

    return winning, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    '''This function will replicate 
    the slot machine spin'''

    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):       # generate column for every COL see **Global variable**
        column = []
        current_symbols = all_symbols[:]        # make a copy of all_symbols
        for _ in range(rows):                   # pick random values for each ROW see  **Global variable**
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)

    
    return columns

def print_slot_machine_spin(columns):
    '''This function will print the 
    slot machine spin'''

    # for row in range(0, len(columns)):      # loop through the columns and group them by rows
    #     print(columns[i:i+rows]) 

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:       # if i is not equal to the last index print with a | at the end
                print(column[row], end =' | ')
            else:
                print(column[row], end=' ')

        print()     # print a new line after each row

def get_deposit():
    '''This function will get the 
    deposit amount from the user '''

    while True:
        amount = input('What are you depositing? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Deposit should be greater than 0')
        
        else:
            print('Please deposit a positive number')
            
    return amount

def get_betting_lines():
    '''This function will get the 
    deposit amount from the user '''

    while True:
        lines = input(f'How many lines are you betting on (1 - {MAX_LINES})? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f'Enter a number between 1 and {MAX_LINES}')
        
        else:
            print('Please enter a  number')
            
    return lines


def get_bet_amount():
    ''' This function will get the bet amount from the user'''

    while True:
        amount = input('What are you betting on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount should be between {MIN_BET} and {MAX_BET}')
        
        else:
            print('Please bet a positive number')
                
    return amount    

def spin(deposit):
    '''This function will run the spin'''
    
    lines = get_betting_lines()
    
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines
        
        if total_bet > deposit:
            print('You do not have enough money to bet that amount')
            
        else:
            break

    print(f'You are betting {bet} on {lines} lines. The total amount you are betting is ${total_bet}.')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine_spin(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f'You won ${winnings}')
    print(f'you won on lines', *winning_lines)
    winnings = winnings - total_bet
    
    return winnings



def main():
   balance = get_deposit()
   while True:
    print(f'Your balance is ${balance}')
    answer = input('Press Enter to play (q to quit)')

    if answer.lower() == 'q':
        break
    balance += spin(balance)
    
    print(f'Your final balance is ${balance}')

main()