import tkinter as tk
from bs4 import BeautifulSoup
import requests

miestai = ['Vilnius', 'Kaunas', 'Klaipeda', 'Siauliai', 'Alytus', 'Druskininkai', 'Panevezys']

window = tk.Tk()
# Etiketė drop listui
tk.Label(window, text="Pasirinkite miestą:").grid(row=0, column=0, padx=50, pady=50 )
# drop listas
miesto_pasirinkimas = tk.StringVar(window)

miesto_pasirinkimas.set(miestai[0])
tk.OptionMenu(window, miesto_pasirinkimas, *miestai).grid(row=0, column=1, padx=50, pady=50)

def get_weather():
    pasirinkimas = miestai.index(miesto_pasirinkimas.get())
    miestas = miestai[pasirinkimas]
    domenas = f"http://www.meteo.lt/lt/miestas?placeCode={miestai[pasirinkimas]}"
    svetaine = requests.get(domenas)
    svetaines_kodas = svetaine.text
    svetaine_2 = BeautifulSoup(svetaines_kodas, 'html.parser')
    antraste = svetaine_2.find("div", class_="forecast-day")
    gauti_duomenys = (antraste.get_text().strip())
    listas = gauti_duomenys.split()
    print(listas)
    rezultatas.config(text=f"Ataskaita:\n{listas[1]} {listas[3]}:\n"
                           f"Mieste {miestai[pasirinkimas]} yra:\n"
                           f"{listas[4]} {listas[5]} temperturos\n"
                           f"pucia {listas[6]} {listas[7]} stiprumo vejas")

# Pridėti mygtuką duomenų rezultatui atvaizduoti
tk.Button(window, text="Gauti orų rezultatą", command=get_weather).grid(row=1, column=0, columnspan=2, padx=5, pady=5 )

# Pridėti etiketę duomenų rezultatų mygtukui
rezultatas = tk.Label(window)
rezultatas.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()

