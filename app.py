from flask import Flask, render_template, json, url_for, request
from rest_api_initial import *

# mysql = MySQL()
app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        vm=request.form['vms']
        strvm=str(vm)
        intvm=int(vm)
        master=request.form['master']
        cluster=request.form['cluster']

        if int(master) == 1: 
            M='m1.large'
        else:
            M='m1.medium'

        if int(cluster) == 1:
            C='m1.large'
        else:
            C='m1.medium'

        print('VMs: '+strvm+' Master: '+M+' Cluster: '+C)
        create_cluster(intvm, M, C)
    return render_template('index.html', title="Hello", text=["First", "Second"])

# @app.route('/showSignUp')
# def showSignUp():
#     return render_template('signup.html')

# @app.route('/signUp',methods=['POST'])
# def signUp():
 
#     # read the posted values from the UI
#     _name = request.form['inputName']
#     _email = request.form['inputEmail']
#     _password = request.form['inputPassword']
 
#     # validate the received values
#     if _name and _email and _password:
#         return json.dumps({'html':'<span>All fields good !!</span>'})
#     else:
#         return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run(port=5002)
