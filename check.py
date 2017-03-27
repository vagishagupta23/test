from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def temp():
    if request.method == 'GET':
        return render_template('heyaa.html')
    elif request.method == 'POST':
        return redirect(url_for('hello'))
    

@app.route('/result', methods=['POST','GET'])
def hello():
    ls=['amit','rishab','prateek','rahul'];
    return render_template('check.html', name=ls)
    
if __name__ == '__main__':
   app.run(debug=True)
        
