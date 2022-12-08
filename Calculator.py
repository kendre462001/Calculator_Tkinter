from tkinter import *


def click(event):
    global strvar
    # print("It\'s working !!!...")

    # cget is used to getting a value from widget property like text what the bg colour etx
    t = event.widget.cget("text")
    if t == "=":
        if strvar.get().isdigit():
            value = input1.get()
            value = int(value)
        else:
            try:

                value = eval(input1.get())
            except Exception as e:
                value = "Error"
        strvar.set(value)
        input1.update()
    elif t == "<x":
        temp = strvar.get()
        if temp == "":
            pass
        else:
            value = ""
            for i in range(len(temp)-1):
                value += temp[i]
            strvar.set(value)
            input1.update()
    elif t == "C":
        strvar.set("")
        input1.update()
    else:
        strvar.set(strvar.get()+t)
        input1.update()


root = Tk()

# root.geometry("401x495")
root.maxsize(401,495)
# print(root.winfo_screenheight())
# print(root.winfo_screenwidth())
root.title("Calculator")


strvar = StringVar()
strvar.set("")

input1 = Entry(root, textvariable=strvar, font="lucida 20 bold")
input1.pack(fill=X, padx=10, pady=10, ipadx=8)
list1 = ['9', '8', '7', '+', '6', '5', '4', '-',
         '3', '2', '1', '*', '<x', '0', '=', "C"]
i = 0
while i < len(list1)-1:

    f = Frame(root)
    if list1[i]=="6":
        b1 = Button(f, text=f"{list1[i]}", padx=28, pady=28, font="lucida 20 bold")
        b1.pack(side=LEFT)
        b1.bind("<Button-1>", click)
    else:

        b1 = Button(f, text=f"{list1[i]}", padx=28, pady=28, font="lucida 20 bold")
        b1.pack(side=LEFT)
        b1.bind("<Button-1>", click)
    b1 = Button(f, text=f"{list1[i+1]}", padx=28,
                pady=28, font="lucida 20 bold")
    b1.pack(side=LEFT)
    b1.bind("<Button-1>", click)
    b1 = Button(f, text=f"{list1[i+2]}", padx=28,
                pady=28, font="lucida 20 bold")
    b1.pack(side=LEFT)
    b1.bind("<Button-1>", click)
    if list1[i+3]=="-":
        b1 = Button(f, text=f"{list1[i+3]}", padx=28,
                pady=28, font="lucida 20 bold")
        b1.pack(side=LEFT)
        b1.bind("<Button-1>", click)
    else:

        b1 = Button(f, text=f"{list1[i+3]}", padx=28,
                    pady=28, font="lucida 20 bold")
        b1.pack(side=LEFT)
        b1.bind("<Button-1>", click)

    f.pack()
    i += 4



root.mainloop()
