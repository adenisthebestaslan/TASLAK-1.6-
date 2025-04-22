import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS
from bs4 import BeautifulSoup, Comment
from tkinter import filedialog
#remove later

#f
def position(div_ids,soup):

    # Create a new window for positioning
    positionwindow = ttk.Window(themename="cosmo")
    positionwindow.title("Positioning")
    positionwindow.geometry("400x300")
    
    dropdowncontent1 = ttk.Combobox(positionwindow, values=div_ids, width=25)
    dropdowncontent1.set("images.")  # Default text
    dropdowncontent1.pack(pady=20)
    # Create a label and entry for the div ID
    # Create a label and entry for the new position
    newpositionlabel = ttk.Label(positionwindow, text="top:")
    newpositionlabel.pack(pady=10)
    newpositionentry = ttk.Entry(positionwindow, width=30)
    newpositionentry.pack(pady=10)    
    
    newpositionlabel1 = ttk.Label(positionwindow, text="bottom")
    newpositionlabel1.pack(pady=10)
    newpositionentrybottom = ttk.Entry(positionwindow, width=30)
    newpositionentrybottom.pack(pady=10)    

    newpositionlabel2 = ttk.Label(positionwindow, text="lrft")
    newpositionlabel2.pack(pady=10)
    newpositionentryleft = ttk.Entry(positionwindow, width=30)
    newpositionentryleft.pack(pady=10)   

    newpositionlabel3 = ttk.Label(positionwindow, text="right")
    newpositionlabel3.pack(pady=10)
    newpositionentryright = ttk.Entry(positionwindow, width=30)
    newpositionentryright.pack(pady=10)   
    def postiondiv():
        # Get the selected div ID and new position from the entries
        selecteddivid = dropdowncontent1.get()
        newposition = newpositionentry.get()
        newpositionbottom = newpositionentrybottom.get()
        newpositionleft = newpositionentryleft.get()
        newpositionright = newpositionentryright.get()
        
        # Find the div with the selected ID and update its position
        div_to_update = soup.find("div", id=selecteddivid)
        print(f"Selected Div ID: {selecteddivid}")
        print(f"Selected Div ID: {div_to_update}")
        if div_to_update:
            div_to_update["style"] = f"position: absolute; top: {newposition}; bottom: {newpositionbottom}; left: {newpositionleft}; right: {newpositionright};"
            print(f"Updated position of div with ID '{selecteddivid}' to '{newposition}'")
            
            # Save the updated HTML to the file
            with open("output1.html", "w", encoding="utf-8") as file:
                file.write(soup.prettify())
                print("Updated HTML saved to output1.html")
    editposStyle= ttk.Button(positionwindow, text="positon Div", bootstyle=SUCCESS, command=postiondiv)
    editposStyle.pack(pady=20)

    positionwindow.mainloop()
