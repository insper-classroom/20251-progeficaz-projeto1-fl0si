import json
from flask import request
import sqlite3 as sql

def load_data():
    con = sql.connect('static/data/app.db')
    notes = con.execute('SELECT titulo, detalhes FROM notes').fetchall()
    con.close()
    return notes

def load_template (nome_arquivo):
    with open(f"static/templates/{nome_arquivo}", 'r') as f:
        return f.read() 

def add_note(titulo, detalhes):
    conn = sql.connect("static/data/app.db")
    cursor = conn.cursor()
    
    # Insere a nova nota no banco
    cursor.execute("INSERT INTO notes (titulo, detalhes) VALUES (?, ?)", (titulo, detalhes))
    conn.commit()
    conn.close()
    
    # Retorna a lista atualizada de notas
    return load_data()



def init_db():
    conn = sql.connect("static/data/app.db")
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

def delete_note(note_id):
    conn = sql.connect("static/data/app.db")
    cursor = conn.cursor()
    
    # Remove a nota com base no ID
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    
    # Retorna a lista atualizada de notas
    return load_data()