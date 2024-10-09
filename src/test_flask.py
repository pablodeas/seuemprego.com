from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Aqui você pode obter os dados de vaga.html
    vagas = [{"Titulo": "", "Descricao": "", "Criacao": "", "Contato": ""}]
    
    return render_template('index.html', vagas=vagas)

if __name__ == '__main__':
    app.run(debug=True)
