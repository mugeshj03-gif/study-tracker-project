import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="study_tracker")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(50) UNIQUE)")

cursor.execute("CREATE TABLE IF NOT EXISTS study_sessions (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),subject VARCHAR(50),duration VARCHAR(20),session_date DATE,focus FLOAT )")

conn.commit()

current_user = None
ids = []

def valid_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False

def clear_fields():
    entry_subject.delete(0, tk.END)
    entry_duration.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_focus.delete(0, tk.END)

def load_data():
    listbox.delete(0, tk.END)
    ids.clear()

    cursor.execute(
        "SELECT id, subject, duration, session_date, focus FROM study_sessions WHERE name=%s",
        (current_user,)
    )

    rows = cursor.fetchall()
    for row in rows:
        ids.append(row[0])
        listbox.insert(tk.END, f"{row[1]} | {row[2]} | {row[3]} | {row[4]}")

def login():
    global current_user
    username = entry_user.get().strip()

    if username == "":
        messagebox.showerror("Error", "Enter username")
        return

    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    if cursor.fetchone() is None:
        messagebox.showerror("Error", "User not found. Register first")
        return

    current_user = username
    login_frame.pack_forget()
    main_frame.pack()

    load_data()

def register():
    username = entry_user.get().strip()

    if username == "":
        messagebox.showerror("Error", "Enter username")
        return

    try:
        cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
        conn.commit()
        messagebox.showinfo("Success", "Registered successfully")
    except:
        messagebox.showerror("Error", "User already exists")

def add_data():
    subject = entry_subject.get()
    duration = entry_duration.get()
    date = entry_date.get()
    focus = entry_focus.get()

    if not subject or not duration or not date or not focus:
        messagebox.showerror("Error", "Fill all fields")
        return

    if not valid_date(date):
        messagebox.showerror("Error", "Date must be YYYY-MM-DD")
        return

    try:
        focus = float(focus)
    except:
        messagebox.showerror("Error", "Focus must be number")
        return

    cursor.execute("INSERT INTO study_sessions (name, subject, duration, session_date, focus)VALUES (%s, %s, %s, %s, %s)", (current_user, subject, duration, date, focus))

    conn.commit()
    load_data()
    clear_fields()

def delete_data():
    if not listbox.curselection():
        return

    index = listbox.curselection()[0]

    cursor.execute("DELETE FROM study_sessions WHERE id=%s", (ids[index],))
    conn.commit()

    load_data()

def select_item(event):
    if not listbox.curselection():
        return

    index = listbox.curselection()[0]

    cursor.execute("SELECT subject, duration, session_date, focus FROM study_sessions WHERE id=%s", (ids[index],))

    row = cursor.fetchone()

    clear_fields()

    entry_subject.insert(0, row[0])
    entry_duration.insert(0, row[1])
    entry_date.insert(0, row[2])
    entry_focus.insert(0, row[3])

def update_data():
    if not listbox.curselection():
        return

    index = listbox.curselection()[0]

    try:
        focus = float(entry_focus.get())
    except:
        messagebox.showerror("Error", "Focus must be number")
        return

    cursor.execute("UPDATE study_sessions SET subject=%s, duration=%s, session_date=%s, focus=%s WHERE id=%s", (
        entry_subject.get(),
        entry_duration.get(),
        entry_date.get(),
        focus,
        ids[index]
    ))

    conn.commit()
    load_data()

root = tk.Tk()
root.title("Study Tracker")

login_frame = tk.Frame(root)
login_frame.pack()

tk.Label(login_frame, text="Username").pack()
entry_user = tk.Entry(login_frame)
entry_user.pack()

tk.Button(login_frame, text="Login", command=login).pack()
tk.Button(login_frame, text="Register", command=register).pack()

main_frame = tk.Frame(root)

listbox = tk.Listbox(main_frame, width=50)
listbox.pack()
listbox.bind("<<ListboxSelect>>", select_item)

tk.Label(main_frame, text="Subject").pack()
entry_subject = tk.Entry(main_frame)
entry_subject.pack()

tk.Label(main_frame, text="Duration ()").pack()
entry_duration = tk.Entry(main_frame)
entry_duration.pack()

tk.Label(main_frame, text="Date (YYYY-MM-DD)").pack()
entry_date = tk.Entry(main_frame)
entry_date.pack()

tk.Label(main_frame, text="Focus (0-100)").pack()
entry_focus = tk.Entry(main_frame)
entry_focus.pack()

tk.Button(main_frame, text="Add", command=add_data).pack()
tk.Button(main_frame, text="Update", command=update_data).pack()
tk.Button(main_frame, text="Delete", command=delete_data).pack()
tk.Button(main_frame, text="Refresh", command=load_data).pack()

root.mainloop()
