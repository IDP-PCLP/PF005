"""
PF005
Objetivos:
- Mostrar quão frágil é a segurança de dados hoje em dia e como, com uma simples engenharia social, podemos conseguir dados importantes de uma pessoa.

"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
        return 'Hello, World!'


if __name__ == '__main__':
    app.run()
