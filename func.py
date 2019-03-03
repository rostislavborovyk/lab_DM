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
    sett = set()
    stri = str(stri)
    if stri[0] == '{' and stri[-1] == '}':
        stri = stri[1:-1]
    # 1,2,3,4,5 --> {1,2,3,4,5}
    elements = stri.split(',')
    for i in elements:
        sett.add(int(i))
    return sett

def print_label(label_list, entry_list):
    global A, B, C
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


def print_from_constants(label_list):
    global A, B, C
    label_list[0].configure(text=str(A))
    label_list[1].configure(text=str(B))
    label_list[2].configure(text=str(C))


print(str_to_set('{1,2,3,4,5}'))
