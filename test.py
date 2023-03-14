import tkinter as tk



root = tk.Tk()
###bold_font = tk.Font(family="Gotham", size=20, weight="bold")
label = tk.Label(root, text="Hello, World!", padx=100, pady=10)
label.pack()

root.title("poopy")
##root.geometry("1280x700")
root.geometry("1280x700")
root.configure(bg="magenta")
def update_label():
    label.configure(text="ate poopy", font= ('Gotham', 18, 'bold'))


button = tk.Button(root, text="eat poopy", command=update_label)

button.pack()
root.mainloop()
print("test")