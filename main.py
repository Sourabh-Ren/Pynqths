from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

dbfile = open('db', 'wb')
pickle.dump([["field1", "field2", "field3"]], dbfile)    
dbfile.close()

@app.route('/')
def hello_world():
    return 'Rohit is great!'

# @app.route('/update/<int:sno>', methods=['GET','POST'])
# def update(sno):
#     res = {
#         "num":sno
#     }
#     return res

# @app.route('/postsend', methods=['GET','POST'])
# def postsend():
#     if request.method=="POST":
#         email = request.form.get('email')
#         password = request.form.get('password')
#         res = {
#             "email": email,
#             "password": password
#         }
#         return res

@app.route('/querydata', methods=['GET','POST'])
def querydata():
    if request.method=="GET":
        field1 = request.args.get('field1')
        field2 = request.args.get('field2')
        field3 = request.args.get('field3')

        res = [field1, field2, field3]

        dbfile = open('db', 'rb')
        data = pickle.load(dbfile)
        dbfile.close()

        data.append(res)

        dbfile = open('db', 'wb')
        pickle.dump(data, dbfile)          
        dbfile.close()

        return jsonify(data)

    if request.method=="POST":
        field1 = request.args.get('field1')
        field2 = request.args.get('field2')
        field3 = request.args.get('field3')

        res = [field1, field2, field3]

        dbfile = open('db', 'rb')
        data = pickle.load(dbfile)
        dbfile.close()

        data.append(res)

        dbfile = open('db', 'wb')
        pickle.dump(data, dbfile)          
        dbfile.close()

        return jsonify(data)

@app.route('/getdata', methods=['GET','POST'])
def getdata():
    if request.method=="GET":
        dbfile = open('db', 'rb')
        data = pickle.load(dbfile)
        return jsonify(data)

# @app.route('/postsendjson', methods=['GET','POST'])
# def postsendjson():
#     if request.method=="POST":
#         data = request.get_json()
#         return data

if __name__ == "__main__":
    app.run(debug=True, port=8000)