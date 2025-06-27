import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import os
from datetime import datetime

FILENAME = "student_records.csv"

if not os.path.exists(FILENAME):
    pd.DataFrame(columns=["RollNo", "Name", "Age", "Marks", "Date"]).to_csv(FILENAME, index=False)

def load_data():
    df = pd.read_csv(FILENAME)
    return df

def save_data(df):
    df.to_csv(FILENAME, index=False)

def add_student():
    roll = roll_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    marks = marks_entry.get()

    if not roll or not name or not age or not marks:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    df = load_data()
    if roll in df["RollNo"].astype(str).values:
        messagebox.showerror("Duplicate", "Roll Number already exists.")
        return

    new_row = {
        "RollNo": roll,
        "Name": name,
        "Age": int(age),
        "Marks": float(marks),
        "Date": datetime.now().strftime("%Y-%m-%d")
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)
    messagebox.showinfo("Success", "Student record added successfully.")
    clear_fields()
    refresh_table()

def clear_fields():
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    df = load_data()
    for index, row in df.iterrows():
        tree.insert("", tk.END, values=list(row))

def delete_student():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a record to delete.")
        return
    df = load_data()
    roll = tree.item(selected[0])["values"][0]
    df = df[df["RollNo"].astype(str) != str(roll)]
    save_data(df)
    messagebox.showinfo("Deleted", f"Record with Roll No {roll} deleted.")
    refresh_table()

def update_student():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a record to update.")
        return

    roll = tree.item(selected[0])["values"][0]
    name = name_entry.get()
    age = age_entry.get()
    marks = marks_entry.get()

    if not name or not age or not marks:
        messagebox.showwarning("Input Error", "Please fill all fields to update.")
        return

    df = load_data()
    index = df[df["RollNo"].astype(str) == str(roll)].index[0]
    df.at[index, "Name"] = name
    df.at[index, "Age"] = int(age)
    df.at[index, "Marks"] = float(marks)
    save_data(df)
    messagebox.showinfo("Updated", f"Record with Roll No {roll} updated.")
    refresh_table()

def on_row_select(event):
    selected = tree.selection()
    if selected:
        row = tree.item(selected[0])["values"]
        roll_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        marks_entry.delete(0, tk.END)

        roll_entry.insert(0, row[0])
        name_entry.insert(0, row[1])
        age_entry.insert(0, row[2])
        marks_entry.insert(0, row[3])
        roll_entry.config(state='disabled')

def search_student():
    query = search_entry.get().lower()
    for row in tree.get_children():
        tree.delete(row)
    df = load_data()
    results = df[df['Name'].str.lower().str.contains(query)]
    for _, row in results.iterrows():
        tree.insert("", tk.END, values=list(row))

def show_analytics():
    df = load_data()
    if df.empty:
        messagebox.showinfo("Analytics", "No data available.")
        return
    total = len(df)
    highest = df["Marks"].max()
    lowest = df["Marks"].min()
    average = df["Marks"].mean()
    latest = df["Date"].max()
    msg = f"Total Students: {total}\nHighest Marks: {highest}\nLowest Marks: {lowest}\nAverage Marks: {average:.2f}\nLast Entry: {latest}"
    messagebox.showinfo("Analytics", msg)

def export_records():
    df = load_data()
    export_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if export_path:
        df.to_csv(export_path, index=False)
        messagebox.showinfo("Exported", f"Data exported to {export_path}")

root = tk.Tk()
root.title("Student Record Manager")
root.geometry("850x600")

# ==== Form ====
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

labels = ["Roll No", "Name", "Age", "Marks"]
entries = []
for i, label in enumerate(labels):
    tk.Label(form_frame, text=label).grid(row=0, column=i, padx=10)

roll_entry = tk.Entry(form_frame)
name_entry = tk.Entry(form_frame)
age_entry = tk.Entry(form_frame)
marks_entry = tk.Entry(form_frame)
roll_entry.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
age_entry.grid(row=1, column=2)
marks_entry.grid(row=1, column=3)

# ==== Buttons ====
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Student", command=add_student).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update Student", command=update_student).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete Student", command=delete_student).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Analytics", command=show_analytics).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Export CSV", command=export_records).grid(row=0, column=4, padx=5)

# ==== Search ====
search_frame = tk.Frame(root)
search_frame.pack(pady=5)
tk.Label(search_frame, text="Search by Name:").pack(side=tk.LEFT)
search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Search", command=search_student).pack(side=tk.LEFT)

# ==== Table ====
tree = ttk.Treeview(root, columns=("RollNo", "Name", "Age", "Marks", "Date"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", on_row_select)

refresh_table()
root.mainloop()