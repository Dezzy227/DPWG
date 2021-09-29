# Erstellen von grafischen Objekten zur einfacheren Nutzung und für mehr Übersichtlichkeit

spacer_8 = '<*><*><*><*><*><*><*><*>'
spacer_16 = '<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>'
greeting = '<*><*> Willkommen beim Passwortgenerator! <*><*>'

# Erstellung von "Grafiken" als Class zur Übersichtlichkeit


def loading():
    print(' ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▢ \n'
          '   ╭━╮╭━╮ ╭╮　╱  \n'
          '   ╰━┫╰━┫ ╰╯╱╭╮ \n'
          '   ╰━╯╰━╯ ╱  ╰╯  COMPLETE \n ')


def bye():
    print('Vielen Dank  für das Benutzen des PyPW-Generator \n'
          'Programmiert von N3ros\n'
          'Auf Wiedersehen\n'
          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀\n'
          '⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀\n'
          '⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀\n'
          '⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀\n'
          '⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀\n'
          '⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆🔴⠀⠀⠀⠀🔴⠀⠀⣿⣷⠀\n'
          '⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿\n'
          '⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀\n'
          '⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀\n'
          '⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀\n'
          '⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀\n'
          '⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀\n'
          '⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀\n'
          '⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀\n'
          '⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀\n'
          '⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀\n'
          '⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀\n'
          '⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀\n'
          '⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n')


def welcome_msg():
    print(spacer_16)
    print(greeting)
    print(spacer_16)


# Start des eigentlichen Programm

welcome_msg()

# While-Schleife, um mehrere Passwörter generieren zu können ohne das Programm neustarten zu müssen

while True:

    # 1. Importieren von benötigten Modulen

    import random   # Zur zufälligen Auswahl von Symbolen und vermischen von Zahlen, Sonderzeichen und Buchstaben
    import string   # Vorgefertige Strings mit Buchstaben, Zahlen, Sonderzeichen
    import time     # Zeitmodul, um Timer zu nutzen (sleep)
    import pyperclip  # Zum automatischen kopieren in die Zwischenablage

    # 2. Abfrage, wieviele Zahlen, Buchstaben, Sonderzeichen der User haben möchte

    length_num = (input('\n Wieviele Zahlen soll das Passwort enthalten?'))

    if not length_num.isdecimal():
        print('\n' + spacer_8 + "\nBitte eine Zahl eingeben.\n" + spacer_8 + '\n')

    else:
        length_num = int(length_num)

        length_let = (input('\n Wieviele Buchstaben soll das Passwort enthalten?'))

        if not length_let.isdecimal():
            print('\n' + spacer_8 + "\nBitte eine Zahl eingeben.\n" + spacer_8 + '\n')

        else:
            length_let = int(length_let)

            length_sym = (input('\n Wieviele Symbole soll das Passwort enthalten?'))

            if not length_sym.isdecimal():
                print('\n' + spacer_8 + "\nBitte eine Zahl eingeben.\n" + spacer_8 + '\n')

            else:
                length_sym = int(length_sym)

        # 3. Gesamtlänge des Passworts errechnen und als integer deklarieren

            length_pw = int(length_let + length_num + length_sym)

            # 4. Definition der Zeichensätze für die obigen Abfragen

            letters = string.ascii_letters
            num = string.digits
            sym = string.punctuation

            # 5. Zufällige Auswahl an gewünschter Anzahl der Zeichen aus Abfrage
            # temp-objekte als Zwischenspeicherobjekt

            temp_num = random.sample(num, length_num)
            temp_let = random.sample(letters, length_let)
            temp_sym = random.sample(sym, length_sym)

            # 6. Zusammenführen der Zeichen in ein Objekt, um diese im nächsten Schritt
            # in zufällige Reihenfolge zu bringen

            temp = temp_num + temp_let + temp_sym

            # 7. Generierung des Passworts mit zufälliger Reihenfolge der Zeichen aus der Zusammenführung
            # sodass Zahlen, Buchstaben und Sonderzeichen gemischt sind.

            password = ''.join(random.sample(temp, length_pw))

            # 8. Simulation des Arbeitsprozesses der Erstellung

            print('  generating new Password \n ')
            loading()
            time.sleep(1)         # Timer um "Arbeit" zu simulieren

            # 9. Ausgabe des generierten Passworts

            print('Ihr generiertes Passwort lautet \n')
            print(spacer_8 + '\n\n' + password + '\n \n' + spacer_8)

        # 10. Abfrage ob PW in die Zwischenablage kopiert werden soll

        pw_copy = input('\n Möchten Sie das Passwort in die Zwischenablage kopieren? Y/N \n')

        # Wenn ja, kopieren des PW in die Zwischenablage von Windows

        if pw_copy == 'Y' or pw_copy == 'y':
            pyperclip.copy(password)
            print('In Zwischenablage kopiert')

        # Else-Anweisung entfällt, da noch eine Abfrage folgt und nichts anderes unternommen werden soll,
        # wenn nicht kopiert wird

        # 11. Abfrage, ob User noch ein Passwort generieren möchte

        new_try = input('Möchten Sie noch ein Passwort generieren? Y/N \n')

        # Wenn ja, Sprung zurück zum Anfang der While-Schleife

        if new_try == 'Y' or new_try == 'y':
            print('restructuring the time-space-coefficient\n')
            loading()
            continue

        # Wenn nein, Verabschiedung und Beendigung des Programms

        else:
            bye()
            print('Das Programm schließt sich in 4 Sekunden von alleine')
            time.sleep(4)
            break
