import tkinter as tk
from actions import show_city_graph

window = tk.Tk()

window.title("Air Pollution Tracker")
window.geometry("700x600")
window.configure(bg="#396893")

name = tk.Label(window, text="Air Pollution Tracker", font=("Arial", 30), bg="#396893", fg="white")
name.pack(padx=15, pady=15)

select = tk.Label(window, text="Select Texas City", font=("Arial", 20), bg="#396893", fg="white")
select.pack(padx=10, pady=10)

button1 = tk.Button(window, text="Austin", font=("Arial", 15), bg="#FFFFFF", fg="black", command=lambda: show_city_graph('Austin',window))
button1.pack(padx=6, pady=8)

button2 = tk.Button(window, text="Dallas", font=("Arial", 15), bg="#FFFFFF", fg="black", command=lambda: show_city_graph('Dallas',window))
button2.pack(padx=6, pady=8)

button3 = tk.Button(window, text="Houston", font=("Arial", 15), bg="#FFFFFF", fg="black", command=lambda: show_city_graph('Houston',window))
button3.pack(padx=6, pady=8)

window.mainloop()
