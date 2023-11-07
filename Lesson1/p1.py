from tkinter import *
from tkinter import ttk 
from tkinter import filedialog, messagebox
import numpy as np 

def make_center(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root = Tk()
root.geometry('1000x700')
make_center(root)

data = []
def open_file():
    global data
    file_path = filedialog.askopenfilename(filetypes=[('Text File', '*.txt')])
    if file_path is not None:
        with open(file=file_path, mode='r') as f:
            content = f.read()
            try:
                data = [float(x) for x in content.split()]
            except ValueError as e: 
                # print("Dữ liệu đọc phải có dạng số!")
                messagebox.showerror(title="Value Error", message=f"{e}: Dữ liệu vào phải ở dạng số !")


btn = ttk.Button(root, text='Open', command=lambda: open_file())
btn.pack(side=TOP, pady=10)

equations_label = ttk.Label(root, text="Hệ phương trình: ")
equations_label.pack(pady=10)

result_label = ttk.Label(root, text="Result will be shown here: ")
result_label.pack(pady=10)

def solve_equations():
    global data 
    n = int(data[0])
    arr = np.array(data[1:], dtype='float64')
    arr = arr.reshape(n, n+1)
    # print(arr)
    A = arr[:,:n]
    print(A)
    B = arr[:,n:].flatten()
    print(B)

    equations_text = "Hệ phương trình: \n"
    for i in range(n):
        equation = " + ".join([f"{A[i][j]}x{j+1}" for j in range(n)]) + f" = {B[i]}"
        equations_text += equation + "\n"

    equations_label.configure(text=equations_text)
    try:
        # Giải hệ thống phương trình tuyến tính Ax = B
        x = np.linalg.solve(A, B)
        print(x)
    except np.linalg.LinAlgError as e:
        if np.linalg.matrix_rank(A) < np.linalg.matrix_rank(arr):
            messagebox.showinfo(title="Singular matrix", message=f"{e}: Hệ phương trình vô nghiệm !")
        else:
            messagebox.showinfo(title="Singular matrix", message=f"{e}: Hệ phương trình vô số nghiệm !")
        
def clear():
    equations_label.configure(text="")



solve_button = ttk.Button(root, text='Solve', command=solve_equations)
solve_button.pack(pady=10)

clear_button = ttk.Button(root, text='Clear', command=clear)
clear_button.pack(pady=10)

quit_button = ttk.Button(root, text='Quit', command=quit)
quit_button.pack(pady=10)

root.mainloop()
