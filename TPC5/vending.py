import json
import re
import tabulate 

STOCK_FILE = "stock.json"

tokens = [
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR'
    ]

def t_LISTAR(t):
    r'LISTAR'
    
    table = []
    for cod, values in stock.items():
        table.append([cod, values[0], values[1], values[2]])
        
    print(tabulate(table, headers = ["cod", "nome", "quantidade", "preço"]))
    return t

def t_MOEDA(t):
    r'MOEDA\s+((1|2|5|10|20|50)c|(1|2)e)(?:\s*,\s*)'
    
    for moeda in re.finditer(r'(?:(?P<cent>1|2|5|10|20|50)c|(?P<euro>1|2)e)', t.value):
        if moeda.lastgroup == "cent":
            saldo += int(moeda.group("cent"))
        else:
            saldo += int(moeda.group("euro")) * 100
            
    euro, cent = divmod(saldo, 100)
    print(f"Saldo = {euro}e{cent}c")
    
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s+.+'
    
    codigo = t.value.replace(" ", "")[10:]
    produto = stock.get(codigo)
    if not produto:
        print(f"Não existe nenhum produto com código {codigo}")
    elif produto[2] > saldo:
        print("Saldo insuficiente para efetuar o seu pedido")
        saldoEuro, saldoCent = divmod(saldo, 100)
        produtoEuro, produtoCent = divmod(produto[2], 100)
        print(f"Saldo = {saldoEuro}e{saldoCent}c; Pedido = {produtoEuro}e{produtoCent}c")
        
    else:
        print(f"Pode retirar o seu produto: *{item[0]}*")
        saldo -= produto[2]
        euro, cent = divmod(saldo, 100)
        
        if produto[1] == 1:
            del stock[codigo]
        else:
            stock[codigo] = (produto[0], produto[1] - 1, produto[2])
            
    return t

def load_stock():
    try:
        with open(STOCK_FILE, "r", encoding = "utf-8") as f:
            json.load(f)
    except  FileNotFoundError:
        return []

def save_stock():
    with open(STOCK_FILE, "w", encoding = "utf-8") as f:
        json.dump(stock, f, indent = 4)

