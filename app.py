from flask import Flask, request, render_template

app = Flask(__name__)


satuan = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

# Fungsi yang menerima nilai, satuan awal, dan satuan akhir
def calculate_konversi(n, unit_from, unit_to):
    try:
        index_from = satuan.index(unit_from)
        index_to = satuan.index(unit_to)
    except ValueError:
        return "Satuan tidak valid"
    difference = index_to - index_from
    factor =  10 ** difference 
    return n * factor

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            number = int(request.form.get('number'))
            satuan_awal = request.form.get('satuan_awal')
            satuan_akhir = request.form.get('satuan_akhir')

            result = calculate_konversi(number, satuan_awal, satuan_akhir)

        except ValueError:
            result = "Input angka tidak valid."
            
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


