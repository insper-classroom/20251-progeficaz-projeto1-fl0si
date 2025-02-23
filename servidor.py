from flask import Flask, render_template_string, request, redirect
from utils import *
import views

app = Flask(__name__)





app.static_folder = 'static'    



@app.route('/')
def index():
    
    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  
    detalhes = request.form.get('detalhes')  

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):

    views.delete(id)
    return redirect('/')

@app.route('/update_page/<int:id>', methods=['GET'])
def update_page (id):

    return render_template_string(views.edit_page(id))


@app.route('/edit_note/<int:id>', methods=['POST'])
def atualizar(id):
    titulo = request.form.get('titulo')  
    detalhes = request.form.get('detalhes')  

    views.save_note(titulo, detalhes, id)
    return redirect('/')



if __name__ == '__main__':
    init_db()
    app.run(debug=True)
