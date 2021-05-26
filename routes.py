#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PF005
Objetivos:
- Mostrar quão frágil é a segurança de dados hoje em dia e como, com uma simples engenharia social, podemos conseguir dados importantes de uma pessoa.

"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField # Os validadores são usados para garantir que as entradas sejam o que a gente espera.
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask import render_template, Blueprint, redirect, url_for, flash, request
from flask import Flask, render_template, abort
app = Flask(__name__)
app.config['SECRET_KEY'] = 'minhasenha'

class Form(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

@app.route("/", methods=['GET','POST'])
def index():
    form = Form()
    if form.validate_on_submit():
        print(f'Usuario: {form.usuario.data} \nSenha: {form.senha.data}')
        return render_template('site.html')
    else:
        print('não validou')

    return render_template('index.html',form=form)
    # return "Hello"

app.run(host='localhost', port=5002, debug=True)

# if __name__ == '__main__':
#     app.run()
