import view as v
import data_base as db

def phone():
    s = v.hello()
    s = int(s)
    print(f'{s} db')
    if s == 1:
        telephone = v.get_tel()
        name = v.get_name()
        db.save_tel(name, telephone)
    elif s == 2:
        contact = db.import_cont()
        print(contact)