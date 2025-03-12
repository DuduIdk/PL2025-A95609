import json
import re
import tabulate 

STOCK_FILE = "stock.json"

tokens = [
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
    ]

def t_LISTAR():
    r'LISTAR'
    
    table = []
    for cod, values in stock.items():
        table.append()
    print(tabulate)

def load_stock():
    try:
        with open(STOCK_FILE, "r", encoding = "utf-8") as f:
            json.load(f)
    except  FileNotFoundError:
        return []
    
def save_stock():
    with open(STOCK_FILE, "w", encoding = "utf-8") as f:
        json.dump(stock, f, indent = 4)

