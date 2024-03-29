import numpy as np
from const import HUM, WOLV, VAMP

SQUARE_SIZE = 60

def draw_square(canvas, l, c, people):
    global SQUARE_SIZE
    center = (SQUARE_SIZE*(c + 0.5), SQUARE_SIZE*(l + 0.5))
    race, number = people
    if race == VAMP:
        color = 'red'
        text_color = 'white'
    elif race == WOLV:
        color = 'black'
        text_color = 'white'
    elif race == HUM:
        color = 'white'  # say no to racism
        text_color = 'black'
    else:
        print(people, number)
        raise ValueError()
    canvas.create_rectangle(SQUARE_SIZE*c, SQUARE_SIZE*l, SQUARE_SIZE*(c+1), SQUARE_SIZE*(l+1), fill=color, outline=color)
    canvas.create_text(center[0], center[1], text=str(number), fill=text_color)


def draw(board):
    global SQUARE_SIZE, canvas
    canvas.delete('all')

    canvas.configure(background='green')

    line, col, _ = board.shape
    for l in range(line):
        for c in range(col):
            if any(board[l, c]):
                people = get_people(board[l, c])
                if people[0]:
                    draw_square(canvas, l, c, people)

    # draw grid
    for l in range(1, line):
        canvas.create_line(0, SQUARE_SIZE*l, SQUARE_SIZE*col, SQUARE_SIZE*l, fill='grey')
    for c in range(1, col):
        canvas.create_line(SQUARE_SIZE*c, 0, SQUARE_SIZE*c, SQUARE_SIZE*line, fill='grey')

    canvas.update()


def get_people(case):
    return HUM*bool(case[0]) + VAMP*bool(case[1]) + WOLV*bool(case[2]), max(case)


def start_GUI(board, start):
    global SQUARE_SIZE, button, canvas

    line, col, _ = board.shape

    import tkinter
    root = tkinter.Tk()
    root.title('Vampires vs Wolves')
    root.geometry('{}x{}'.format(SQUARE_SIZE*col, SQUARE_SIZE*line + 50))

    canvas = tkinter.Canvas(root, width=SQUARE_SIZE*col, height=SQUARE_SIZE*line)
    draw(board)
    canvas.pack()

    root.bind('<Return>', start)
    button = tkinter.Button(root, text='Play', command=start)
    button.pack(expand=1)

    root.mainloop()





