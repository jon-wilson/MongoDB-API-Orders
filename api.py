from flask import Flask, request, json, Response
import Models
from pymongo import MongoClient

app = Flask(__name__)

# Achieving CRUD through API - '/fairfieldudw'
@app.route('/fairfieldudw', methods=['GET'])     # Read MongoDB Document, through API and METHOD - GET
def read_data():
    data = request.args
    if data.get('collection') is None:
        return Response(response=json.dumps({"Error": "Please provide collection information"}), status=400, mimetype='application/json')
    read_obj = Models.FairfieldUDW(data.to_dict(), db)
    response = read_obj.read()
    return Response(response=json.dumps(response), headers={'count': len(response)}, status=200, mimetype='application/json')

@app.route('/fairfieldudw', methods=['POST'])    # Create MongoDB Document, through API and METHOD - POST
def create():
    data = request.json
    if data is None or data == {} or 'document' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}), status=400, mimetype='application/json')
    create_obj = Models.FairfieldUDW(data, db)
    response = create_obj.insert_data(data)
    return Response(response=json.dumps(response), bgstatus=200, mimetype='application/json')

@app.route('/fairfieldudw/', methods=['PUT'])     # Update MongoDB Document, through API and METHOD - PUT
def update():
    data = request.json
    if data is None or data == {} or 'filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}), status=400, mimetype='application/json')
    update_obj = Models.FairfieldUDW(data, db)
    response = update_obj.update_data()
    return Response(response=json.dumps(response), status=200, mimetype='application/json')

@app.route('/fairfieldudw', methods=['DELETE'])   # Delete MongoDB Document, through API and METHOD - DELETE
def delete():
    data = request.json
    if data is None or data == {} or 'filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}), status=400, mimetype='application/json')
    delete_obj = Models.FairfieldUDW(data, db)
    response = delete_obj.delete_data(data)
    return Response(response=json.dumps(response), status=200, mimetype='application/json')

if __name__ == '__main__':
    MONGODB_URI = "mongodb+srv://jwilson:WdYjwEwtlyBWhm1S@atlascluster.a9kqbxc.mongodb.net/test"
    print("...Connecting to MongoDB client")
    client = MongoClient(MONGODB_URI)
    db = client.FairfieldUDW
    print("...Established a connection with MongoDB client")

    app.run(debug=True, port=5000)
        