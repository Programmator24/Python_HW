# Создайте программу для игры в ""Крестики-нолики"".


table = "/Users/nikitagaripov/Desktop/Python/HW/hw05.py/N_03/table.txt"

row1 = '1 2 3'

row2 = '4 5 6'

row3 = '7 8 9'

print(f'{row1} \n{row2}\n{row3}')

player1 = 'X'

player2 = 'O'





def fill_x (row1, row2, row3):
    x = input()
    if x in row1:
        return(x)
    elif x in row2:
        return(x)
    elif x in row3:
        return(x)
    else:
        print('try again')
        fill_x(row1, row2, row3)
    
    


def replase_x_row1(position, row1, symbol):

    if position == 1:
        row1 = f'{symbol}' + row1[1:]
        print(f'{row1} \n{row2}\n{row3}')
        
    elif position == 2:
        row1 = row1[:2] + f'{symbol}' + row1[3:]
        print(f'{row1} \n{row2}\n{row3}')
        
    elif position == 3:
        row1 = row1[:4] + f'{symbol}'
        print(f'{row1} \n{row2}\n{row3}')
    
    return(row1) 

def replase_x_row2(position, row2, symbol):

    if position == 4:
        row2 = f'{symbol}' + row2[1:]
        print(f'{row1} \n{row2}\n{row3}')
        
    elif position == 5:
        row2 = row2[:2] + f'{symbol}' + row2[3:]
        print(f'{row1} \n{row2}\n{row3}')

    elif position == 6:
        row2 = row2[:4] + f'{symbol}'
        print(f'{row1} \n{row2}\n{row3}')

    return(row2)  
        
def replase_x_row3(position, row3, symbol):
    
    if position == 7:
        row3 = f'{symbol}' + row3[1:]
        print(f'{row1} \n{row2}\n{row3}')

    elif position == 8:
        row3 = row3[:2] + f'{symbol}' + row3[3:]
        print(f'{row1} \n{row2}\n{row3}') 

    elif position == 9:
        row3 = row3[:4] + f'{symbol}'
        print(f'{row1} \n{row2}\n{row3}')

    return(row3)  


def replace_position(a):
    global y
    global row1
    global row2
    global row3
    if y in range(1, 4):
        row1 = replase_x_row1(y, row1, a)
    if y in range(4, 7):
        row2 = replase_x_row2(y, row2, a)
    if y in range(7, 10):
        row3 = replase_x_row3(y, row3, a)


for i in range(0, 4):
    print('player1 chose number = ')
    y = fill_x(row1, row2, row3)
    y = int(y)
    d = replace_position(player1)
    print('player2 chose number =')
    y = fill_x(row1, row2, row3)
    y = int(y)
    d = replace_position(player2)
print('player1 chose number =')
y = fill_x(row1, row2, row3)
y = int(y)
d = replace_position(player1)




    
