import tkinter as tk
from PIL import Image, ImageTk
import math  # Import math for square root

calculation = ""

def add2calculations(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", calculation)

def evaluatecalculations():
    global calculation
    try:
        result = str(eval(calculation))
        text_result.delete("1.0", "end")
        text_result.insert("1.0", result)
        calculation = result
    except Exception as e:
        clear_field()
        text_result.delete("1.0", "end")
        text_result.insert("1.0", "ERROR")
        calculation = ""

def clear_field():
    global calculation
    calculation = ""
    text_result.delete("1.0", "end")

def sqrt_calculation():
    global calculation
    try:
        # Handle empty input or invalid input
        if not calculation:
            text_result.delete("1.0", "end")
            text_result.insert("1.0", "ERROR")
            return

        # Evaluate the expression and compute the square root
        value = float(eval(calculation))  # Safely evaluate the input
        if value < 0:
            text_result.delete("1.0", "end")
            text_result.insert("1.0", "ERROR")  # Square root of negative numbers is not supported
            return

        result = str(math.sqrt(value))  # Use math.sqrt for square root
        text_result.delete("1.0", "end")
        text_result.insert("1.0", result)
        calculation = result  # Update calculation with the result
    except Exception as e:
        clear_field()
        text_result.delete("1.0", "end")
        text_result.insert("1.0", "ERROR")
        calculation = ""



root = tk.Tk()
root.geometry("1200x673")
root.configure(bg="red")

# Load JPG image using Pillow
image = Image.open("neon.JPG")
bg_image = ImageTk.PhotoImage(image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

text_result = tk.Text(root, height=2, width=18, font=("Helvetica Neue", 24), bg="lavender", fg="black", bd=0)
text_result.grid(columnspan=5, pady=20)

# Button Definitions
button_1 = tk.Button(root, text="1", command=lambda: add2calculations(1), width=5, font=("Arial", 24))
button_1.grid(row=2, column=1, padx=6, pady=6)

button_2 = tk.Button(root, text="2", command=lambda: add2calculations(2), width=5, font=("Arial", 24))
button_2.grid(row=2, column=2, padx=6, pady=6)

button_3 = tk.Button(root, text="3", command=lambda: add2calculations(3), width=5, font=("Arial", 24))
button_3.grid(row=2, column=3, padx=6, pady=6)

button_4 = tk.Button(root, text="4", command=lambda: add2calculations(4), width=5, font=("Arial", 24))
button_4.grid(row=3, column=1, padx=6, pady=6)

button_5 = tk.Button(root, text="5", command=lambda: add2calculations(5), width=5, font=("Arial", 24))
button_5.grid(row=3, column=2, padx=6, pady=6)

button_6 = tk.Button(root, text="6", command=lambda: add2calculations(6), width=5, font=("Arial", 24))
button_6.grid(row=3, column=3, padx=6, pady=6)

button_7 = tk.Button(root, text="7", command=lambda: add2calculations(7), width=5, font=("Arial", 24))
button_7.grid(row=4, column=1, padx=6, pady=6)

button_8 = tk.Button(root, text="8", command=lambda: add2calculations(8), width=5, font=("Arial", 24))
button_8.grid(row=4, column=2, padx=6, pady=6)

button_9 = tk.Button(root, text="9", command=lambda: add2calculations(9), width=5, font=("Arial", 24))
button_9.grid(row=4, column=3, padx=6, pady=6)

button_0 = tk.Button(root, text="0", command=lambda: add2calculations(0), width=5, font=("Arial", 24))
button_0.grid(row=5, column=2, padx=6, pady=6)

button_dot = tk.Button(root, text=".", command=lambda: add2calculations("."), width=5, font=("Arial", 24))
button_dot.grid(row=5, column=4, padx=6, pady=6)

button_open = tk.Button(root, text="(", command=lambda: add2calculations("("), width=5, font=("Arial", 24))
button_open.grid(row=4, column=4, padx=6, pady=6)

button_close = tk.Button(root, text=")", command=lambda: add2calculations(")"), width=5, font=("Arial", 24))
button_close.grid(row=4, column=5, padx=6, pady=6)

button_plus = tk.Button(root, text="+", command=lambda: add2calculations("+"), width=5, font=("Arial", 24))
button_plus.grid(row=2, column=5, padx=6, pady=6)

button_minus = tk.Button(root, text="-", command=lambda: add2calculations("-"), width=5, font=("Arial", 24))
button_minus.grid(row=2, column=4, padx=6, pady=6)

button_mul = tk.Button(root, text="*", command=lambda: add2calculations("*"), width=5, font=("Arial", 24))
button_mul.grid(row=3, column=4, padx=6, pady=6)

button_div = tk.Button(root, text="/", command=lambda: add2calculations("/"), width=5, font=("Arial", 24))
button_div.grid(row=3, column=5, padx=6, pady=6)

button_cl = tk.Button(root, text="AC", command=clear_field, width=5, font=("Arial", 24))
button_cl.grid(row=5, column=5, padx=6, pady=6)

button_equals = tk.Button(root, text="=", command=evaluatecalculations, width=5, font=("Arial", 24))
button_equals.grid(row=6, column=4, columnspan=4, padx=6, pady=6)

button_exp = tk.Button(root, text="^", command=lambda: add2calculations("**"), width=5, font=("Arial", 24))
button_exp.grid(row=5, column=3, padx=6, pady=6)

button_sqrt = tk.Button(root, text="√", command=sqrt_calculation, width=5, font=("Arial", 24))
button_sqrt.grid(row=5, column=1, padx=6, pady=6)

root.mainloop()
