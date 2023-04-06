from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from random import *
from random import uniform
from datetime import date
from tkinter.font import Font
	

def basic_Oreha_Window():

	basic = Tk()
	basic.title('BasicOrehaCraftProfit')
	basic.iconbitmap(r'Images\sss.ico')
	
	frame3 = Frame(basic, width=567, height=567967, bg="#3d6466")
	frame3.grid(row=0,column=0)

	def close_Widnow():
		basic.destroy()

	#Create a database or connect to one
	conn = sqlite3.connect(r'Craftdatabase\OrehaDataBase.db')

	#Creat cursor
	c = conn.cursor()

	#query_label
	def query():
		#Create a database or connect to one
		conn = sqlite3.connect(r'Craftdatabase\OrehaDataBase.db')
		#Creat cursor
		c = conn.cursor()

		#Quary the DB
		c.execute("SELECT *, oid FROM BasicOreha")
		records = c.fetchall()
		#print(records)

		#Loop Thru Results
		print_records =''
		for record in records:
			print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2])+ " "+str(record[3])+ " " + str(record[4]) + " " + str(record[5]) + " "+ str(record[6]) + " " + str(record[7]) + " " + str(record[8])+ "\n"

		quary_label = Label(frame3, text=print_records, bg="#3d6466", fg="white")
		quary_label.grid(row=12, column=0, columnspan=2)

		#Commit Changes
		conn.commit()

		#Close Connetion
		conn.close()

	today = date.today()


	#Calculate double craft chance
	def findx():
		percentChance = int(chanceToDouble.get())
		global x
		x = 0
		for n in range (0,90):
			if round(uniform(0.01, 100.00), 2) < percentChance :
				x = x+1

				
		return x


	def calculateResoult():
		global great_succesEntry
		global x
		findx()
		great_succesEntry = Label(frame3,text=str(x), bg="#3d6466", fg="white")
		great_succesEntry.grid(row=6,column=1)
		great_succesLabel = Label(frame3, text = "Amount doubled :", bg="#3d6466", fg="white")
		great_succesLabel.grid(row=6, column=0)
		global profit
		craftcost = int((90 * int(fish_Price.get()) * 0.8 + 90 * int(goldenFish_Price.get()) * 1 + 90 * int(perl_Price.get()) * 4 + 90 * 184)) 
		sellPrice = int((90 * 30 * int(oneOreha_Price.get()))+ x * int(oneOreha_Price.get()))
		tax = sellPrice * 0.05
		profit = sellPrice - (tax + craftcost)

		global profit_entry
		profit_Label = Label(frame3, text = "Profit :", bg="#3d6466", fg="white")
		profit_Label.grid(row=8, column=0)
		profitLabel = Label(frame3,text=str(profit),bg="#3d6466", fg="white")
		profitLabel.grid(row=8,column=1)
	


	titleFont = Font(
	family = "Helvetica",
	size = 42,
	weight = "bold",
	slant = "italic",
	underline=0,
	overstrike = 0
	)
	




	
	#Create profit button	
	profitButton = Button(frame3, text="Calculate day profit",command=lambda:calculateResoult(),bg="#3d6466", fg="white")
	profitButton.grid(row=0,column=2)
	query_btn = Button(frame3, text = "Show Records", command=query, bg="#3d6466", fg="white")
	query_btn.grid(row=11, column=0,columnspan=3,pady=10,padx=10, ipadx=130)

	# Create Text Box Labels
	title_Label = Label(frame3, text="Basic Oreha Craft Profit", font = titleFont, bg="#3d6466", fg="white")
	title_Label.grid(row=0,column= 1)
	fish_PriceLabel = Label(frame3, text="Fish Price", bg="#3d6466", fg="white")
	fish_PriceLabel.grid(row=1,column=0,pady=(10,0))
	perl_PriceLabel = Label(frame3, text="Pearl Price", bg="#3d6466", fg="white")
	perl_PriceLabel.grid(row=2,column=0)
	goldenFish_PriceLabel = Label(frame3, text="Golden Fish Price", bg="#3d6466", fg="white")
	goldenFish_PriceLabel.grid(row=3,column=0)
	oneOreha_PriceLabel = Label(frame3, text="Oreha Price", bg="#3d6466", fg="white")
	oneOreha_PriceLabel.grid(row=4,column=0)
	chanceToDoubleLabel = Label(frame3, text="Your chance to double", bg="#3d6466", fg="white")
	chanceToDoubleLabel.grid(row=5,column=0)
	daylabel = Label(frame3, text ="Date: ", bg="#3d6466", fg="white")
	daylabel.grid(row=7, column=0)
	dayTimelabel = Label(frame3, text = today, bg="#3d6466", fg="white")
	dayTimelabel.grid(row=7, column=1)

	#delete_box_label = Label(frame3, text = "Select ID ", bg="#3d6466", fg="white")
	#delete_box_label.grid(row=10, column=0,pady=5)
	

	# Create Text Boxes
	fish_Price = Entry(frame3, width=30, bg="#3d6466", fg="white")
	fish_Price.grid(row=1,column=1, padx=20, pady=(10,0))
	perl_Price = Entry(frame3, width=30, bg="#3d6466", fg="white")
	perl_Price.grid(row=2,column=1)
	goldenFish_Price = Entry(frame3, width=30, bg="#3d6466", fg="white")
	goldenFish_Price.grid(row=3,column=1)
	oneOreha_Price = Entry(frame3, width=30,bg="#3d6466", fg="white")
	oneOreha_Price.grid(row=4,column=1)
	chanceToDouble = Entry(frame3,width=30, bg="#3d6466", fg="white")
	chanceToDouble.grid(row=5,column=1)


	def savePrices():
		#Create a database or connect to one
		conn = sqlite3.connect('CraftDataBase/OrehaDataBase.db')

		#Creat cursor
		c = conn.cursor()

		#Insert Into Table
		c.execute("INSERT INTO BasicOreha VALUES(:Day, :fishPrice, :perlPrice, :goldenFishPrice, :marketPrice, :chanceToDouble, :greatSuccesCount, :profitForDay)",
			{
				'Day':today,
				'fishPrice':fish_Price.get(),
				'perlPrice':perl_Price.get(),
				'goldenFishPrice':goldenFish_Price.get(),
				'marketPrice':oneOreha_Price.get(),
				'chanceToDouble':chanceToDouble.get(),
				'greatSuccesCount':str(x),
				'profitForDay':profit

			}
		)

		#Commit Changes
		conn.commit()

		#Close Connetion
		conn.close()
	
	#Commit Changes
	
	save_Button = Button(frame3, text="Save the results to the database", command=savePrices, bg="#3d6466", fg="white")
	save_Button.grid(row=0,column=0)
	exit_Button = Button(frame3, text="Close this window", command = lambda:close_Widnow(),bg="#3d6466", fg="white")
	exit_Button.grid(row=13, column=0, columnspan=3)
	
	#Close Connetion
	conn.commit()
	conn.close()
	basic.mainloop()