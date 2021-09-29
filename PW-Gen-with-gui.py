# Importieren benötigter Funktionen und "Tools"

import random
import string
import pyperclip
import PySimpleGUI as sg

sg.theme("Darkblue")        # Farbschema des Fensters

# Definition der benötigten Elemente und des Aussehens des Fensters

layout = [[sg.Text("Le Passwort-Generator ", font=("Helvetica", 25, "bold"))],
          # oben Titeltext im GUI
          # unten Erstellen von Eingabefeldern für Usereingabe
          [sg.Text("Anzahl Buchstaben (max 10)", key='Output-Let', font=("Helvetica", 10, "bold"))],
          [sg.Spin([i for i in range(0, 11)], initial_value=4,
                   size=(25, 4), key='Input-Let')],
          [sg.Text("Anzahl Zahlen (max 10)", key='Output-Num', font=("Helvetica", 10, "bold"))],
          [sg.Spin([i for i in range(0, 11)], initial_value=4,
                   size=(25, 4), key='Input-Num')],
          [sg.Text("Anzahl Sonderzeichen (max 10)", key='Output-Sym', font=("Helvetica", 10, "bold"))],
          [sg.Spin([i for i in range(0, 11)], initial_value=4,
                   size=(25, 4), key='Input-Sym')],
          [sg.Text("Hier steht gleich das Passwort", size=(40, 1), key='Output', font=("Helvetica", 25, "bold"))],
          [sg.Button('Generieren', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold")),
           sg.Button('Kopieren', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold")
                     ), sg.Button('Beenden', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold"))]]

window = sg.Window('Dezzys Passwort Generator', layout)

# Definition der Funktionen, die angesprochen werden, wenn man auf der GUI was betätigt
while True:
    event, values = window.read()

    if event == 'Generieren':                 # Definition was passiert, wenn auf "Generieren" gedrückt wird
        useriptlet = values['Input-Let']      # Auslesen der Eingabe im Feld für Buchstaben
        letters = string.ascii_letters        # Zeichensatzbestimmung für Buchstaben
        useriptnum = values['Input-Num']      # Auslesen der Eingabe im Feld für Zahlen
        num = string.digits                   # Zeichensatzbestimmung für Zahlen
        useriptsym = values['Input-Sym']      # Auslesen der Eingabe im Feld für Sonderzeichen
        symbols = string.punctuation          # Zeichensatzbestimmung für Sonderzeichen/Symbole
        let_temp = random.sample(letters, useriptlet)   # Zufälliges Wählen von gewünschter Anzahl an Buchstaben
        num_temp = random.sample(num, useriptnum)       # Zufälliges Wählen von gewünschter Anzahl an Zahlen
        sym_temp = random.sample(symbols, useriptsym)   # Zufälliges Wählen von gewünschter Anzahl an Sonderzeichen
        temp_all = let_temp + num_temp + sym_temp       # Zusammenfügen der Bestandteile (Zeichenweitergabe)
        length = useriptsym + useriptnum + useriptlet   # Bestimmung genauer Passwortlänge
        temp = random.sample(temp_all, length)          # Generierung zufälliger Reihenfolge der übergebenen Zeichen
        password = "".join(temp)              # Definition des Passworts als auslesbaren Operator
        # sg.popup(password)                    # Popup mit generiertem Passwort, momentan ausgeblendet
        window['Output'].update(password)     # Update des unsichtbaren "Output"-Feldes auf dem GUI (PW wird angezeigt)

        window["Input-Let"].update("4")       # Zurücksetzen der Input-Felder auf Standartwerte
        window["Input-Num"].update("4")       # Zurücksetzen der Input-Felder auf Standartwerte
        window["Input-Sym"].update("4")       # Zurücksetzen der Input-Felder auf Standartwerte

    if event == "Kopieren":             # Definition was passiert, wenn auf Kopieren gedrückt wird
        op = window['Output'].get()     # Auslesen des Passworts aus dem Output Feld
        pyperclip.copy(op)              # Kopieren in die Zwischenablage
        sg.popup("Erfolgreich kopiert")   # Feedback an den User, das PW kopiert wurde

    # Beenden des PW generator durch (X) oder "Beenden"-Schaltfläche
    if event == sg.WINDOW_CLOSED or event == 'Beenden':
        break


window.close()
