from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

dbfile = open('db', 'wb')
pickle.dump([], dbfile)    
dbfile.close()

@app.route('/')
def hello_world():
    return 'pynq Z1!'


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

        if(len(data)==20):
            del data[0:10]
        

        data.append(res)

        dbfile = open('db', 'wb')
        pickle.dump(data, dbfile)          
        dbfile.close()

        return jsonify(data)

    # if request.method=="POST":
    #     field1 = request.args.get('field1')
    #     field2 = request.args.get('field2')
    #     field3 = request.args.get('field3')

    #     res = [field1, field2, field3]

    #     dbfile = open('db', 'rb')
    #     data = pickle.load(dbfile)
    #     dbfile.close()

    #     data.append(res)

    #     dbfile = open('db', 'wb')
    #     pickle.dump(data, dbfile)          
    #     dbfile.close()

    #     return jsonify(data)

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