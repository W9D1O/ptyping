from random import randint
from random import choice

#Variables globales, se movieron a este archivo para poder calcular el máximo de palabras que se pueden generar
#a maxY hay que restarle 1, que estaw agregado aen ptyjping para que rectangulo no quese sobreescrito con las palabras
#del primer renglón
maxX = 100
maxY = 16

def len_file(file) -> int:
    index:int = 0
    for i in file:
        index += 1
    return index

def flag_error(flag):
    try:
        assert flag == "-d" or flag == "-i" or flag == ""

    except AssertionError:
        print("ERROR: Unexoected flag.\n\nUsage: python ptyping.py\n Flags:\n\t-d: Word from right side\n\t-i: Word from left side")
        exit()

def return_name_file(flag) -> str:
    arch = ""
    if flag == "-d":
        arch = "der.txt"
    elif flag == "-i":
        arch = "izq.txt"
    else:
        arch = "0_palabras_todas.txt"
    return arch


def generar_texto(flag):

    flag_error(flag)
    arch = return_name_file(flag)

    file = open(arch,encoding="utf-8").readlines()
    
    text = ""
    countLetter = 0
    fLen = len_file(file)
    
    maxLetter = (maxX - 1) *(maxY - 1)

    randMaxLetter = randint(0,maxLetter)

    while countLetter < randMaxLetter:
        #print(countLetter)
        line = file[randint(0,fLen)]
        words = line.split() 
        i = choice(words)
        ss = i + " "

        countLetter += len(ss)
        #print(countLetter//maxX)
        text += ss
    return text
