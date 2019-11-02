from pokedex import pokedex
from pprint import pprint
from PIL import Image 
import requests
from io import BytesIO
from urllib.request import urlopen



# from PIL import Image
# import requests
# url = 'https://pokeres.bastionbot.org/images/pokemon/1.png'
# Image.open(urlopen(url).read())



pokedex = pokedex.Pokedex(version='v1')
starting = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu']
pokemon = pokedex.get_pokemon_by_name(f'{starting[0]}')[0].get('sprite')


print(pokemon)


# import tkinter as tk
# from PIL import ImageTk, Image
# import os
# import requests
# from io import BytesIO
 
# root = tk.Tk()
# img_url = 'https://pokeres.bastionbot.org/images/pokemon/1.png'
# response = requests.get(img_url)
# img_data = response.content
# img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
# panel = tk.Label(root, image=img)
# panel.pack(side="bottom", fill="both", expand="yes")
# root.mainloop()