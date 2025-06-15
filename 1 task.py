import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result.set(eval(entry.get()))
        except Exception as e:
            result.set("Error")
    elif text == "C":
        entry.delete(0, tk.END)
        result.set("")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 20))
entry.pack()

result = tk.StringVar()
entry_result = tk.Entry(root, textvariable=result, font=("Arial", 20), state="readonly")
entry_result.pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(buttons_frame)
    row_frame.pack(side=tk.TOP)
    for button in row:
        btn = tk.Button(row_frame, text=button, font=("Arial", 20), width=5, height=2)
        btn.pack(side=tk.LEFT)
        btn.bind("<Button-1>", on_click)

root.mainloop()
j
