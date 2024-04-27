import PySimpleGUI as sg

col_1 = [
        [sg.B('7', size=(4,2),font="bold"),sg.B('8', size=(4,2),font="bold"),sg.B('9', size=(4,2),font="bold")],
        [sg.B('4', size=(4,2),font="bold"),sg.B('5', size=(4,2),font="bold"),sg.B('6', size=(4,2),font="bold")],
        [sg.B('1', size=(4,2),font="bold"),sg.B('2', size=(4,2),font="bold"),sg.B('3', size=(4,2),font="bold")],
        [sg.B('+/-', size=(4,2),font="bold", key='OPPOSITE'),sg.B('0', size=(4,2),font="bold"),sg.B('.', size=(4,2),font="bold",key='DOT')],
        ]

col_2 = [
        [sg.B('*', size=(4,2),font="bold",key='mul')],
        [sg.B('-', size=(4,2),font="bold",key='min')],
        [sg.B('+', size=(4,5),font="bold",key='plus')],
        ]

col_3 = [
        [sg.B('/', size=(4,2),font="bold",key='devide')],
        [sg.B('-->', size=(4,2),font="bold",key='clr')],
        [sg.B('CE', size=(4,2),font="bold",key='cle')],
        [sg.B('=', size=(4,2),font="bold",key='equal')],
        ]

layout = [
         [sg.I(font=(None,30),size=(15,1),key='-Input-')],
         [sg.Col(col_1), sg.VerticalSeparator() ,sg.Col(col_2), sg.Col(col_3)]
         ]


num = [str(i) for i in range(10)]


win = sg.Window("Calculater", layout)

history = ""
operator = ["devide","plus","min","mul"]
while True:
    event, Value = win.read()
    if event == sg.WIN_CLOSED:
        break
        win.close()
    elif event in  num:
        if len(history)<11:
            history += event
            win["-Input-"].update(int(history))
    elif event in operator:
        op = event
        num_1 = float(history)
        history = ""
    elif event == "equal":
        num_2 = float(history)
        if op  == "plus":
            result = num_1 + num_2
        elif op  == "min":
            result = num_1 - num_2
        elif op  == "mul":
            result = num_1 * num_2
        elif op  == "devide":
            result = num_1 / num_2
        win["-Input-"].update(result)
    elif event == "clr":
        if len(history):
            history = history[:-1]
            win["-Input-"].update(history)
    elif event == "cle":
        history = ""
        num_1 = 0
        num_2 = 0
        op = ""
        win["-Input-"].update(history)
    elif event == "OPPOSITE":
        history = str (int(history) * -1)
        win["-Input-"].update(history)
