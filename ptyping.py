import curses
from curses.textpad import rectangle


#clase para obtener un caracter con una poscion en la terminal
class Oracion:
    ch:chr
    x:int
    y:int
    def __init__(self,ch,x,y):
        self.ch = ch
        self.x = x
        self.y = y
    

#separa las platabras por espacios y asigna cara caracter a una posicion las guarda en una lista y la retorna
def asignar_posicion(texto:str, maxX:int) -> list:
    cadena:list[Oracion] = []
    palabra = ""
    x:int = 0
    y:int = 1
    for i in range(len(texto)):
        if i < len(texto) and texto[i] != ' ': #Esto solo va a funcionar porque el final de la oracion nunca va a haber un espacio.
            palabra += texto[i]               
        else:
            if i < len(texto):
                palabra += texto[i]
            if x + len(palabra) < maxX:
                for i in range(len(palabra)):
                    x += 1
                    aux_or = Oracion(ch=palabra[i], x= x,y=y)
                    cadena.append(aux_or)
            else:
                x = 0
                y += 1
                for i in range(len(palabra)):
                    x += 1
                    aux_or = Oracion(ch=palabra[i], x= x,y=y)
                    cadena.append(aux_or)
            palabra = ""
    return cadena
    

#Lo dice mas abajo pero inicia las cosas de ncurses
def init_curses(stdscr):
    # Initialize curses settings
    curses.cbreak()  # React to keys instantly without requiring Enter
    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.start_color()
    #No me queda para nada claro pero hay que inicializar los colores que uno quiene y de la forma en que los quiere
    curses.init_pair(curses.COLOR_BLUE,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_RED,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_GREEN,curses.COLOR_GREEN,curses.COLOR_BLACK)


#Dibuja los caracteres en la terminaln comprueba con texto dos, que es otra lista de caracteres si son iguales
#En caso de serlo pinta ade color verde el caracter corresponiente caso contrario de rojo
def render(win,maxX,texto,texto2):


    rectangle(win,0,0,14,maxX-1)

    for i in range(len(texto)):

        if texto2[i] == "":
            c = curses.COLOR_BLUE
        elif texto2[i] != "" and texto2[i] != texto[i].ch:
            c = curses.COLOR_RED
        elif texto2[i] == texto[i].ch:
            c = curses.COLOR_GREEN
        win.addstr(texto[i].y,texto[i].x,texto[i].ch,curses.color_pair(c))

    

def main(stdscr):
    init_curses(stdscr)
    texto = "Hola a todos yo soy el leon grito  la bestia en medio de la avenida yo soy el rey te destrozare, todos los complices son de mi apetito"
    texto2 = [""]*len(texto)
    maxX = 100
    c:int = curses.COLOR_BLUE
    _, x = stdscr.getmaxyx()
    paddingX = x//2 - maxX//2
    strWin = curses.newwin(16,maxX,4,paddingX)
    bp:int = 0 #index para las teclas apretadas

    tex_con_pos = asignar_posicion(texto,maxX)
    while True:

        render(strWin,maxX,tex_con_pos,texto2)
        key = stdscr.getch()  # Get character input

        if key != -1:  # A key was pressed
            texto2[bp] = chr(key)
            if bp < len(texto) - 1:
                bp += 1
        if key == 27:
            break  # ESC rompre el loop

        strWin.refresh() # Refresh the screen to

if __name__ == '__main__':
    curses.wrapper(main)
