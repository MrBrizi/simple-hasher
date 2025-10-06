from tkinter import *
from argon2 import PasswordHasher

global_outcome = "" 

#generate hash out of the input text
def hasher():
    global global_outcome

    hash_entry = input_entry.get()
    #print(hash_entry)


    ph = PasswordHasher()

    outcome = ph.hash(hash_entry)
    global_outcome = outcome
    hash_label.config(text="Dein Hash: " + outcome)
    copy_button.config(state=NORMAL) 


def copy_hash():

    copy_value = global_outcome 
    print(copy_value)

    copy=copy_value
    #print(copy)
    root.clipboard_clear()
    root.clipboard_append(copy)
#master gui

root = Tk()
root.title("Argon2 Hash-Ersteller")
root.config(bg="#f0f0f0") # Etwas helleres Grau für Hintergrund
# Fenstergröße flexibel halten
root.geometry("600x300")
root.resizable(False, False)


# 1. Eingabefeld
input_entry = Entry(root, width=80, font=('Arial', 12))
input_entry.pack(pady=20, padx=20, fill=X) # Füllt die gesamte Breite


# 2. Frame für Buttons (Packen der Buttons nebeneinander)
button_frame = Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

# Enter Button
button = Button(button_frame, text="HASH ERSTELLEN", command=hasher, 
                bg="#4CAF50", fg="white", font=('Arial', 10, 'bold'), padx=10)
button.pack(side=LEFT, padx=10)

# Kopier Button
copy_button = Button(button_frame, text="HASH KOPIEREN", command=copy_hash, 
                     bg="#2196F3", fg="white", font=('Arial', 10, 'bold'), padx=10, 
                     state=DISABLED) # Anfangs deaktiviert
copy_button.pack(side=LEFT, padx=10)

# Cancel Button
button2 = Button(button_frame, text="BEENDEN", command=root.destroy, 
                 bg="#f44336", fg="white", font=('Arial', 10, 'bold'), padx=10)
button2.pack(side=LEFT, padx=10)


# 3. Hash-Ausgabe-Label
hash_label = Label(root, text="HASH_DISPLAY_TEXT", 
                   bg="#fff", fg="#333", justify=LEFT, anchor="nw",
                   wraplength=560, relief=GROOVE, bd=2, font=('Consolas', 10))
hash_label.pack(pady=15, padx=20, fill=X, ipady=10) # ipady für Innen-Padding

root.mainloop()