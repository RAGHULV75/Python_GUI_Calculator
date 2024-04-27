# Python_GUI_Calculator
GUI Based Calculator for Windows using Python. 

This is a documentation for the code that creates a simple calculator using PySimpleGUI.

The code starts by importing PySimpleGUI as sg, which is a library for creating graphical user interfaces (GUIs) in Python.

The code then defines three columns of buttons for the calculator layout. Each column is a list of lists, where each sublist contains one or more buttons with their size, font, and key attributes.

The col_1 column contains the buttons for the digits from 0 to 9, as well as the buttons for the plus/minus sign and the decimal point. The key attribute is used to identify the button when an event occurs.

The col_2 column contains the buttons for the arithmetic operators of multiplication, subtraction, and addition. The key attribute is also used to identify the operator when an event occurs.

The col_3 column contains the buttons for the arithmetic operator of division, as well as the buttons for clearing the input, clearing the last entry, and calculating the result. The key attribute is also used to identify these functions when an event occurs.

The layout variable is a list that contains two sublists. The first sublist contains an input element with a font and size attribute, and a key attribute of '-Input-'. This element is used to display the input and output of the calculator. The second sublist contains a column element that combines the three columns of buttons with a vertical separator between them.

The code then creates a window object with the title "Calculator" and the layout variable as its argument.

The code then defines some variables and lists for storing the input and output values, as well as the operators.

The code then enters a while loop that runs until the window is closed by the user. Inside the loop, the code reads the event and value from the window object using its read method.

If the event is equal to sg.WIN_CLOSED, which means that the user has closed the window, then the loop breaks and the window object is closed using its close method.

If the event is in num, which is a list of strings from '0' to '9', then it means that the user has pressed a digit button. The code then checks if the length of history, which is a string variable that stores the input value, is less than 11. If so, it appends the event to history and updates the input element with its integer value using its update method.

If the event is in operator, which is a list of strings that represent the arithmetic operators, then it means that the user has pressed an operator button. The code then assigns op to be equal to event, and num_1 to be equal to history converted to a float value. The code then resets history to an empty string.

If the event is equal to "equal", which means that the user has pressed the equal button, then it means that the user wants to calculate the result. The code then assigns num_2 to be equal to history converted to a float value. The code then checks which operator was stored in op and performs the corresponding arithmetic operation on num_1 and num_2. The result is stored in result and updated on
the input element using its update method.

If the event is equal to "clr", which means that the user has pressed
the clear button, then it means that
the user wants to clear all input and output values. The code then resets history,
op, num_1, num_2,
and result to their initial values and updates
the input element with an empty string using its update method.


points 



This is a documentation for the code that creates a simple calculator using PySimpleGUI.

- The code starts by importing PySimpleGUI as sg, which is a library for creating graphical user interfaces (GUIs) in Python.
- The code then defines three columns of buttons for the calculator layout. Each column is a list of lists, where each sublist contains one or more buttons with their size, font, and key attributes.
  - The col_1 column contains the buttons for the digits from 0 to 9, as well as the buttons for the plus/minus sign and the decimal point. The key attribute is used to identify the button when an event occurs.
  - The col_2 column contains the buttons for the arithmetic operators of multiplication, subtraction, and addition. The key attribute is also used to identify the operator when an event occurs.
  - The col_3 column contains the buttons for the arithmetic operator of division, as well as the buttons for clearing the input, clearing the last entry, and calculating the result. The key attribute is also used to identify these functions when an event occurs.
- The layout variable is a list that contains two sublists. The first sublist contains an input element with a font and size attribute, and a key attribute of '-Input-'. This element is used to display the input and output of the calculator. The second sublist contains a column element that combines the three columns of buttons with a vertical separator between them.
- The code then creates a window object with the title "Calculator" and the layout variable as its argument.
- The code then defines some variables and lists for storing the input and output values, as well as the operators.
- The code then enters a while loop that runs until the window is closed by the user. Inside the loop, the code reads the event and value from the window object using its read method.
  - If the event is equal to sg.WIN_CLOSED, which means that the user has closed
  the window, then
    - The loop breaks and
    - The window object is closed using its close method.
  - If the event is in num, which is a list of strings from '0' to '9', then it means that
  the user has pressed a digit button. 
    - The code then checks if
    the length of history, which is a string variable that stores
    the input value,
    is less than 11. 
      - If so,
        - It appends
        the event to history and
        - Updates
        the input element with its integer value using its update method.
  - If
  the event is in operator,
  which is a list of strings that represent
  the arithmetic operators,
  then it means that
  the user has pressed an operator button. 
    - The code then assigns op to be equal to event,
    and num_1 to be equal to history converted to a float value. 
    - The code then resets history to an empty string.
  - If
  the event is equal to "equal",
  which means that
  the user has pressed
  the equal button,
  then it means that
  the user wants to calculate
  the result. 
    - The code then assigns num_2 to be equal to history converted to a float value. 
    - The code then checks which operator was stored in op and performs
    the corresponding arithmetic operation on num_1 and num_2. 
      - The result is stored in result and updated on
      the input element using its update method.
  - If
  the event is equal to "clr",
  which means that
  the user has pressed
  the clear button,
  then it means that
  the user wants to clear all input and output values. 
    - The code then resets history,
    op, num_1, num_2,
    and result to their initial values and updates
    the input element with an empty string using its update method.

more


This code is a simple calculator program that uses PySimpleGUI to create a graphical user interface. The code consists of four parts:

- Importing the PySimpleGUI module as sg
- Defining the layout of the calculator window, which has four columns of buttons for digits, operators, and other functions
- Creating a list of numbers and a list of operators for easy reference
- Creating a loop that reads the user input and performs the calculations based on the event and value variables

The code uses the sg.Window, sg.I, sg.B, sg.Col, and sg.VerticalSeparator methods from the PySimpleGUI module to create and update the window and its elements. The code also uses the win.read method to get the user input and the win.update method to display the result. The code uses conditional statements to check the event variable and perform the appropriate operations. The code uses the history variable to store the current input and the num_1 and num_2 variables to store the operands. The code uses the op variable to store the operator. The code handles some edge cases such as dividing by zero, entering more than 11 digits, and clearing the input.

![image](https://github.com/RAGHULV75/Python_GUI_Calculator/assets/168255383/14528951-d6bc-4287-a0df-3e6a40612384)
