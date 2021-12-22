from tkinter import *
from functools import partial
from PIL import ImageTk, Image
import excel_populate
#import gui

window = Tk()
window.withdraw()
loginWindow = Toplevel(window)
loginWindow.geometry('200x150')
loginWindow.title('Login Form')

if __name__ == '__main__':              #runs script when called in main
    loginWindow.mainloop()

valid_users = ['Test', 'Michael', 'User', 'DanSmith']
valid_pass = ['Test1', 'Gass', 'Pass', '12345']
valid = False

def validateLogin(username, password):
    print("username entered: ", username.get())
    print("password entered: ", password.get())
    user = username.get()
    pass_ent = password.get()
    if user in valid_users:
        user_index = valid_users.index(user)
        pass_test = valid_pass[user_index]
        if pass_test == pass_ent:
            print('Valid!')
            loginWindow.withdraw()
            loginWindow.destroy()
            #mainWindow()
            #gui.mainloop()
            valid == True
    else:
        invalidWindow = Toplevel(window)
        invalidWindow.geometry('200x50')
        loginWindow.title('Invalid Login')
        invalid = Label(invalidWindow, text = 'Invalid credentials, please try again').grid(row=2, column=0)
        print('invalid user or pass')
    return valid

loginTitle = Label(loginWindow, text ='Welcome. \n Please login').grid(row=0, column=1)
usernameLabel = Label(loginWindow, text='User Name').grid(row=1, column = 0)
username = StringVar()
usernameEntry = Entry(loginWindow, textvariable=username).grid(row=1, column = 1)
passwordLabel = Label(loginWindow, text='Password').grid(row=2, column=0)
password = StringVar()
passwordEntry = Entry(loginWindow, textvariable = password, show='*').grid(row=2, column=1)
validateLogin = partial(validateLogin, username, password)
loginButton = Button(loginWindow, text="Login", command=validateLogin).grid(row=3, column = 1)