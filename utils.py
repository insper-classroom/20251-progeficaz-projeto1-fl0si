import json
from flask import request
import sqlite3 as sql

def load_data():
    con = sql.connect('static/data/app.db')
    notes = con.execute('SELECT * FROM notes').fetchall()
    con.close()
    return notes


def load_template (nome_arquivo):
    with open(f"static/templates/{nome_arquivo}", 'r') as f:
        return f.read() 

def add_note(titulo, detalhes):
    conn = sql.connect("static/data/app.db")
    cursor = conn.cursor()
    
    
    cursor.execute("INSERT INTO notes (titulo, detalhes) VALUES (?, ?)", (titulo, detalhes))
    conn.commit()
    conn.close()
    
    
    return load_data()



def init_db():
    conn = sql.connect("static/data/app.db")
    cursor = conn.cursor()
    
   
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
    
    
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    
    
    return load_data()

def editar_notedb(titulo, detalhe, id):
    conn = sql.connect("static/data/app.db")
    cursor = conn.cursor()
    
    
    cursor.execute(f"UPDATE notes SET TITULO = '{titulo}', DETALHES = '{detalhe}' WHERE ID = {id};")      
    conn.commit()
    conn.close()
    
    
    return load_data()




