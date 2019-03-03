from tkinter import *
import func as f
from basic_alg import basic_alg
from simplified_alg import simplified_alg
from alg_2 import alg_2


G = 82
N = 3
Var = (N+G % 60) % 30+1
print("Моя група: ІВ -", G)
print("Мій номер у групі:", N)
print("Мій варіант:", (N+G % 60) % 30+1)
# -----------------------windows--------------------------------------

def window2():
    win2 = Toplevel(root)
    win2.geometry('400x200')

def window3():
    win3 = Toplevel(root)
    win3.geometry('400x200')

def window4():
    win4 = Toplevel(root)
    win4.geometry('400x200')

def window5():
    win5 = Toplevel(root)
    win5.geometry('400x200')
# --------------------------------------------------------------------

root = Tk()
# root.geometry('600x400')

mainMenu = Menu(root)
root.config(menu=mainMenu)

win2 = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=win2, label='Вікно 2')
win2.add_command(label='Відкрити', command=window2)

win3 = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=win3, label='Вікно 3')
win3.add_command(label='Відкрити', command=window3)

win4 = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=win4, label='Вікно 4')
win4.add_command(label='Відкрити', command=window4)

win5 = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=win5, label='Вікно 5')
win5.add_command(label='Відкрити', command=window5)


name_label1 = Label(root, text="Ім'я:")
name_label1.grid(row=0, column=0, sticky='w')
name_label2 = Label(root, text="Боровик  Ростислав  Вікторович")
name_label2.grid(row=0, column=1, sticky='w')
group_label1 = Label(root, text='Група:')
group_label1.grid(row=1, column=0, sticky='w')
group_label2 = Label(root, text='ІВ-82')
group_label2.grid(row=1, column=1, sticky='w')
list_num_label1 = Label(root, text='Номер у списку:')
list_num_label1.grid(row=2, column=0, sticky='w')
list_num_label2 = Label(root, text='3')
list_num_label2.grid(row=2, column=1, sticky='w')

var_label1 = Label(root, text='Варіант:')
var_label1.grid(row=3, column=0, sticky='w')
var_label2 = Label(root, text=str(Var))
var_label2.grid(row=3, column=1, sticky='w')

power_label = Label(root, text='Задайте потужність множин')
power_label.grid(row=0, column=2, columnspan=2, padx=10)
pow_a_label = Label(root, text='Потужність для А:')
pow_a_label.grid(row=1, column=2, sticky='w', padx=10)
pow_a_entry = Entry(root)
pow_a_entry.grid(row=1, column=3, sticky='w')
pow_b_label = Label(root, text='Потужність для B:')
pow_b_label.grid(row=2, column=2, sticky='w', padx=10)
pow_b_entry = Entry(root)
pow_b_entry.grid(row=2, column=3, sticky='w')
pow_c_label = Label(root, text='Потужність для C:')
pow_c_label.grid(row=3, column=2, sticky='w', padx=10)
pow_c_entry = Entry(root)
pow_c_entry.grid(row=3, column=3, sticky='w')
pow_button = Button(root, text="Згенерувати множини автоматично!")
pow_button.grid(row=4, column=2, columnspan=2, pady=5)

manual_label = Label(root, text='Задати множини вручну')
manual_label.grid(row=0, column=4, columnspan=2, padx=10)
man_a_label = Label(root, text='А:')
man_a_label.grid(row=1, column=4, sticky='w', padx=10)
man_a_entry = Entry(root)
man_a_entry.grid(row=1, column=5, sticky='w')
man_b_label = Label(root, text='B:')
man_b_label.grid(row=2, column=4, sticky='w', padx=10)
man_b_entry = Entry(root)
man_b_entry.grid(row=2, column=5, sticky='w')
man_c_label = Label(root, text='C:')
man_c_label.grid(row=3, column=4, sticky='w', padx=10)
man_c_entry = Entry(root)
man_c_entry.grid(row=3, column=5, sticky='w')
man_button = Button(root, text="Задати множини вручну!")
man_button.grid(row=4, column=4, columnspan=2, pady=5)

pow_button.bind('<Button-1>', lambda event: f.rand(int(pow_a_entry.get())))
label_a_rand=Label(root, text="A:")
label_a_rand.grid(row=5,column=2,sticky='w',padx=10)
label_al_rand=Label(root,text="")



print("\nРозмір сітки: ", root.grid_size())

root.mainloop()
