import tkinter as tk
from tkinter import messagebox
from sympy import symbols, sympify, diff, integrate
import numpy as np
import matplotlib.pyplot as plt

expression = ""
derivative = ""

def calculate_derivative():
    global expression
    global derivative
    degree = degree_entry.get()
    coefficients = coefficients_entry.get()
    variable = variable_entry.get()
    try:
        x = symbols(variable)
        degree = int(degree)
        coefficients = [float(coeff) for coeff in coefficients.split(",")]

        expression = 0
        for i in range(0, degree + 1):
            expression += coefficients[i] * x ** (degree - i)

        derivative = diff(expression, x)

        result_label.config(text=f"Phương trình gốc: {expression}\nĐạo hàm: {derivative}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi trong quá trình tính toán: {str(e)}")
        result_label.config(text="Phương trình gốc: \nĐạo hàm: ")

def calculate_integral():
    lower_limit = lower_limit_entry.get()
    upper_limit = upper_limit_entry.get()
    coefficients = coefficients_entry.get()
    variable = variable_entry.get()
    try:
        x = symbols(variable)
        lower_limit = float(lower_limit)
        upper_limit = float(upper_limit)
        if lower_limit >= upper_limit:
            messagebox.showerror("Lỗi", f"Hệ số trên phải lớn hơn hệ số dưới")
        else:
            coefficients = [float(coeff) for coeff in coefficients.split(",")]

            expression = 0
            for i in range(0, len(coefficients)):
                expression += coefficients[i] * x ** (len(coefficients) - i - 1)

            integral = integrate(expression, (x, lower_limit, upper_limit))

            result_label.config(text=f"Phương trình gốc: {expression}\nTích phân từ {lower_limit} đến {upper_limit}: {integral}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi trong quá trình tính toán: {str(e)}")
        result_label.config(text="Phương trình gốc: \nTích phân: ")

def plot_expression(expression, derivative):
    x = symbols(variable_entry.get())
    x_values = np.linspace(-10, 10, 400)
    y_expression = [expression.subs(x, val) for val in x_values]
    y_derivative = [derivative.subs(x, val) for val in x_values]

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x_values, y_expression, label="Phương trình gốc")
    plt.xlabel(variable_entry.get())
    plt.ylabel("Giá trị")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(x_values, y_derivative, label="Đạo hàm")
    plt.xlabel(variable_entry.get())
    plt.ylabel("Giá trị")
    plt.legend()

    plt.tight_layout()
    plt.show()

root = tk.Tk()
root.title("Tính Đạo Hàm và Tích Phân Của Phương Trình")

degree_label = tk.Label(root, text="Bậc của phương trình:")
degree_label.pack()

degree_entry = tk.Entry(root)
degree_entry.pack()

coefficients_label = tk.Label(root, text="Hệ số (các hệ số cách nhau bằng dấu phẩy từ bậc cao đến bậc thấp):")
coefficients_label.pack()

coefficients_entry = tk.Entry(root)
coefficients_entry.pack()

variable_label = tk.Label(root, text="Tên biến:")
variable_label.pack()

variable_entry = tk.Entry(root)
variable_entry.pack()

lower_limit_label = tk.Label(root, text="Hệ số dưới tích phân:")
lower_limit_label.pack()

lower_limit_entry = tk.Entry(root)
lower_limit_entry.pack()

upper_limit_label = tk.Label(root, text="Hệ số trên tích phân:")
upper_limit_label.pack()

upper_limit_entry = tk.Entry(root)
upper_limit_entry.pack()

calculate_derivative_button = tk.Button(root, text="Tính Đạo Hàm", command=calculate_derivative)
calculate_derivative_button.pack()

calculate_integral_button = tk.Button(root, text="Tính Tích Phân", command=calculate_integral)
calculate_integral_button.pack()

plot_expression_button = tk.Button(root, text="Vẽ Hình", command=lambda: plot_expression(expression, derivative))
plot_expression_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
