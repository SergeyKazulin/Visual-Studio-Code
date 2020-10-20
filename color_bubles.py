from tkinter import *
from random import *
def exit_ (event):
    if event.keysym == 'space':
        MyWindow.destroy()

MyWindow = Tk()
#MyWindow.overrideredirect(1) # убираем заголовок окна
#MyWindow.state('zoomed')
MyWindow.title("BUBLE")
size = 800

buble = Canvas(MyWindow,  width=size, height=size)
buble.pack()
diapason = 0

while diapason >= 0:                   # diapason < 1000:
    colors = choice(
        ['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', 'pink', 'purple', 'red', 'yellow', 'violet', 'indigo',
         'chartreuse', 'lime', ''])
    x0 = randint(-size / 10, size)
    y0 = randint(-size / 10, size)
    d = randint(0, size / 5)
    MyWindow.update()
    diapason += 1
    buble.create_oval(x0 * 1.2, y0 * 1.2, d,  d, fill=colors)


MyWindow.bind_all('<space>', exit_)

MyWindow.mainloop()