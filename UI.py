import tkinter as tk
from tkinter import ttk

def open_window1():
    window1 = tk.Toplevel(root)
    window1.title("Window 1")
    window1.configure(bg="lightblue")
    label1 = ttk.Label(window1, text="This is Window 1", background="lightblue")
    label1.pack(padx=200, pady=200)

def open_window2():
    window2 = tk.Toplevel(root)
    window2.title("Add record")
    window2.configure(bg="lightgreen")
    label2 = ttk.Label(window2, text="Add record", background="lightgreen", font=("Helvetica", 16))
    label2.pack(padx=20, pady=20)

    button_bank_card = tk.Button(window2, text="Add bank card", command=open_add_bank_card, width=30, height=3, bg="springgreen", fg="black", activebackground="green", activeforeground="white", font=("Helvetica", 14))
    button_bank_card.pack(padx=20, pady=10)

    button_transaction = tk.Button(window2, text="Add transaction", command=open_add_transaction, width=30, height=3, bg="lightseagreen", fg="black", activebackground="green", activeforeground="white", font=("Helvetica", 14))
    button_transaction.pack(padx=20, pady=10)

    button_category = tk.Button(window2, text="Add category", command=open_add_category, width=30, height=3, bg="mediumseagreen", fg="black", activebackground="green", activeforeground="white", font=("Helvetica", 14))
    button_category.pack(padx=20, pady=10)

def open_window3():
    window3 = tk.Toplevel(root)
    window3.title("Window 3")
    window3.configure(bg="lightyellow")
    label3 = ttk.Label(window3, text="This is Window 3", background="lightyellow")
    label3.pack(padx=200, pady=200)

def open_add_bank_card():
    add_bank_card_window = tk.Toplevel(root)
    add_bank_card_window.title("Add Bank Card")
    add_bank_card_window.configure(bg="springgreen")
    
    label = ttk.Label(add_bank_card_window, text="Add Bank Card", background="springgreen", font=("Helvetica", 16))
    label.pack(padx=20, pady=20)

    bank_name_label = ttk.Label(add_bank_card_window, text="Bank Name:", background="springgreen", font=("Helvetica", 12))
    bank_name_label.pack(padx=20, pady=(10, 0))

    bank_name_entry = ttk.Entry(add_bank_card_window, font=("Helvetica", 12))
    bank_name_entry.pack(padx=20, pady=5)

    balance_label = ttk.Label(add_bank_card_window, text="Bank Balance:", background="springgreen", font=("Helvetica", 12))
    balance_label.pack(padx=20, pady=(10, 0))

    balance_entry = ttk.Entry(add_bank_card_window, font=("Helvetica", 12))
    balance_entry.pack(padx=20, pady=5)

    add_button = tk.Button(add_bank_card_window, text="Add", width=15, height=2, bg="lightblue", fg="black", activebackground="blue", activeforeground="white", font=("Helvetica", 12))
    add_button.pack(padx=20, pady=20)

def open_add_transaction():
    add_transaction_window = tk.Toplevel(root)
    add_transaction_window.title("Add Transaction")
    add_transaction_window.configure(bg="lightseagreen")
    label = ttk.Label(add_transaction_window, text="Add Transaction", background="lightseagreen", font=("Helvetica", 16))
    label.pack(padx=200, pady=200)

def open_add_category():
    add_category_window = tk.Toplevel(root)
    add_category_window.title("Add Category")
    add_category_window.configure(bg="mediumseagreen")
    label = ttk.Label(add_category_window, text="Add Category", background="mediumseagreen", font=("Helvetica", 16))
    label.pack(padx=200, pady=200)

root = tk.Tk()
root.title("My Database Project")

title_label = tk.Label(root, text="My Database Project", font=("Helvetica", 20, "bold"))
title_label.pack(padx=40, pady=20)

button1 = tk.Button(root, text="Show information", command=open_window1, width=40, height=4, bg="lightblue", fg="black", activebackground="blue", activeforeground="white", font=("Helvetica", 16))
button1.pack(padx=40, pady=10)

button2 = tk.Button(root, text="Add record", command=open_window2, width=40, height=4, bg="lightgreen", fg="black", activebackground="green", activeforeground="white", font=("Helvetica", 16))
button2.pack(padx=40, pady=10)

button3 = tk.Button(root, text="Search", command=open_window3, width=40, height=4, bg="lightyellow", fg="black", activebackground="yellow", activeforeground="white", font=("Helvetica", 16))
button3.pack(padx=40, pady=10)

root.mainloop()
