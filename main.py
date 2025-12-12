#!/usr/bin/env python3

""" 
    Project:        seuemprego.com
    Author:         Pablo Andrade
    Created:        12/12/2025
    Version:        0.0.1
    Objective:      A fast and simple job website
    Last Change:    
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from database import Session, init_db
from models import Vagas

app = Flask(__name__)
app.secret_key = ''

@app.route('/')
def index():
    """Página principal com lista de vagas"""
    session = Session()
    try:
        vagas = session.query(Vagas).order_by(Vagas.created_at.desc()).all()
        return render_template('index.html', vagas=vagas)
    finally:
        session.close()


@app.route('/nova-vaga')
def nova_vaga():
    """Página com formulário para adicionar nova vaga"""
    return render_template('nova_vaga.html')


@app.route('/adicionar-vaga', methods=['POST'])
def adicionar_vaga():
    """Processa o formulário e adiciona a vaga no banco"""
    session = Session()
    try:
        nova_vaga = Vagas(
            titulo_vaga=request.form.get('titulo_vaga'),
            cargo=request.form.get('cargo'),
            regime_contratacao=request.form.get('regime_contratacao'),
            numero_vagas=int(request.form.get('numero_vagas', 1)),
            descricao=request.form.get('descricao'),
            experiencia_desejada=request.form.get('experiencia_desejada'),
            forma_trabalho=request.form.get('forma_trabalho'),
            local=request.form.get('local'),
            beneficios=request.form.get('beneficios'),
            expediente=request.form.get('expediente'),
            salario=request.form.get('salario'),
            como_candidatar=request.form.get('como_candidatar')
        )
        session.add(nova_vaga)
        session.commit()
        flash('Vaga adicionada com sucesso!', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        session.rollback()
        flash(f'Erro ao adicionar vaga: {str(e)}', 'error')
        return redirect(url_for('nova_vaga'))
    finally:
        session.close()


@app.route('/vaga/<int:vaga_id>')
def detalhes_vaga(vaga_id):
    """Página com detalhes completos da vaga"""
    session = Session()
    try:
        vaga = session.query(Vagas).filter(Vagas.id == vaga_id).first()
        if not vaga:
            flash('Vaga não encontrada', 'error')
            return redirect(url_for('index'))
        return render_template('detalhes_vaga.html', vaga=vaga)
    finally:
        session.close()


def main():
    """Inicializa o banco de dados e inicia o servidor"""
    print("Inicializando banco de dados...")
    init_db()
    print("Banco de dados pronto!")
    print("Iniciando servidor Flask...")
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()