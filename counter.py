from flask import Flask, render_template, session, redirect, request
app=Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/addclick', methods=['POST'])
def addclick():
    session['bruh'] = request.form['add']
    session['number_of_clicks'] = request.form['numclicks']

    if 'bruh' in session:
        print('yay')
    else:
        print('dam bruh that key dont exist')
    
    return redirect('/')

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)