import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

# Функция для выбора файла PDF
def select_pdf_file():
    pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, pdf_file_path)

# Функция для выбора места и имени для DOCX файла
def select_docx_file():
    docx_file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")])
    docx_entry.delete(0, tk.END)
    docx_entry.insert(0, docx_file_path)

# Функция для выполнения преобразования
def convert():
    pdf_path = pdf_entry.get()
    print(pdf_entry.get())
    docx_path = docx_entry.get()

    if pdf_path and docx_path:
        cv = Converter(pdf_path)
        cv.convert(docx_path, start=0, end=None)
        cv.close()
        status_label.config(text="Преобразование завершено!")

# Создаем главное окно
root = tk.Tk()
root.title("PDF to DOCX Converter")

# Создаем и размещаем виджеты
pdf_label = tk.Label(root, text="Выберите файл PDF:")
pdf_label.pack()

pdf_entry = tk.Entry(root, width=50)
pdf_entry.pack()

pdf_button = tk.Button(root, text="Обзор", command=select_pdf_file)
pdf_button.pack()

docx_label = tk.Label(root, text="Выберите место и имя для DOCX файла:")
docx_label.pack()

docx_entry = tk.Entry(root, width=50)
docx_entry.pack()

docx_button = tk.Button(root, text="Обзор", command=select_docx_file)
docx_button.pack()

convert_button = tk.Button(root, text="Преобразовать", command=convert)
convert_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# Запускаем главный цикл приложения
root.mainloop()