from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEmpleado import ControladorEmpleado
import pymongo
import certifi

app=Flask( __name__ )
cors = CORS(app)
ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://santiagohsalazar:ErgF8KesKgJIcVA8@cluster0.qfgmf.mongodb.net/NOMBREBASEDEDATOS?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)

miControladorEmpleado = ControladorEmpleado()

@app.route("/emplado",methods=['GET'])
def getEmplado():
    json=miControladorEmpleado.index()
    return jsonify(json)

@app.route("/empleado",methods=['POST'])
def crearEmplado():
    data = request.get_json()
    json=miControladorEmpleado.create(data)
    return jsonify(json)

@app.route("/empleado/<string:id>",methods=['GET'])
def getEmpleado(id):
    json=miControladorEmpleado.show(id)
    return jsonify(json)

@app.route("/empleado/<string:id>",methods=['PUT'])
def modificarEmpleado(id):
    data = request.get_json()
    json=miControladorEmpleado.update(id,data)
    return jsonify(json)

@app.route("/empleado/<string:id>",methods=['DELETE'])
def eliminarEmpleado(id):
    json=miControladorEmpleado.delete(id)
    return jsonify(json)

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
