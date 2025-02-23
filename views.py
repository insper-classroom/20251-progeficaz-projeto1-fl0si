from utils import *

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title = dados[1], details = dados[2], id = dados[0])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):  
    add_note(titulo,detalhes)

def delete(note_id):
    delete_note(note_id)

def edit_page(id):
    note = [dados for dados in load_data() if dados[0] == id][0]
    return load_template('edit.html').format(titulo = note[1], detalhes = note[2], id = note[0])

def save_note(titulo, detalhes, id):
    editar_notedb(titulo, detalhes ,id)

