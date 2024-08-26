import tkinter #Importing the tkinter Library

#Creating the Main Window
window = tkinter.Tk()
window.title("GUi")
#These two lines create a new tkinter window and set its title to "GUi".

#define the size of the window we want, the geometry of the window
window.geometry("640x240") #This line sets the size of the window to 640x240 pixels.

#Creating and Placing the "Hello World" Message
hello_message = tkinter.Message(window, text="Hello World GUI")
hello_message.place(relx= 0.5, rely=0.5, anchor=tkinter.CENTER)
#These two lines create a new Message widget with the text "Hello World GUI" and place it in the center of the window (both horizontally and vertically). The relx and rely options specify the relative position of the widget within its parent widget (in this case, the main window)

#Creating and Placing the "Welcome" Message
welcome_message = tkinter.Message(window, text="My name is oluwapelumi")
welcome_message.place(relx= 0.5, rely= 0.7, anchor=tkinter.CENTER)
#These two lines create another Message widget with the text "My name is oluwapelumi" and place it below the "Hello World" message, also centered horizontally.

#Starting the Main Event Loop
window.mainloop()
#This line starts the main event loop of the GUI application, which waits for user interactions (such as button clicks or key presses) and updates the GUI accordingly.