from function import add_person, show_person

while True:
    print("""
    1. Dodanie osoby
    2. Zobaczenie dane osób
    3. Zakończenie
    """)
    id_option = int(input("Wybierz opcję: "))
    print()

    if id_option == 1:
        add_person()

    if id_option == 2:
        show_person()

    if id_option == 3:
        break