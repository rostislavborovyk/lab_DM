import random as r
def rand(a):
    a=int(a)
    A = set()
    uni = [i for i in range(20)]
    for i in range(a):
        temp = r.choice(uni)
        A.add(temp)
        uni.remove(temp)
    return A



def universal(u):
    U = {i for i in range(1,u)}
    return U

def str_to_set(stri):
    A={int(i) for i in stri if i.isdecimal()}
    return A

def print_label(label_list, entry_list):
    global A,B,C
    label_list[0].configure(text=str(rand(entry_list[0].get())))
    label_list[1].configure(text=str(rand(entry_list[1].get())))
    label_list[2].configure(text=str(rand(entry_list[2].get())))
    A=(str_to_set(label_list[0].cget("text")))
    B=(str_to_set(label_list[1].cget("text")))
    C=(str_to_set(label_list[2].cget("text")))
def print_manlabel(label_list, entry_list):
    global A,B,C
    label_list[0].configure(text=str(str_to_set(entry_list[0].get())))
    label_list[1].configure(text=str(str_to_set(entry_list[1].get())))
    label_list[2].configure(text=str(str_to_set(entry_list[2].get())))
    A = (str_to_set(label_list[0].cget("text")))
    B = (str_to_set(label_list[1].cget("text")))
    C = (str_to_set(label_list[2].cget("text")))
