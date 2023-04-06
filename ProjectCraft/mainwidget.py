from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from random import *
from random import uniform
from datetime import date
from tkinter.font import Font
from simpleorehawidget import simple_Oreha_Window
from basicorehawidget import basic_Oreha_Window
from superiororehawidget import superior_Oreha_Window

bg="#3d6466"

root = Tk()
root.title('Craft Simulator')
root.iconbitmap(r'Images\sss.ico')
root.geometry('500x600')



#Create a database or connect to one
conn = sqlite3.connect(r'Craftdatabase\OrehaDataBase.db')

#Creat cursor
c = conn.cursor()

'''
#Create tables

c.execute("""CREATE TABLE SuperiorOreha (
		Day text,
		fishPrice integer,
		perlPrice integer,
		goldenFishPrice integer,
		marketPrice integer,
		chanceToDouble text,
		greatSuccesCount integer,
		profitForDay text
		)""")

c.execute("""CREATE TABLE BasicOreha (
		Day text,
		fishPrice integer,
		perlPrice integer,
		goldenFishPrice integer,
		marketPrice integer,
		chanceToDouble text,
		greatSuccesCount integer,
		profitForDay text
		)""")


c.execute("""CREATE TABLE SimpleOreha (
		Day text,
		fishPrice integer,
		perlPrice integer,
		goldenFishPrice integer,
		marketPrice integer,
		chanceToDouble text,
		greatSuccesCount integer,
		profitForDay text
		)""")


'''
conn.commit()

conn.close()

frame1 = Frame(root, width=500, height=600, bg="#3d6466")
frame1.grid(row=0,column=0)

#Define title font

titleFont = Font(
	family = "Helvetica",
	size = 42,
	weight = "bold",
	slant = "italic",
	underline=0,
	overstrike = 0
	)

#Create title label
title_Label = Label(frame1, text="Chose Oreha", font = titleFont, bg="#3d6466", fg="white")
title_Label.place(x=60,y=120)

#Create button photos
simplePhoto = PhotoImage(file ="Images/simpleoreha.png" )
basicPhoto = PhotoImage(file="Images/basicoreha.png")
superiorPhoto = PhotoImage(file="Images/superiororeha.png")

#Create buttons on frame widget
simple_Button = Button(frame1, text="Simple Oreha",command=lambda:simple_Oreha_Window() ,image = simplePhoto,compound = BOTTOM, bg="#3d6466", fg="white")
simple_Button.place(x=70,y=220)
basic_Button = Button(frame1, text="Basic Oreha", image = basicPhoto,command = lambda:basic_Oreha_Window(),compound = BOTTOM, bg="#3d6466", fg="white")
basic_Button.place(x=210,y=220)
superior_Button = Button(frame1, text="Superior Oreha", image = superiorPhoto,command =lambda:superior_Oreha_Window(),compound = BOTTOM, bg="#3d6466", fg="white")
superior_Button.place(x=350,y=220)



root.mainloop()