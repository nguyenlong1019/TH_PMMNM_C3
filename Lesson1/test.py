# import json
# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# import numpy as np 

# root = Tk()
# root.geometry('300x300')

# data = []

# def open_file():
#     global data
#     file_path = filedialog.askopenfilename(filetypes=[('Text File', '*.txt')])
#     if file_path is not None:
#         with open(file=file_path, mode='r') as f:
#             content = f.read()
#             data = [float(x) for x in content.split()]

# btn = ttk.Button(root, text='Open', command=lambda: open_file())
# btn.pack(side=TOP, pady=10)

# result_label = Label(root, text="Result will be shown here:")
# result_label.pack(pady=10)

# def solve_equations():
#     global data
#     n = int(data[0])
#     arr = np.array(data[1:], dtype='float64')
#     A = arr[:n * n].reshape(n, n)
#     b = arr[n * n:]
    
#     try:
#         # Giải hệ thống phương trình tuyến tính Ax = b
#         x = np.linalg.solve(A, b)
#         result_label.config(text=f"Solution: {x}")
#     except np.linalg.LinAlgError:
#         result_label.config(text="Error: The system may be singular or not solvable.")

# solve_button = ttk.Button(root, text='Solve', command=solve_equations)
# solve_button.pack(pady=10)

# root.mainloop()








from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import numpy as np 

root = Tk()
root.geometry('1000x700')

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
                print("Dữ liệu đọc phải có dạng số!")

btn = ttk.Button(root, text='Open', command=lambda: open_file())
btn.pack(side=TOP, pady=10)

equations_label = ttk.Label(root, text="Hệ phương trình:")
equations_label.pack(pady=10)

result_label = ttk.Label(root, text="Kết quả sẽ được hiển thị ở đây:")
result_label.pack(pady=10)

def solve_equations():
    global data 
    n = int(data[0])
    arr = np.array(data[1:], dtype='float64')
    arr = arr.reshape(n, n+1)
    A = arr[:,:n]
    B = arr[:,n:].flatten()

    equations_text = "Hệ phương trình:\n"
    for i in range(n):
        equation = " + ".join([f"{A[i][j]}x{j+1}" for j in range(n)]) + f" = {B[i]}"
        equations_text += equation + "\n"

    equations_label.config(text=equations_text)

    try:
        x = np.linalg.solve(A, B)
    except np.linalg.LinAlgError as e:
        if np.linalg.matrix_rank(A) < np.linalg.matrix_rank(arr):
            message = f"{e}: Hệ phương trình vô nghiệm !"
        else:
            message = f"{e}: Hệ phương trình vô số nghiệm !"
        result_label.config(text=message)

solve_button = ttk.Button(root, text='Solve', command=solve_equations)
solve_button.pack(pady=10)

quit_button = ttk.Button(root, text='Quit', command=quit)
quit_button.pack(pady=10)

root.mainloop()
