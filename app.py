from flask import Flask, render_template

app = Flask(__name__)

@app.route('/equipe', methods=['GET', 'POST'])
def equipe():
    # methods=['GET', 'POST'] informa ao Flask que esta rota aceita AMBOS os métodos.
    # GET: exibe o formulário vazio (quando o usuário chega na página).
    # POST: processa os dados enviados (quando o usuário clica em "Enviar").
    # Sem essa declaração, Flask aceita apenas GET por padrão.

    # Por enquanto, tratamos só o GET — o processamento do POST vem no Passo 8.
    return render_template('equipe.html')

if __name__ == '__main__':
    app.run(debug=True)