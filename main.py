import customtkinter as ctk
from widgets import SlidePanel

#window
window = ctk.CTk()
window.title('Grapher')
window.geometry('600x400')

#Animated widget
animated_panel = SlidePanel(window, 0, 0.3)

#Move the button when the menu is toggled
def move_btn():
    global button_x
    global isToggled
    if isToggled:
        if button_x >= 0.15:
            button_x -= 0.01
            window.after(50, move_btn)
        else:
            isToggled = False
            button.place(relx = button_x, rely = 0.1, anchor = 'center')
            return
    else:
        if button_x <= 0.3:
            button_x += 0.01
            window.after(50, move_btn)
        else:
            isToggled = True
            button.place(relx = button_x, rely = 0.1, anchor = 'center')
            return
    button.place(relx = button_x, rely = 0.1, anchor = 'center')

#Menu button
isToggled = False
button_x = 0.15
button = ctk.CTkButton(window, text='Menu', command = move_btn)
button.place(relx = button_x, rely = 0.1, anchor = 'center')

#Main loop
window.mainloop()
