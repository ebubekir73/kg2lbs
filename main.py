from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

def convert_kg_to_lbs(kg):
    return kg * 2.2

def convert_lbs_to_kgs(bro):
    return bro * 0.45


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/submit', methods=['POST'])
def convert():
    selected_option = request.form.get('option')
    kg = float(request.form['kilograms'])
    bro = float(request.form['kilograms'])
    lbs = convert_kg_to_lbs(kg)
    kgs = convert_lbs_to_kgs(bro)

    if selected_option == "kilos":
        return render_template('pound.html', lbs=lbs)
    
    if selected_option == "pounds":
        return render_template('kilo.html', kgs=kgs)
    
    
if __name__ == '__main__':
    app.run(debug=True)



