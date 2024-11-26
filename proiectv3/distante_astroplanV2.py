import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Dictionar cu linkuri catre informatii
planete_urls = {
    "Sun": "https://starlust.org/how-far-away-is-earth-from-the-sun/",
    "Moon": "https://starlust.org/how-far-away-is-the-moon-now/",
    "Mars": "https://starlust.org/how-far-away-is-mars-now/",
    "Mercury": "https://starlust.org/how-far-away-is-mercury-now/",
    "Venus": "https://starlust.org/how-far-away-is-venus-now/",
    "Jupiter": "https://starlust.org/how-far-away-is-jupiter-now/",
    "Saturn": "https://starlust.org/how-far-away-is-saturn-now/",
    "Uranus": "https://starlust.org/how-far-away-is-uranus-now/",
}
# Image paths for planets
planet_images = {
    "Sun": "sun.png",
    "Moon": "moon.png",
    "Mars": "mars.png",
    "Mercury": "mercury.png",
    "Venus": "venus.png",
    "Jupiter": "jupiter.png",
    "Saturn": "saturn.png",
    "Uranus": "uranus.png",
}

# Functie cautare date
def cautareDate():
    distante = {}
    for planeta, url in planete_urls.items():
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            distanta_element = soup.find('div', attrs={'class': 'elementor-shortcode'})
            if distanta_element:
                distante[planeta] = distanta_element.text.strip()
            else:
                distante[planeta] = "Distance not found"
        except requests.RequestException as e:
            distante[planeta] = f"Error: {e}"
    return distante

# Functie callback pt combobox
def arataInformatii(event):
    planetaSelectata = combobox.get()
    distanta = distante.get(planetaSelectata, "Nu s-au gasit informatii.")
    result_label.config(text=f"Distance to {planetaSelectata}: {distanta}")
        # Update the planet image
    if planetaSelectata in planet_images:
        image_path = planet_images[planetaSelectata]
        try:
            planet_image = Image.open(image_path).resize((400, 400), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(planet_image)
            planet_image_label.config(image=photo)
            planet_image_label.image = photo
        except Exception as e:
            result_label.config(text=f"Eroare la incarcarea imaginii: {e}")

def on_button_click():
    # Incarca imaginea sau afiseaza un fundal alb
    image_path = "astronaut.png" 
    try:
        img = Image.open(image_path).resize((400, 300)) 
    except FileNotFoundError:
        img = Image.new("RGB", (400, 300), color="white")  # Creaza imagine alba in caz ca nu se incarca cea aleasa
    # Display the image in a new window
    new_window = Toplevel(afisaj)
    new_window.title("Informatii proiect")
    new_window.geometry("420x400")
    #Incarcam imaginea in label si scrisul in label2
    img_tk = ImageTk.PhotoImage(img)
    label = Label(new_window, image=img_tk)
    label.image = img_tk
    label.pack()
    label2 = Label(
        new_window,
        text="Buna ziua, noi suntem Sebastian Paulenco si Munteanu George Ciprian, "
             "si am creat acest proiect pentru a demonstra utilizarea unor functii si librarii in Python.",
        wraplength=400,  # Face wrap text to window size
        justify="center",  # Aliniament
        font=("Arial", 12),  
        )
    label2.pack(pady=10)  # Adauga niste padding intre imagine si text
# GUI
afisaj = Tk()
afisaj.geometry("750x600")
afisaj.title("Distante planetare")
# cauta distantele
distante = cautareDate()
label = Label(afisaj, text="Select a celestial object to see the distance to it:", font=("Arial", 14))
label.pack(pady=10)
combobox = ttk.Combobox(afisaj, values=list(distante.keys()), state="readonly", font=("Arial", 12))
combobox.pack(pady=10)
# Asignam selectia
combobox.bind("<<ComboboxSelected>>", arataInformatii)
result_label = Label(afisaj, text="", font=("Arial", 14), fg="blue", wraplength=700, justify="center")
result_label.pack(pady=20)
# Label pt a afisa imaginea planetei
planet_image_label = Label(afisaj, bg="white")
planet_image_label.pack(pady=10)
# Mesajul preselectat
combobox.set("Selectati o planeta")

buton = Button(afisaj, text="Despre proiect", justify="left", font=("Arial", 12), command=on_button_click)
buton.place(x=10, y=10)

mainloop()
