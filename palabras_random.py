
        

def generar_texto(flag):
    try:
        assert flag == "-d" or flag == "-i" or flag == ""

    except AssertionError:
        print("ERROR: Unexoected flag.\n\nUsage: python ptyping.py\n Flags:\n\t-d: Word from right side\n\t-i: Word from left side")
    
    arch = ""

    if flag == "-d":
        arch = "der.txt"
    elif flag == "-i":
        arch = "izq.txr"
    else:
        arch = "0_palabras_todas.txt"

    file = open(arch,"r",encoding="utf-8")
    p:list[str] = []

        
    for i in file:
        ss = i.replace("\n","")
        p.append(ss)


generar_texto(2)