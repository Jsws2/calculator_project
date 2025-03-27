import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        score1 = int(entry1.get())
        score2 = int(entry2.get())
        score3 = int(entry3.get())

        
        total = score1 + score2 + score3
        avg = total / 3

        result_label.config(text=f'합계: {total}점, 평균: {avg:.2f}점')

    except ValueError:
        messagebox.showerror("입력 오류", "숫자만 입력하세요")


root = tk.Tk()
root.title("평균 계산기")

tk.Label(root, text="점수1:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="점수2:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="점수3:").grid(row=2, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

calc_button = tk.Button(root, text="계산", command=calculate)
calc_button.grid(row=3, columnspan=2)

result_label = tk.Label(root, text="결과: ")
result_label.grid(row=4, columnspan=2)

root.mainloop()