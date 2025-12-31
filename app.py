from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    nama = ""
    
    if request.method == 'POST':
        nama = request.form.get('input_nama')

        return render_template('hasil.html', data_nama=nama)
    
    return render_template('index.html', data_nama=nama)

if __name__ == '__main__':
    app.run(debug=True)