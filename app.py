from flask import Flask, request, jsonify, url_for


app = Flask(__name__)


@app.route('/register', methods=['GET','POST'])
def registration():
    return "registration"

@app.route('/', methods=['GET','POST'])
def login():
    return "login"

@app.route('/logout', methods=['GET','POST'])
def logout():
    return jsonify({'message':'bye'})



if __name__=="__main__":
    app.run()
