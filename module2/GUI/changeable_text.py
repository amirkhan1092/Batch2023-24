from tkinter import *

count = 0 # Click counter
def buttonPushed():
    global myText
    global count
    count += 1
    myText.set(f"Stop your clicking, it's already been {count} times!")
#Creating a label you can change
def addTextLabel(root):
    global myText
    myText = StringVar()
    myText.set("")
    myLabel = Label(root, textvariable=myText)
    myLabel.pack()
def main():
    global root
    root = Tk() # Create the root (base) window where all widgets go 
    myButton = Button(root, text="Show Text",command=buttonPushed) 
    myButton.pack()
    addTextLabel(root)
    root.mainloop() # Start the event loop
# Set the text in the label
#     (call set method with a string actual parameter)
#     Create a StringVar to hold text
#     Link the label to the StringVar
main()