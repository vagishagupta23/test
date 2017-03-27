from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def temp():
    if request.method == 'GET':
        return render_template('heyaa.html')
    

@app.route('/result', methods=['POST','GET'])
def hello():
    ls=['amit','rishab','prateek','rahul'];
    if request.method == 'POST':
        return render_template('check.html', name=ls)
    
if __name__ == '__main__':
   app.run(debug=True)
        
