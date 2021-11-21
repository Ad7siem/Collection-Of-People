info_all_person = {}


def add_person():
    id_person = 1

    while True:
        info_person = {
            'imie' : '',
            'nazwisko' : '',
            'wiek' : ''
        }
    
        first_name = input('Podaj imię: ')
        last_name = input('Podaj nazwisko: ')
        try:
            age = int(input('Podaj wiek: '))
        except:
            print('To nie jest wartość liczbowa!\n')
            continue
        
        info_person['imie'] = first_name
        info_person['nazwisko'] = last_name
        info_person['wiek'] = age

        info_all_person[f'{id_person}'] = info_person
        id_person += 1

        if end_while():
            break


def show_person():
    while True:
        info = input('Podaj co dokładnie wyświetlić [imie / nazwisko / wiek / all]: ')
        print()
        try:
            if info == 'all':
                for person in info_all_person.values():
                    print(f" Imie - {person['imie']}\n Nazwisko - {person['nazwisko']}\n Wiek - {person['wiek']}\n")
            else:
                for person in info_all_person.values():
                    print(f'{info.capitalize()} -',person[f'{info}'])
            
            if end_while():
                break
        except:
            print('Wybierz imie / nazwisko / wiek / all')
            continue


def end_while():
    end = input('Koniec? [t/n]: ')
    print()
    if end == 't':
        return True
    elif end == 'n':
        return False
    else:
        end_while()
 