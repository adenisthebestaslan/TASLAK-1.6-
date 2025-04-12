def creatediv(ttk, soup, status):
    # Sets up the window
    divsetup = ttk.Window(themename="cosmo")
    divsetup.title("Create Div")
    divsetup.geometry("400x300")

    # Class entry box
    textboxClassDiv = ttk.Entry(divsetup)
    textboxClassDiv.pack(pady=20)
    # ID entry box
    textboxDivID = ttk.Entry(divsetup)
    textboxDivID.pack(pady=20)
    
    # Function to create the div
    def makediv():
        print("starting Makediv")

        # Read the existing content of the file

        # Create the "div" tag
        div_tag = soup.new_tag("div")
        print(div_tag)
        DivClass = textboxClassDiv.get()
        print(DivClass)
        DivID = textboxDivID.get()
        print(DivID)
        div_tag["class"] = DivClass
        print("added class")
        div_tag["id"] = DivID
        print("added id")
        print("soup".upper(), soup)
        soup.body.append(div_tag)
        
        with open("output1.html", "w", encoding="utf-8") as file:
            print("opening file")
            file.write(soup.prettify())
            print("writing file")
        # Save the updated HTML to the file

        
        # Print the HTML to the console
        print(soup.prettify())

    button = ttk.Button(divsetup, text="Submit", bootstyle=status, command=makediv)
    button.pack(pady=20)
