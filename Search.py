from curses import window
import gooeypie as gp
from jmespath import search


app = gp.GooeyPieApp('Login')
next_window = gp.Window(app,'Next Window')
next_window.set_size(400,500)

        

user_lbl = gp.Label(app, "Username")
user_inp = gp.Input(app)

def login(event):
    user = user_inp.text
    username = {
    "Paul": ("PB", "11.9", "SB", "12.1"),
    "Jordan": ("PB", "14.5", "SB", "15.1")
    }
    if user in username:
        print("Athlete found")
        next_window.show()
    else:
        print("Athlete not found")
           
login_btn = gp.Button(app, 'Login', login)
status_lbl = gp.Label(app, '')

app.set_grid(4, 2)
app.add(user_lbl, 1, 1)
app.add(user_inp, 1, 2)
app.add(login_btn, 3, 2)
app.add(status_lbl, 4, 2)

app.run()