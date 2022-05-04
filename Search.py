from curses import window
import gooeypie as gp
from jmespath import search


def Next_Window(event):
    event = gp.GooeyPieApp('Next Window')


        


app = gp.GooeyPieApp('Login')

user_lbl = gp.Label(app, "Username")
user_inp = gp.Input(app)

def login(index):
    global user_inp
    username = 'Drac'
    if user_inp == username:
        Next_Window()  
    else:
        print("That is the wrong username.")
           
login_btn = gp.Button(app, 'Login', login)
status_lbl = gp.Label(app, '')

app.set_grid(4, 2)
app.add(user_lbl, 1, 1)
app.add(user_inp, 1, 2)
app.add(login_btn, 3, 2)
app.add(status_lbl, 4, 2)

app.run()