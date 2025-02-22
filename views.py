from utils import load_data, load_template, add_note

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title = dados[0], details = dados[1])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):  
    add_note(titulo,detalhes)