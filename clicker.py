import tkinter as tk

root = tk.Tk() #Tworzenie okna

root.title("Bomb Clicker")
root.geometry("950x700")
root.iconbitmap("roblox.ico")
root.resizable(False, False)

bomb = 100
score = 0
pres_return = True

label = tk.Label(root, text="Press [enter] to start the game", font = ("Impact", 22))
label.pack()

fuse_label = tk.Label(root, text = f"Timer: {str(bomb)}", font = ("Impact", 20))
fuse_label.pack()

score_label = tk.Label(root, text = f"Score: {str(score)}", font = ("Impact", 20))
score_label.pack()

img_1 = tk.PhotoImage(file = "img_1.png").subsample(2, 2)
img_2 = tk.PhotoImage(file = "img_2.png").subsample(2, 2)
img_3 = tk.PhotoImage(file = "img_3.png").subsample(2, 2)
img_4 = tk.PhotoImage(file = "img_4.png").subsample(2, 2)

bomb_label = tk.Label(image = img_1,)
bomb_label.pack()

def update_display():
    pass

def is_alive():
    pass

def update_bomb():
    pass

def update_score():
    pass

def start(event):
    global press_return
    if not press_return:
        pass
    else:
        update_bomb()
        update_score()
        update_display()
        label.config(text = "")
        press_return = False
        

def click():
    pass

click_buttom = tk.Button(root, text = "Click me", bg = "black", fg = "white", font =  ("Impact", 22), width = 23, command = click)
click_buttom.pack()

root.mainloop()
