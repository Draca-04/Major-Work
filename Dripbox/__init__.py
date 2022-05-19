import random
import asyncio
import PySimpleGUI as sg
import sys
# from Dripbox.GUI import ui, create_layout
# from Dripbox.Background import Background



sg.change_look_and_feel('DarkAmber')
# This changes the background colour - for stylistic features



layout = [
[sg.Text('')],
[sg.Text('Password:'), sg.InputText(password_char='*', key ='passwod')],
[sg.Text('', key='status', size = (20, 1))],
[sg.Button('Submit'), sg.Button('Cancel')]
]
# Creates a simple layout using buttons text and setting input characters to *
# key allows a variable or module to be placed underneath 'Password'


window = sg.Window('DripBox').Layout(layout) 
# Defining the window, naming it and giving it features of the layout


async def Background():
    while True:
        rando = random.randint(2, 2000)
        window['status'].update(rando)
        await asyncio.sleep(1)
    # The feature async allows real time data to be passed into the program without threading
    # Using the rando variable to check and test the program is constantly updating
    # await prevents the program from crashing due to the program trying to do multiple things at once
    # asyncio is the import function that allows the program to run multiple methods at once



async def ui():
    while True:
        event, value  = window.read(timeout=1)
        if event in (None, 'Cancel'):
            sys.exit()
        # Collect the value inputed and record the event it passed through 


        if event != '__TIMEOUT__':
            print(f"{event} - {value}")
        await asyncio.sleep(.0001)
        # Print the event and value while working with asyncio


async def wait_list():
    await asyncio.wait(
        [Background(), ui()]
    )
    # Creating a method that calls and utilises both functions asynchronously







if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_list())
    loop.close()
    # If statement is to execute some code only if the file was run directly, and not imported
    # 'loop' provides convenient access to event loops managed by the default policy





