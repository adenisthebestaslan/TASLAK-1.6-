# V 1.3
#1 line :)
#We're using TKK bootstrap here cuz it makes it look Professional. Not like any of my COMMENTS are professional. anyways.
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from bs4 import BeautifulSoup, Comment
from tkinter import filedialog
from div import creatediv
from add import addcontent
# max 5 files 

#Remember to put font before background
try:
    print("created")
    with open("output1.html", "r", encoding="utf-8") as file:
        print("created0")
        soup = BeautifulSoup(file, "html.parser")
        print("created1")
except FileNotFoundError:
        print("created2")
        soup = BeautifulSoup("<html><head></head><body></body></html>", "html.parser")
        print("created3")
        
        with open("output1.html", "w", encoding="utf-8") as file:
            file.write(soup.prettify())


# Create the main application window
root = ttk.Window(themename="cosmo")
root.title("Base")
root.geometry("400x300")
selectedid = None
div_ids = []
# The script for creating a div.
# creatediv = creatediv(ttk, soup, SUCCESS)
#fifty lines! :)
DIVBUTTON = ttk.Button(root, text="Create Div", bootstyle=SUCCESS, command=lambda: creatediv(ttk, soup, SUCCESS))
DIVBUTTON.pack(pady=20)

from bs4 import BeautifulSoup
import tkinter as tk
def extractdivs():
    global div_ids
    with open("output1.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        div_list = [{"class": div.get("class", []), "id": div.get("id")} for div in soup.find_all("div")]
        # Create a dropdown with div IDs
        div_ids = [div["id"] for div in div_list if div["id"]]


def seedivs():
    divinvestigation = tk.Tk()
    divinvestigation.title("See Divs")
    divinvestigation.geometry("400x300")
    global div_ids
    with open("output1.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        div_list = [{"class": div.get("class", []), "id": div.get("id")} for div in soup.find_all("div")]
        # Create a dropdown with div IDs
        div_ids = [div["id"] for div in div_list if div["id"]]
        divclass = [div["class"] for div in div_list if div["id"]]
        dropdown = ttk.Combobox(divinvestigation, values=div_ids, width=25)
        print("Extracted Div IDs:", div_ids)
        dropdown.set("Select a div :)")  # Default text
        dropdown.pack(pady=20)

        # Label to display the content of the selected div
        content_label = ttk.Label(divinvestigation, text="", wraplength=300)
        content_label.pack(pady=20)

        def showdivcontent(event):
            with open("output1.html", "r", encoding="utf-8") as file:
                src = file.read()
            soup = BeautifulSoup(src, 'html.parser')
            global selectedid
            selectedid = dropdown.get()
            print(f"Selected Div ID: {selectedid}")
            selecteddiv = soup.find("div", id=selectedid)
            print(f"Selected Div Raw: {selecteddiv}")
            if selecteddiv:   
                divcontent = selecteddiv.decode_contents().strip()  # Extract inner content
                print(f"Extracted Content: {divcontent}")
                
                if divcontent:
                    content_label.config(text=divcontent)
                else:
                    content_label.config(text="No content found in the selected div.")
            else:
                print("No div found with the slected ID.")
                content_label.config(text="No div found with the selected ID.")
        # Bind the dropdown selection change to the show_div_content function
        dropdown.bind("<<ComboboxSelected>>", showdivcontent)
#  0000000000 an army of zeros.


    button = ttk.Button(divinvestigation, text="add content", bootstyle=SUCCESS, command=lambda: addcontent(div_ids, soup, dropdown))
    button.pack(pady=20)

        


        

 #this is jerry --> :((: his mother was a :) face, and his dad was a :( face.(yes i got a little bored. lets get back to work. )

from delete import delete1, deletebodcont


extractdivs()
# Create a button to delete the selected div
print("EXtracted div ids".upper(), div_ids)#.upper() is a method that makes the string uppercase.
deletebutton = ttk.Button(root, text="Delete Div", bootstyle=SUCCESS, command=lambda: delete1(ttk, div_ids))
deletebutton.pack(pady=20)

seedivbutton = ttk.Button(root, text="See Div", bootstyle=SUCCESS, command=seedivs)

seedivbutton.pack(pady=20)

deletebodyinfd = ttk.Button(root, text="Delete body info", bootstyle=SUCCESS, command=deletebodcont)
deletebodyinfd.pack(pady=20)


#remember to keep all your varibles in lowercase
#ALWAYS REMEMBER TO READ THE CODE FULLY! DONT SKIM OVER IT. YOU MIGHT MISS SOMETHING IMPORTANT.
#ALSO, DONT EAT PAVEMENT. ITS NOT GOOD FOR YOU.
#200 lines. Jerry is at school. Mr Shocked-Face  is teaching
#                              | (::( |
#                              | _____
#                              
#                            __________
#                           |          |
#                           |  :0      |
#                           ___________
root.mainloop()
#:((:|    <--- Dont talk to Jerry. He's GROUNDED FOR EATING PAVEMENT >:( 

#150 lines.
#250 lines :D
#300 lines :D
#350 lines :D
#400 lines :3333
#450 lines
#500
#600
#:( jerrys dad is happy. sadly, he can not show it since he is permenantly a :( face.
