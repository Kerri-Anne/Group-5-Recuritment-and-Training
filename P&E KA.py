from tkinter import *
import os
import webbrowser
import sqlite3

conn = sqlite3.connect('user.db')
c = conn.cursor()

#c.execute("""CREATE TABLE people3 (
#ID INTEGER,
#first_name text,
#last_name text,
#company_name text,
#HouseNo INTEGER,
#StreetName text,
#city text,
#county text,
#Zip INTEGER,
#email text       )""")
#c.execute("INSERT INTO people1 VALUES (1001, 'James', 'Butt', 'Ufix limited',6649,'N Blue Gum St','New Orleans', 'Orleans', 70116, 'jbutt@gmail.com')")
#c.execute("SELECT * FROM user WHERE user_name = 'KA'")

#c.execute("INSERT INTO user VALUES ('kerri', 'pass')")

conn.commit()
conn.close()


def database():
    pass
    #db =
   # if username1 == db.name:
       # file1 = open(username1, "r")
        # print("login success")
        # logged()
        #verify = file1.read().splitlines()
        #if password1 in verify:
          #  logged()
        #else:
         #   password_not_recognised()
    #else:
      #  user_not_found()

def agree():
    myLabel = Label(register_screen, text=var.get()).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(main_screen, text="Registration complete").pack()
   # register_user.destroy()


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.geometry("300x250")
    register_screen.title('Register')

    global username
    global password
    global username_entry
    global password_entry
    global var
    var = IntVar()

    username = StringVar()
    password = StringVar()

    Label(register_screen, text='Please enter details below: ').pack()
    Label(register_screen, text='Username').pack(pady=10)
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    Label(register_screen, text='Password').pack(pady=10)
    password_entry = Entry(register_screen, textvariable=password)
    password_entry.pack()
    Label(register_screen, text='').pack(pady=10)

    Button(register_screen, text="Terms", fg="blue", width="20", height=1,command=open_terms).pack(pady=5, padx=5)
    Checkbutton(register_screen, text="I agree", fg="blue", width="20", height=1).pack()
    Button(register_screen, text="Register", width=10, height=2, command=register_user).pack()


def login_admin_verify():
    print("Working...")
    username1 = username_verify.get()
    password1 = password_verify.get()
    #username1 = "Kerri"
    #password1 = "pass"

    global username_entry1
    global password_entry1

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 == list_of_files:
        file1 = open(username1, "r")
            #print("login success")
            #logged()
        verify = file1.read().splitlines()
        if password1 in verify:
            logged()
        else:
            password_not_recognised()
    else:
        user_not_found()
    '''
     if username1 == "Kerri":
        if password1 == "pass":
            print("login success")
            logged()
        else:
            print("password has not been recognised")
    else:
        print("User not found!")
    '''

# in list_of_files
#file1 = open(username1, "r")
       # verify = file1.read().splitlines()


def logged():
    print("Working")
    logged_screen = Toplevel(main_screen)
    logged_screen.title("Admin")
    logged_screen.geometry("300x250")
    Label(logged_screen, text="You may view applications, see what training there is, see who's on training").pack()
    Label(logged_screen, text="").pack()
    Button(text="OK", command=logged_screen.destory())


def password_not_recognised():
    print("Working")


def user_not_found():
    print("Working")


def login_admin():
    global login_admin_screen
    login_admin_screen = Toplevel(main_screen)
    login_admin_screen.title("Admin Login")
    login_admin_screen.geometry("300x250")
    Label(register_screen, text="Please enter your login details").pack()
    Label(register_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()



    Label(register_screen, text="Username:").pack(pady=10)
    user_entry1 = Entry(register_screen, textvariable=username_verify)
    user_entry1.pack()

    Label(login_admin_screen, text="Password:").pack(pady=10)
    pass_entry1 = Entry(login_admin_screen, textvariable=password_verify)
    pass_entry1.pack()
    Label(login_admin_screen, text="").pack()

    Button(login_admin_screen, text="Admin Login", width=10, height=2, command=login_admin_verify).pack()


def guest_logged():
    guest_logged_screen = Toplevel()
    guest_logged_screen.title("Guest")
    guest_logged_screen.geometry("300x250")
    Label(guest_logged_screen, text="You may take an interview, math test, English test").pack()
    Label(guest_logged_screen, text="").pack()


def login_guest_verify():
    print("Working...")
    #username2 = username_verify2.get()
    #password2 = password_verify2.get()

    username3 = "guest"
    password3 = "pass"

    #username_entry2.delete(0, END)
    #password_entry2.delete(0, END)

    #list_of_files = os.listdir()
    '''
    list_of_files = os.listdir()
     if username2 in list_of_files:
        file2 = open(username2, "r")
        verify = file2.read().splitlines()
        if password2 in verify:
            print("login success")
        else:
            print("password has not been recognised")
    else:
        print("User not found!")
    '''
    if username3 == "guest":
        if password3 == "pass":
            print("login success")
            guest_logged()
        else:
            print("password has not been recognised")
    else:
        print("User not found!")


def login_guest():
    login_guest_screen = Toplevel(main_screen)
    login_guest_screen.title("Guest Login")
    login_guest_screen.geometry("300x250")
    Label(login_guest_screen, text="Please enter your login details").pack()
    Label(login_guest_screen, text="").pack()

    global username_verify2
    global password_verify2

    username_verify2 = StringVar()
    password_verify2 = StringVar()

    global username_entry2
    global password_entry2

    Label(login_guest_screen, text="Username:").pack(pady=10)
    user_entry2 = Entry(login_guest_screen, textvariable=username_verify2)
    user_entry2.pack()

    Label(login_guest_screen, text="Password:").pack(pady=10)
    pass_entry2 = Entry(login_guest_screen, textvariable=password_verify2)
    pass_entry2.pack()
    Label(login_guest_screen, text="").pack()



    Button(login_guest_screen, text="Terms", fg="blue", width="20", height=1, command=open_terms).pack(pady=5, padx=5)
    Checkbutton(login_guest_screen, text="I agree", fg="blue", width="20", height=1).pack(pady=5, padx=5)


    Button(login_guest_screen, text="Guest Login", width=10, height=2, command=login_guest_verify).pack()


def open_terms():
    webbrowser.open("file:///C:/Users/kerri/Downloads/Terms%20and%20Conditions.pdf")




def main_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title('Welcome!')

    Label(main_screen, text='Please login in to admin if your an administrator otherwise login as a guest!', bg="light blue", width="200", height=1, font=("Cambria Math", 10)) .pack(pady=10)
    Button(main_screen, text="Admin Login", width="20", height=1, command=login_admin).pack(pady = 5, padx = 5)
    Button(main_screen, text="Guest Login", width="20", height=1, command=login_guest).pack(pady = 5, padx = 5)
    Button(main_screen, text="Register", width="20", height=1, command=register).pack(pady = 5, padx = 5)


    t5menu_bar = Menu(main_screen)
    main_screen.config(menu=t5menu_bar)
    file = Menu(t5menu_bar)

    t5menu_bar.add_cascade(menu=file, label='File')

    main_screen.mainloop()


main_screen()