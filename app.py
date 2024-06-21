from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    session.clear()
    return render_template('section1.html')

@app.route('/section1', methods=['GET', 'POST'])
def section1():
    if request.method == 'POST':
        session['filename'] = request.form['filename']
        session['response1'] = request.form['response1']
        session['response2'] = request.form['response2']
        session['response3'] = request.form['response3']
        return redirect(url_for('section2'))
    return render_template('section1.html')

@app.route('/section2', methods=['GET', 'POST'])
def section2():
    if request.method == 'POST':
        session['response4'] = request.form['response4']
        session['response5'] = request.form['response5']
        session['response6'] = request.form['response6']
        return redirect(url_for('section3'))
    return render_template('section2.html')

@app.route('/section3', methods=['GET', 'POST'])
def section3():
    if request.method == 'POST':
        session['response7'] = request.form['response7']
        session['response8'] = request.form['response8']
        session['response9'] = request.form['response9']
        session['response10'] = request.form['response10']
        return redirect(url_for('section4'))
    return render_template('section3.html')

@app.route('/section4', methods=['GET', 'POST'])
def section4():
    if request.method == 'POST':
        session['response11'] = request.form['response11']
        session['response12'] = request.form['response12']
        session['response13'] = request.form['response13']
        session['response14'] = request.form['response14']
        session['response15'] = request.form['response15']
        return redirect(url_for('section5'))
    return render_template('section4.html')

@app.route('/section5', methods=['GET', 'POST'])
def section5():
    if request.method == 'POST':
        session['response16'] = request.form['response16']
        return redirect(url_for('section6'))
    return render_template('section5.html')

@app.route('/section6', methods=['GET', 'POST'])
def section6():
    if request.method == 'POST':
        session['response17'] = request.form['response17']
        session['response18'] = request.form['response18']
        session['response19'] = request.form['response19']
        session['response20'] = request.form['response20']
        return redirect(url_for('section7'))
    return render_template('section6.html')

@app.route('/section7', methods=['GET', 'POST'])
def section7():
    if request.method == 'POST':
        session['response21'] = request.form['response21']
        session['response22'] = request.form['response22']
        session['response23'] = request.form['response23']
        return redirect(url_for('summary'))
    return render_template('section7.html')

@app.route('/summary')
def summary():
    filename = session.get('filename')
    responses = {k: session[k] for k in session if k.startswith('response')}
    with open(filename, 'w') as f:
        for key, response in responses.items():
            f.write(f"{key}: {response}\n")
    return render_template('summary.html', filename=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
