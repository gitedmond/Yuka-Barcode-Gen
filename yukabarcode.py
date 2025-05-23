import requests
from bs4 import BeautifulSoup
import barcode
from barcode.writer import ImageWriter
from PIL import ImageTk, Image
import io
import tkinter as tk
from tkinter import messagebox

EAN = barcode.get_barcode_class('code128')

def generate_barcode():
    url = url_entry.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    divs = soup.find_all('div')
    upc_number = None
    for div in divs:
        b = div.find('b')
        if b and 'UPC' in b.get_text():
            upc_number = str(div.contents[-2]).strip()  # Extract the UPC number
            break

    if upc_number is not None:
        ean = EAN(upc_number, writer=ImageWriter())
        
        barcode_data = io.BytesIO()
        ean.write(barcode_data)
        barcode_data.seek(0)
        
        barcode_image = ImageTk.PhotoImage(Image.open(barcode_data))
        
        barcode_label.config(image=barcode_image)
        barcode_label.image = barcode_image

        messagebox.showinfo("Success", "Barcode generated successfully")
    else:
        print("UPC number not found")

window = tk.Tk()
url_entry = tk.Entry(window)
url_entry.pack()

generate_button = tk.Button(window, text="Generate Barcode", command=generate_barcode)
generate_button.pack()

barcode_label = tk.Label(window)
barcode_label.pack()

window.mainloop()
