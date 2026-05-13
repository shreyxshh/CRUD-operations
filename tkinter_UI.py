from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from pathlib import Path
import os

root = Tk()
root.title("File Handling System")
root.geometry("600x500")
root.config(bg="#f0f0f0")

# =========================
# TEXT AREA
# =========================
text_area = Text(root, width=70, height=20)
text_area.pack(pady=20)

# =========================
# FUNCTIONS
# =========================

def refresh_files():
    text_area.delete(1.0, END)
    p = Path('.')
    items = list(p.rglob('*'))

    for index, file in enumerate(items):
        text_area.insert(END, f"{index + 1} - {file}\n")


def create_file():
    file_name = simpledialog.askstring("Create File", "Enter file name")

    if file_name:
        p = Path(file_name)

        if p.exists():
            messagebox.showinfo("Info", "File already exists!")
        else:
            content = simpledialog.askstring("Content", "Enter file content")

            with open(file_name, 'w') as file:
                file.write(content if content else "")

            messagebox.showinfo("Success", "File Created Successfully!")
            refresh_files()


def read_file():
    file_name = simpledialog.askstring("Read File", "Enter file name")

    if file_name:
        p = Path(file_name)

        if p.exists():
            with open(file_name, 'r') as file:
                content = file.read()

            text_area.delete(1.0, END)
            text_area.insert(END, content)

        else:
            messagebox.showerror("Error", "File not found!")


def update_file():
    file_name = simpledialog.askstring("Update File", "Enter file name")

    if file_name:
        p = Path(file_name)

        if p.exists():

            choice = simpledialog.askinteger(
                "Update Option",
                "Press 1 to overwrite\nPress 2 to append"
            )

            content = simpledialog.askstring(
                "Content",
                "Enter content"
            )

            if choice == 1:
                with open(file_name, 'w') as file:
                    file.write(content)

            elif choice == 2:
                with open(file_name, 'a') as file:
                    file.write(content)

            else:
                messagebox.showerror("Error", "Invalid choice")
                return

            messagebox.showinfo("Success", "File Updated!")

        else:
            messagebox.showerror("Error", "File does not exist!")


def delete_file():
    file_name = simpledialog.askstring("Delete File", "Enter file name")

    if file_name:
        p = Path(file_name)

        if p.exists():
            os.remove(p)
            messagebox.showinfo("Success", "File Deleted!")
            refresh_files()

        else:
            messagebox.showerror("Error", "File not found!")


def rename_file():
    file_name = simpledialog.askstring("Rename File", "Enter current file name")

    if file_name:
        p = Path(file_name)

        if p.exists():
            new_name = simpledialog.askstring(
                "Rename",
                "Enter new file name"
            )

            p.rename(new_name)

            messagebox.showinfo("Success", "File Renamed!")
            refresh_files()

        else:
            messagebox.showerror("Error", "File not found!")


def create_folder():
    folder_name = simpledialog.askstring(
        "Create Folder",
        "Enter folder name"
    )

    if folder_name:
        p = Path(folder_name)

        if p.exists():
            messagebox.showinfo("Info", "Folder already exists!")

        else:
            p.mkdir()
            messagebox.showinfo("Success", "Folder Created!")
            refresh_files()


def remove_folder():
    folder_name = simpledialog.askstring(
        "Remove Folder",
        "Enter folder name"
    )

    if folder_name:
        p = Path(folder_name)

        if p.exists():
            p.rmdir()
            messagebox.showinfo("Success", "Folder Removed!")
            refresh_files()

        else:
            messagebox.showerror("Error", "Folder not found!")


# =========================
# BUTTON FRAME
# =========================

frame = Frame(root, bg="#f0f0f0")
frame.pack()

Button(frame, text="Refresh Files", width=18, command=refresh_files).grid(row=0, column=0, padx=5, pady=5)

Button(frame, text="Create File", width=18, command=create_file).grid(row=1, column=0, padx=5, pady=5)

Button(frame, text="Read File", width=18, command=read_file).grid(row=1, column=1, padx=5, pady=5)

Button(frame, text="Update File", width=18, command=update_file).grid(row=2, column=0, padx=5, pady=5)

Button(frame, text="Delete File", width=18, command=delete_file).grid(row=2, column=1, padx=5, pady=5)

Button(frame, text="Rename File", width=18, command=rename_file).grid(row=3, column=0, padx=5, pady=5)

Button(frame, text="Create Folder", width=18, command=create_folder).grid(row=3, column=1, padx=5, pady=5)

Button(frame, text="Remove Folder", width=18, command=remove_folder).grid(row=4, column=0, padx=5, pady=5)

Button(frame, text="Exit", width=18, command=root.quit).grid(row=4, column=1, padx=5, pady=5)

# =========================
# START
# =========================

refresh_files()

root.mainloop()