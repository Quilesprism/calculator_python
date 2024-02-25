from tkinter import*
from math import sqrt
main = Tk()
main.title("Sapa")

view = Entry(main,font=("arian", 20, "bold"), width=18, justify="right", background="black", foreground="white")

view.pack(padx=10, pady=(10,0), ipady=10, fill=BOTH)
view.insert(0, "0")

write = Frame(main);write.pack(padx=10, pady=10)
btn= [["C", "X²", "%", "Raiz"], ["7", "8", "9", "/"], ["4", "5", "6", "X"], ["1", "2", "3", "-"], [".", "0", "=", "+"] ]

def btnPress(text):
    match text:
        case "=": 
            result = eval(view.get().replace("²", "**2"))
            view.delete(0, END)
            view.insert(0, result)
        case "C":
            view.delete(0, END)
            view.insert(0, "0")
        case "Raiz": 
            resutl = sqrt(float(view.get()))
            view.delete(0, END)
            view.insert(0, resutl)
        case _:
            if view.get() == "0":
                view.delete(0, 1)
            view.insert(END, text.replace("X²", "²".replace("x", "*")))

def funtionBtn(text): 
    return lambda:btnPress(text)

for i in range(5):
    for j in range(4):
        Button(write, width=6, height=3, background="#33C1FF", foreground="black", font=("arian", 12, "bold"),
               text=btn[i][j], command=funtionBtn(btn[i][j]), cursor="hand2").grid(row=i, column=j)

main.mainloop()