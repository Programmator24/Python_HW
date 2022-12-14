# 2. game sweets

sweets = 200

while sweets > 0:
    player1 = int(input('enter number < 29 = '))
    sweets = sweets - player1
    print(f'result = {sweets}')
    if sweets < 28:
        print('bot won')
        break
    import random
    bot = random.randint(1, 28)
    print(f'Bot = {bot}')
    sweets = sweets - bot
    print(f'result = {sweets}')
    if sweets < 28:
        print('player1 won')
        break
