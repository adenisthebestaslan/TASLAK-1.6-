from bs4 import BeautifulSoup
from tkinter import ttk
def delete1(ttk, div_ids):
    print("skibdi")
    Deletewindow = ttk.Window(themename="cosmo")
    Deletewindow.title("Delete Div")
    Deletewindow.geometry("400x300")
    dropdown = ttk.Combobox(Deletewindow, values=div_ids, width=25)
    dropdown.set("Select a div to delete")  # Default text
    dropdown.pack(pady=20)

    def deletediv():
        with open("output1.html", "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        selecteddiv = dropdown.get()
        for div in soup.find_all("div", id=selecteddiv): 
            div.decompose()
        with open("output1.html", "w", encoding="utf-8") as file:
            file.write(str(soup))
        print("Deleted div with ID:", selecteddiv)
        print(soup.prettify())
    
    button = ttk.Button(Deletewindow, text="Delete", bootstyle="danger", command=deletediv)
    button.pack(pady=20)

def deletebodcont():
    with open("output1.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        body = soup.find("body")
        #It dletes the style attribute from the body tag, and then adds the new code withouth the style attribute.
        if 'style' in body.attrs:
            del body['style']
    with open("output1.html", "w", encoding="utf-8") as file:
            print(soup.prettify())
        
            file.write(soup.prettify())

    
