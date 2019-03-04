import random as r
import re
import pickle
from alg_2 import alg_2
from basic_alg import basic_alg


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
    pattern = re.compile('\d+')
    elements = re.findall(pattern, stri)
    for i in elements:
        sett.add(int(i))
    return sett

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

def u_print(l,l1):
    global U
    l.configure(text=str(universal(int(l1.get()))))
    U=str_to_set(l.cget("text"))


def print_from_constants(label_list):
    global A, B, C
    label_list[0].configure(text=str(A))
    label_list[1].configure(text=str(B))
    label_list[2].configure(text=str(C))


def step_exec(label):
    label.configure(text=  'NA = {NA}\n'
                           'NB = {NB}\n'
                           'NC = {NC}\n'
                           '1) NA&B = {f1}\n'
                           '2) NA|C = {f2}\n'
                           '3) B&C = {f3}\n'
                           '4) B&NC = {f4}\n'
                           '5) NA|(NA|B) = {f5}\n'
                           '6) NA|(NA|B)&(NA|C) = {f6}\n'
                           '7) (B&C)|(B&NC) = {f7}\n'
                           '8) NB&((B&C)|(B|NC)) = {f8}\n'
                           '9) NA|(NA|B)&(NA|C)|NB&((B&C)|(B|NC))={f9}\n'.format(NA=U-A,
                                                NB=U-B,
                                                NC=U-C,
                                                f1=(U-A)|B,
                                                f2=(U-A)|C,
                                                f3=B&C,
                                                f4=B&(U-C),
                                                f5=(U-A)|((U-A)|B),
                                                f6=(U-A)|((U-A)|B)&((U-A)|C),
                                                f7=(B&C)|(B&(U-C)),
                                                f8=(U-B)&(B&C)|(B&(U-C)),
                                                f9=basic_alg(A, B, C, U)))


def step_exec_2(A, B, C, U, label):

    label.configure(text='1) NA = {NA}\n'
                         '2) B and C = {BC}\n'
                         '3) D = {f3}\n'.format(NA=U-A,
                                                 BC=B&C,
                                                 f3=(U - A) | (B & C)))

def func2(A, C, U, label):
    X=U-C
    Y=A
    Z = alg_2(X, Y)
    label.configure(text='Z = ' + str(Z))
    return Z

def save_to_file1(D):
    with open(r'file1.txt', 'wb') as f:
        pickle.dump(D, f)

def save_to_file2(D):
    with open(r'file2.txt', 'wb') as f:
        pickle.dump(D, f)

def save_to_file3(Z):
    with open('file3.txt','wb') as f:
        pickle.dump(Z,f)
def read_from_file():
    global K
    with open(r'file1.txt','rb') as f:
        K=pickle.load(f)
        return K
def read_from_file2():
    global H
    with open(r'file2.txt','rb') as f:
        H=pickle.load(f)
        return H
def read_from_file3():
    global J
    with open(r'file3.txt','rb') as f:
        J=pickle.load(f)
        return J
def virno_funk(a,b):
    return "Результати збiгаються" if a==b else "Не збігаються."
def simetr_difer(a,b):
    return (a^b)
def calc_Z(A,C,U):
    X = U - C
    Y = A
    return str(X & Y)
def Z_equals(label1, label2, label3):
    label3.configure(text="Результати збігаються") if label1.cget('text') == label2.cget('text') else label3.configure(text="Результати не збігаються")

#print('Stri:' + str(str_to_set(',,,2,3,4,1,,')))
print("Stri ti set:" + str(str_to_set(',,,1,2,3,4,5,1;;')))
print("Stri ti set:" + str(str_to_set('1,,,2,123,4,5,1,,,')))
print("Stri ti set:" + str(str_to_set('1,,2132,313,,,4,51,,23,1')))