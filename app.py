from flask import Flask, render_template


app = Flask(__name__)

@app.route('/equipe', methods=['GET', 'POST'])
def equipe():

   return render_template('equipe.html')

if __name__ == '__main__':
    app.run(debug=True)