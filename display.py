from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def temp():
    if request.method == 'GET':
        return render_template('text.html')
    elif request.method == 'POST':
        return redirect(url_for('hello'))
    

@app.route('/result/<user>', methods=['POST','GET'])
def hello(user):
    user = request.form['text']
    return render_template('display.html', text=user)
    
if __name__ == '__main__':
   app.run(debug=True)
        
