import json
from flask import request
import sqlite3

def load_data (arquivo):
    with open(f'static/data/{arquivo}', 'r') as f:
        response = json.load(f)
    return response 
 
def load_template (nome_arquivo):
    with open(f"static/templates/{nome_arquivo}", 'r') as f:
        response = f.read()
    return response 

def add_note (titulo, detalhes):
    
    with open('static/data/notes.json', 'r') as j:
        notes = json.load(j)
    params = {
        'titulo': titulo,
        'detalhes': detalhes,
    }
    notes.append(params)

    with open('static/data/notes.json', 'w') as j:
        json.dump(notes,j)
              
    return notes



def init_db():
    conn = sqlite3.connect("static/data/app.db")
    cursor = conn.cursor()
    
    # Criação da tabela notes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            detalhes TEXT NOT NULL
        );
    """)
    
    conn.commit()
    conn.close()
