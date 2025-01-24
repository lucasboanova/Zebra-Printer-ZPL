import csv
import os
import sys
from models.modelZpl import ZplModel
from zpl.zpl import ZplFile
from zebra import Zebra
import logging
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import shutil
import json

LOG_DIR = os.path.join(os.path.expanduser("~"), "PrinterZPL")
CSV_DIR = os.path.join(LOG_DIR, "csvFile")

def create_directories():
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(CSV_DIR, exist_ok=True)

# Create directories before configuring logging
create_directories()

logging.basicConfig(level=logging.INFO, filename=os.path.join(LOG_DIR, 'app.log'), filemode='w', format='%(name)s - %(levelname)s - %(message)s')

CONFIG_FILE = 'config.json'

def load_config():
    config_path = os.path.join(LOG_DIR, CONFIG_FILE)
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            return json.load(file)
    return {}

def save_config(config):
    config_path = os.path.join(LOG_DIR, CONFIG_FILE)
    with open(config_path, 'w') as file:
        json.dump(config, file)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def process_csv_file(csv_file_path, printer_name):
    try:
        zebra_printer = Zebra()
        zebra_printer.setqueue(printer_name)

        with open(csv_file_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=';')
            total_rows = sum(1 for row in csv_reader)
            csvfile.seek(0)
            for i, row in enumerate(csv_reader):
                if len(row) != 3:
                    logging.error(f"Dados inválidos no CSV: {row}")
                    continue
                branch, turn, typeTonner = row
                zpl_model = ZplModel(turn=turn, typeTonner=typeTonner, branch=str(branch))
                zpl_file_path = os.path.join(LOG_DIR, f'output_{branch}.txt')
                with ZplFile(zpl_file_path) as zpl_file:
                    zpl_file.generate_zpl_label(zpl_model)
                    zebra_printer.output(zpl_file.filename)
                progress_var.set((i + 1) / total_rows * 100)
                root.update_idletasks()

        logging.info('ZPL impresso com sucesso')
        messagebox.showinfo("Sucesso", "ZPL impresso com sucesso")
    except Exception as e:
        logging.error(f"Erro ao processar o arquivo CSV: {e}")
        messagebox.showerror("Erro", f"Erro ao processar o arquivo CSV: {e}")

def select_csv_file():
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if csv_file_path:
        standard_csv_path = os.path.join(CSV_DIR, 'tonner.csv')
        shutil.copyfile(csv_file_path, standard_csv_path)
        display_csv_data(standard_csv_path)
        config['csv_file_path'] = csv_file_path
        save_config(config)

def display_csv_data(csv_file_path):
    for row in tree.get_children():
        tree.delete(row)
    with open(csv_file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        for row in csv_reader:
            tree.insert("", "end", values=row)

def print_labels():
    printer_name = printer_entry.get()
    if not printer_name:
        messagebox.showerror("Erro", "Por favor, insira o nome da impressora")
        return
    config['printer_name'] = printer_name
    save_config(config)
    csv_file_path = os.path.join(CSV_DIR, 'tonner.csv')
    logging.info(f"CSV file path: {csv_file_path}")
    process_csv_file(csv_file_path, printer_name)

root = tk.Tk()
root.title("Impressão de etiquetas ZPL")

config = load_config()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Selecione o arquivo CSV:")
label.pack(pady=5)

button = tk.Button(frame, text="Importar CSV", command=select_csv_file)
button.pack(pady=5)

tree = ttk.Treeview(frame, columns=("Branch", "Turn", "TypeTonner"), show='headings')
tree.heading("Branch", text="Filial")
tree.heading("Turn", text="Turno")
tree.heading("TypeTonner", text="Tonner")
tree.pack(pady=5)

printer_label = tk.Label(frame, text="Nome da Impressora:")
printer_label.pack(pady=5)

printer_entry = tk.Entry(frame)
printer_entry.pack(pady=5)
printer_entry.insert(0, config.get('printer_name', ''))

print_button = tk.Button(frame, text="Imprimir", command=print_labels)
print_button.pack(pady=5)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(frame, variable=progress_var, maximum=100)
progress_bar.pack(pady=5)

root.mainloop()