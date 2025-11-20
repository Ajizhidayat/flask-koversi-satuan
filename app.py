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
    
    
    
    
    
# from flask import Flask, request, render_template

# app = Flask(__name__)


# def calculate_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * calculate_factorial(n-1)
    
    
# @app.route('/',methods=['GET','POST'])

# def index():
#     result = None
#     if request.method == 'POST':
#         try:
#             number = int(request.form.get('number'))
#             result = calculate_factorial(number)
#         except ValueError:
#             result ="invalid input. Please enter an integer."
#     return render_template('index.html', result=result)


# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, request, render_template

# app = Flask (__name__)


# def calculate_conversi(n, satuan_awal, satuan_akhir):
#     satuan = ["km","hm","dam","m","dm","cm","mm"]
#     try:
#         index_awal = SATUAN.index(satuan_awal)
#         index_akhir = SATUAN.index(satuan_akhir)

#         selisih_jarak = index_akhir - index_awal
#         faktor = 10 * faktor * selisih_jarak
#         return n * faktor
#     except ValueError:
#         return "satuan tidak valid"

# @app.route('/',methods=['GET','POST'])

# def index():
#     result = None
#     if request.method == 'POST':
#         try:
#             number = float(request.form.get('number'))
#             satuan_awal = request.form.get('satuan_awal')
#             satuan_akhir = request.form.get('satuan_akhir')
#             result = calculate_conversi(number, satuan_awal, satuan_akhir)
#         except ValueError:
#             result ="invalid input. Please enter an integer."
#     return render_template('index.html', result=result)

# if __name__ == "__main__":
#     app.run(debug=True)

