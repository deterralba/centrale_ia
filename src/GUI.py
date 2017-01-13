import numpy as np

SQUARE_SIZE = 30

def draw_square(canvas, l, c, people):
    global SQUARE_SIZE
    center = (SQUARE_SIZE * (c + 0.5), SQUARE_SIZE * (l + 0.5))
    width = SQUARE_SIZE // 10
    race, number = people
    if race == 'V':
        color = 'red'
        text_color = 'white'
    elif race == 'L':
        color = 'brown'
        text_color = 'white'
    elif race == 'H':
        color = 'white'
        text_color = 'black'
    else:
        raise ValueError()
    canvas.create_text(center[0], center[1], text=str(number), color=text_color)
    canvas.create_rectangle(SQUARE_SIZE*c, SQUARE_SIZE*l, SQUARE_SIZE*(l+1), SQUARE_SIZE*(c+1), fill=color, outline='grey')


def draw(canvas, solution, solved=False):
    global SQUARE_SIZE
    canvas.delete('all')
    line, col = solution.shape
    for l in range(line):
        for c in range(col):
            if any(board[l, c]):
                people = get_people(board[l, c])
                draw_square(canvas, l, c, people)
    '''
    for l in range(1, line):
        canvas.create_line(0, SQUARE_SIZE * l, SQUARE_SIZE * col, SQUARE_SIZE * l, fill='grey')
    for c in range(1, col):
        canvas.create_line(SQUARE_SIZE * c, 0, SQUARE_SIZE * c, SQUARE_SIZE * line, fill='grey')
    '''

    if solved:
        canvas.configure(background='green')
    else:
        canvas.configure(background='red')

    canvas.update()

def get_people(case):
    return ('H'*case[0] + 'L'*case[1] + 'V'*case[2], max(case))

def GUI_solve(canvas, problem, FORWARD_CHECK, ARC_CONSISTENCY, SHOW_STEPS, FAST):
    from misc import console_print_solutions
    from time import time, sleep
    start = time()
    if FAST:
        solutions = solve(
            problem,
            FORWARD_CHECK=FORWARD_CHECK,
            ARC_CONSISTENCY=ARC_CONSISTENCY
        )
    else:
        solutions = solve(
            problem,
            FORWARD_CHECK=FORWARD_CHECK,
            ARC_CONSISTENCY=ARC_CONSISTENCY,
            GUI_callback=lambda solution, valid=False: draw(canvas, solution, SHOW_STEPS=SHOW_STEPS, solved=valid)
        )

    console_print_solutions(solutions, start)
    if solutions:
        global button
        button.pack_forget()
        while True:
            for solution in solutions:
                draw(canvas, solution, solved=True)
                sleep(0.8)


def start_GUI(problem, **params):
    global SQUARE_SIZE, button
    SQUARE_SIZE = 30

    line, col = problem.shape

    import tkinter
    root = tkinter.Tk()
    root.geometry('{}x{}'.format(SQUARE_SIZE*col, 2*SQUARE_SIZE*line + 50))

    canvas1 = tkinter.Canvas(root, width=SQUARE_SIZE*col, height=SQUARE_SIZE*line)
    draw(canvas1, problem)
    canvas1.configure(background='black')
    canvas1.pack()

    canvas2 = tkinter.Canvas(root, width=SQUARE_SIZE*col, height=SQUARE_SIZE*line)
    canvas2.configure(background='red')
    canvas2.pack()

    def start_solving(event=None):
        GUI_solve(
            canvas2,
            problem,
            **params
        )
    root.bind('<Return>', start_solving)
    button = tkinter.Button(root, text='Solve', command=start_solving)
    button.pack(expand=1)

    root.mainloop()
