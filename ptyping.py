import curses

def window(stdscr):
    pass

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

def render(win,maxX,texto,texto2):

    for i in range(len(texto)):
        y = i // maxX
        x = i % maxX
       
        if texto2[i] == "":
            c = curses.COLOR_BLUE
        elif texto2[i] != "" and texto2[i] != texto[i]:
            c = curses.COLOR_RED
        elif texto2[i] == texto[i]:
            c = curses.COLOR_GREEN
        win.addstr(y,x,texto[i],curses.color_pair(c))
        #curses.delay_output(20)

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
    #stdscr.addstr(10,0,str(len(texto)))
    stdscr.addstr(11,0,str(x))
    while True:
        render(strWin,maxX,texto,texto2)
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
