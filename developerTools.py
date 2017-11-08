from Tkinter import * 
from PIL import Image, ImageTk
import Tkinter, Tkconstants, tkFileDialog
import csv
import sys
import os

class App:

    #Initialize the application
    def __init__(self, master):

        #Create the application frame
        frame = LabelFrame(master, text="Spreadsheet Configuration Generator", padx=5, pady=5, height=500)
        frame.pack(padx=10,pady=10)
        #Create a quit button   
        self.quit = Button(frame, text="Quit", fg="red", command=frame.quit)
        self.quit.pack(side=LEFT)

        #Create a button to Upload the file and generate configuration
        self.ufile = Button(frame, text="Upload File/Generate Configuration", command=self.upload)
        self.ufile.pack(side=LEFT)

    #Function triggered when upload button is pressed
    def upload(self):

        #Ask user to select a file
        file = tkFileDialog.askopenfile(initialdir = "~/",title = "Select file",filetypes = (("txt","*.txt"),("all files","*.*")))

        #Read the content in line by line
        contents = file.readlines()

        #create an array for each row in our spreadsheet
        labels_row = []
        field_type_row = []
        liquid_field_row = []   

        #Iterate through each line in the contents
        for line in contents:
            #Split the field and type out
            fields = line.split(': ')

            #Generate a label from the field name
            label = fields[0].replace('_',' ').title()
            field_type = fields[1].rstrip().lower()

            #An actual date is needed instead of the text date
            if field_type == 'date':
                field_type = '11/23/2017'
            liquid_field = '{{loop_atom.'+fields[0].rstrip()+'}}'

            #Build our rows
            labels_row.append(label)
            field_type_row.append(field_type)
            liquid_field_row.append(liquid_field)

        #Generate a csv for the template
        with open(os.path.expanduser("~/Desktop/template.csv"),"wb") as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(labels_row)
            wr.writerow(field_type_row)
            wr.writerow(liquid_field_row)

#Tkinter root widget, one exists for each program you create
root = Tk()

#Name our program
root.title("Developer Tools")

#Create an instance of the root
app = App(root)

#Runs the app in a continuous loop that listens for user input
root.mainloop()

#Destroy the app instance 
root.destroy()