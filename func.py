from random import randint
def rand(a):
    A={randint(0,20) for i in range(a)}
    return A


def universal(u):
    U = {i for i in range(u)}
    return U

def str_to_set(stri):
    A={int(i) for i in stri if i.isdecimal()}
    return A

def print_label(label_list, entry_list):
    label_list[0].configure(text=str(entry_list[0].get()))
    label_list[1].configure(text=str(entry_list[1].get()))
    label_list[2].configure(text=str(entry_list[2].get()))
