#wes allen
#this is all my imports
from tkinter import *
from tkinter import Tk
from tkinter.font import *
from tkinter import messagebox
import tkinter as Tkint
import os
#the main block of code itself
class RecipeBook(Frame):
	#the constructor for the frame
	def __init__(self):
		self.fp = ""
		self.mylist = os.listdir("Recipes")#this brings in the original list for my caregories
		root = Tk()
		self.font1 = Tkint.font.Font(family = "Times New Roman", size = 25)#these ate the different fonts in the program
		self.font1.configure(size=25)
		self.font2 = Tkint.font.Font(family = "Apple Chancery", size = 15)
		self.font2.configure(size=15)
		self.font3 = Tkint.font.Font(family = "Chalkduster", size = 20)
		self.font3.configure(size=20)
		Frame.__init__(self, bg = "#55aaff")#this begins the construction of the main frame
		self.master.title("My Recipe Book")
		self.master.resizable(0, 0)
		self.grid()
		
		self._buttonPane2 = Frame(self, bg = "#55aaff")#this is nested frames to old the buttons
		self._buttonPane2.grid(row = 2, column = 0, columnspan = 2)
		
		self._listPane2 = Frame(self)#this is a nested frame to hold the scrolling listbox for the categories folders
		self._listPane2.grid(row = 1, column = 0, sticky = N+S, padx = 15, pady = 5)
		self._yScroll2 = Scrollbar(self._listPane2, orient = VERTICAL)
		self._yScroll2.grid(row = 1, column = 2, sticky = N+S)
		self._theList2 = Listbox(self._listPane2, width = 20, height = 10, font = self.font2, selectmode = SINGLE, yscrollcommand = self._yScroll2.set)
		self._theList2.grid(row = 1, column = 1, sticky = N+S)
		self._yScroll2["command"] = self._theList2.yview
		self.rowconfigure(1, weight = 1)
		self._listPane2.rowconfigure(1, weight = 1)
		for title in self.mylist:#this is where i populate the listbox with my list of categories
			if not title.startswith('.'):
				self._theList2.insert(END, title)
		self._theList2.activate(0)
		self._theList2.bind("<Double-Button-1>", self._openclick)		
		
		self._listPane = Frame(self)#this is a second listbox for holdint the individual recipies from each category
		self._listPane.grid(row = 1, column = 1, sticky = N+S, padx = 0, pady = 5)
		self._yScroll = Scrollbar(self._listPane, orient = VERTICAL)
		self._yScroll.grid(row = 1, column = 2, sticky = N+S)
		self._xScroll = Scrollbar(self._listPane, orient = HORIZONTAL)
		self._xScroll.grid(row = 2, column = 1, sticky = E+W)
		self._theList = Listbox(self._listPane, width = 20, height = 10, font = self.font2, selectmode = SINGLE, yscrollcommand = self._yScroll.set)
		self._theList.grid(row = 1, column = 1, sticky = N+S)
		self._yScroll["command"] = self._theList.yview
		self._xScroll["command"] = self._theList.xview
		self.rowconfigure(1, weight = 1)
		self._listPane.rowconfigure(1, weight = 1)
		self._theList.bind("<Double-Button-1>", self._viewclick)		
		
		self._messagelabel = Label(self, font = self.font1, text = "Recipe List")#these are my headers for the categories and recipes listboses
		self._messagelabel.grid(row = 0, column = 1)
		self._messagelabel = Label(self, font = self.font1, text = "Categories")
		self._messagelabel.grid(row = 0, column = 0)
		
		self._outputArea = Text(self, wrap = WORD)#this is the main viewing area to view the recipe and also for adding new recipes
		self._outputArea.grid(row = 1, column = 4, rowspan = 2, columnspan = 2, padx = 15, pady = 5)
		self._outputArea["state"] = DISABLED
		
		self._messagevar = StringVar()#this is for the header of the recipe that holds the title of the recipe, also for the file name of a new recipe
		self._messageentry = Entry(self, textvariable = self._messagevar)
		self._messageentry.grid(row = 0, column = 4, columnspan = 1)
		self._messageentry["state"] = DISABLED
		
		self.button1 = Button(self._buttonPane2, font = self.font1, text = "View Recipe", bg = "#ff0000", padx=10, pady=0, command = self._view)#this is the button to view the recipe
		self.button1.grid(row = 0, column = 1, columnspan = 1)
		self.button1["state"] = DISABLED
		
		self.button2 = Button(self._buttonPane2, font = self.font1, text = "New Recipe", padx=10, pady=0, command = self._new)#this is the button to start a new recipe
		self.button2.grid(row = 1, column = 0, columnspan = 1)
		self.button2["state"] = DISABLED
		
		self.button3 = Button(self._buttonPane2, font = self.font1, text = "Remove Recipe", padx=10, pady=0, command = self._remove)#this is the button to delete a recipe
		self.button3.grid(row = 1, column = 1, columnspan = 1)
		self.button3["state"] = DISABLED 
		
		self.button4 = Button(self._buttonPane2, font = self.font1, text = "Open Category", padx=10, pady=0, bd=0, command = self._open)#this is the button to open the category and see the list of available recipes in that category
		self.button4.grid(row = 0, column = 0, columnspan = 1)
		
		self.button6 = Button(self._buttonPane2, font = self.font1, text = "Save", padx=10, pady=0, command = self._save)#this is the save button when creating a new recipe
		self.button6.grid(row = 2, column = 0, columnspan = 1)
		self.button6["state"] = DISABLED
		
		self.button7 = Button(self._buttonPane2, font = self.font1, text = "Cancel", padx=10, pady=0, command = self._cancel)#this is the cancle button to stop creating a new recipe
		self.button7.grid(row = 2, column = 1, columnspan = 1)
		self.button7["state"] = DISABLED
		#self._buttonPane1.config(bg = "#ff0044")
		
	def _save(self):#this is the functionality for the save button
		filename = self.fp + "/" + self._messagevar.get()
		f = open(filename, 'w')
		f.write(self._outputArea.get("1.0",END))
		f.close()
		self._theList.insert(END, self._messagevar.get())
		self._messageentry.delete(0,END)
		self._outputArea.delete("1.0",END)
		self._outputArea["state"] = DISABLED
		self._messageentry["state"] = DISABLED
		self.button1["state"] = NORMAL
		self.button2["state"] = NORMAL
		self.button3["state"] = NORMAL
		self.button6["state"] = DISABLED
		self.button7["state"] = DISABLED
		
	def _cancel(self):#this is the functionality for the cancel button
		self._messageentry.delete(0,END)
		self._outputArea.delete("1.0",END)
		self._outputArea["state"] = DISABLED
		self._messageentry["state"] = DISABLED
		self.button1["state"] = NORMAL
		self.button2["state"] = NORMAL
		self.button3["state"] = NORMAL
		self.button6["state"] = DISABLED
		self.button7["state"] = DISABLED
		
	def _openclick(self, event):#this is the functionality for the open button
		self._theList.delete(0, END)
		folder = "Recipes/" + self._theList2.get(self._theList2.curselection())
		self.mylist2 = os.listdir(folder)
		
		for title in self.mylist2:
			if not title.startswith('.'):
				self._theList.insert(END, title)
		self._theList.activate(0)
		self._listPane.update_idletasks
		self.fp = folder
		self.button1["state"] = NORMAL
		self.button2["state"] = NORMAL
		self.button3["state"] = NORMAL
		
	def _open(self):#this is the functionality for the open button
		self._theList.delete(0, END)
		if not self._theList2.curselection():
			folder = "Recipes"
		else:
			folder = "Recipes/" + self._theList2.get(self._theList2.curselection())
		self.mylist2 = os.listdir(folder)
		
		for title in self.mylist2:
			if not title.startswith('.'):
				self._theList.insert(END, title)
		self._theList.activate(0)
		self._listPane.update_idletasks
		self.fp = folder
		self.button1["state"] = NORMAL
		self.button2["state"] = NORMAL
		self.button3["state"] = NORMAL
		
		
	def _viewclick(self, event):#this is the functionality for the view recipe button
		self._messageentry["state"] = NORMAL
		self._messageentry.delete(0,END)
		self._messageentry.insert(END, self._theList.get(self._theList.curselection()))
		
		self._outputArea["state"] = NORMAL
		self._outputArea.delete("1.0",END)
		filename = self.fp + "/" + self._messagevar.get()
		f = open(filename, 'r')
		while True:
			line = f.readline()
			if line == '':
				break
			self._outputArea.insert(END, line)
		f.close()
		self._outputArea["state"] = DISABLED
		self._messageentry["state"] = DISABLED
		
	def _view(self):#this is the functionality for the view recipe button
		self._messageentry["state"] = NORMAL
		self._messageentry.delete(0,END)
		self._messageentry.insert(END, self._theList.get(self._theList.curselection()))
		
		self._outputArea["state"] = NORMAL
		self._outputArea.delete("1.0",END)
		filename = self.fp + "/" + self._messagevar.get()
		f = open(filename, 'r')
		while True:
			line = f.readline()
			if line == '':
				break
			self._outputArea.insert(END, line)
		f.close()
		self._outputArea["state"] = DISABLED
		self._messageentry["state"] = DISABLED
		
	def _new(self):#this is the functionality for the new recipe button
		self._outputArea["state"] = NORMAL
		self._messageentry["state"] = NORMAL
		self._messageentry.delete(0,END)
		self._outputArea.delete("1.0",END)
		self.button1["state"] = DISABLED
		self.button2["state"] = DISABLED
		self.button3["state"] = DISABLED
		self.button6["state"] = NORMAL
		self.button7["state"] = NORMAL
	
	def _remove(self):#this is the functionality for the remove recipe button
		eraser = Tkint.messagebox.askyesno(title = "WARNING", message = "Are You Sure You Want To Remove " + self._theList.get(self._theList.curselection()) + " ?", parent = self)#this is a pop up confirmation when deleting a recipe
		if eraser == True:
			os.remove(self.fp + "/" + self._theList.get(self._theList.curselection()))
			self._theList.delete(self._theList.curselection())
			self._outputArea["state"] = NORMAL
			self._messageentry["state"] = NORMAL
			self._messageentry.delete(0,END)
			self._outputArea.delete("1.0",END)
			self._outputArea["state"] = DISABLED
			self._messageentry["state"] = DISABLED

def main():#this is the main function where it all begins
	RecipeBook().mainloop()#this is the continuous loop that keeps the program running while its still open
main()#this is like clicking play