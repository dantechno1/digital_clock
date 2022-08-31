from tkinter import Tk, Label

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(bg="steelblue")

label = Label(window, text="Welcome to DevOps Class!", font=("Arial Black",30,"bold"), bg="steelblue", fg="white")
label.pack(pady=100)

window.mainloop()
