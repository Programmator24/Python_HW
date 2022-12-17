
def save_tel(name, tel):
    contact = '/Users/nikitagaripov/Desktop/Python/HW/hw07.py/phone_book.txt'
    with open(contact, 'a') as c:
        c.writelines(f'{name}\n')
        c.writelines(f'{tel}\n')

def import_cont():
    contact = '/Users/nikitagaripov/Desktop/Python/HW/hw07.py/phone_book.txt'
    name = input('print name: ')
    with open (contact, 'r') as c:
        cont = c.readlines()
        for i in range(0, len(cont)):
            if name in cont[i]:
                print(cont[i+1])