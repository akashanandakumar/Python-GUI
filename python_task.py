from tkinter import *
import sqlite3




window = Tk()
window.title("Simple Journey Fare Calculator")
window.geometry("1000x500")


with sqlite3.connect("TravelPrice.db") as db:
    cursor = db.cursor()

# SAVE BUTTON
def save_button():
    
    # CREATE TABLE FOR AGE AND PRICE
    cursor.execute("""CREATE TABLE IF NOT EXISTS Ages(age int, price int);""")

    age = int(entrybox1.get())

    if age <= 2:
        price = 0
    elif 3 <= age <= 12:
        price = 7
    elif age >= 66:
        price = 13
    else:
        price = 18

    # INSERTING AGE AND PRICE VALUES
    cursor.execute("""INSERT INTO Ages(age,price) VALUES(?,?)""",(age,price))
    db.commit()
    entrybox1.delete(0,END)
    

# CLEAR BUTTON
def clear_button():

    textbox1['text'] = ''
    textbox2['text'] = ''
    textbox3['text'] = ''
    cursor.execute("DROP TABLE Ages")

    
# DISPLAYING AGE
def display_age():

    cursor.execute("SELECT * FROM Ages")
    display_age = ''
    
    # LOOPING TO DISPLAY THE AGE FROM DATABASE
    for age_number in cursor.fetchall():
        display_age = display_age + str(age_number[0]) + '\n'
    textbox2['text'] = display_age

    db.commit()


# DISPLAYING PRICE
def display_price():

    cursor.execute("SELECT * FROM Ages")
    display_price = ''

    for price_value in cursor.fetchall():
        display_price = display_price + str(price_value[1]) + '\n'
    textbox3['text'] = display_price

    db.commit()


# DISPLAYING COST
def display_cost():
    cursor.execute("SELECT * FROM Ages")
    total_cost = 0
    for each_price in cursor.fetchall():
        total_cost = total_cost + int(each_price[1])
    textbox4['text'] = str(total_cost)
    db.commit()




# INPUT BOX
entrybox1 = Entry(text = "") # Enter the input
entrybox1.place(x = 245, y = 30, width = 250, height = 25) 

label1 = Label(text = "Enter the client's age, one at a time ")
label1.place(x = 40, y = 30)

label2 = Label(text = "Client's age in years:")
label2.place(x = 220, y = 170)


label3 = Label(text = "Price per client £: ")
label3.place(x = 600, y = 170)

label4 = Label(text = "Display total cost for the journey:")
label4.place(x = 220, y = 370)



# BUTTONS FOR ALL FUNCTIONS
button1 = Button(text = "Save Age", command = save_button)
button1.place(x = 250, y = 100, width = 80, height = 30)

button2 = Button(text = "Clear All", command = clear_button)
button2.place(x = 380, y = 100, width = 80, height = 30)


button3 = Button(text = "Display Age", command = display_age)
button3.place(x = 70, y = 250, width = 130, height = 35)


button4 = Button(text = "Display ticket price", command = display_price)
button4.place(x = 430, y = 250, width = 150, height = 35)


button5 = Button(text = "Display Cost £", command = display_cost)
button5.place(x = 70, y = 410, width = 120, height = 35)




#textboxes for all messages


textbox1 = Label(text='')
textbox1 ["anchor"] ="nw"
textbox1 ["justify"] = "left"
textbox1.place(x = 220, y = 200, width = 120, height = 150)

textbox2 = Label(text='')
textbox2 ["anchor"] ="nw"
textbox2 ["justify"] = "left"
textbox2.place(x = 220, y = 200, width = 110, height = 150)
textbox2["bg"] = "white"
textbox2["relief"] = "sunken"
 
textbox3 = Label(text='')
textbox3 ["anchor"] ="nw"
textbox3 ["justify"] = "left"
textbox3.place(x = 600, y = 200, width = 110, height = 150)
textbox3["bg"] = "white"
textbox3["relief"] = "sunken"


textbox4 = Label(text='')
textbox4 ["anchor"] ="nw"
textbox4 ["justify"] = "left"
textbox4.place(x = 220, y = 400, width = 300, height = 70)
textbox4["bg"] = "white"
textbox4["relief"] = "sunken"



window.mainloop()

db.close()