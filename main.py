from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEmpleado import ControladorEmpleado
from Controladores.ControladorCategoria import ControladorCategoria
from Controladores.ControladorProducto import ControladorProducto
from Controladores.ControladorInventario import ControladorInventario
import pymongo
import certifi

app=Flask( __name__ )
cors = CORS(app)
ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://santiagohsalazar:ErgF8KesKgJIcVA8@cluster0.qfgmf.mongodb.net/NOMBREBASEDEDATOS?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)

miControladorEmpleado = ControladorEmpleado()
miControladorCategoria = ControladorCategoria()
miControladorProducto = ControladorProducto()
miControladorInventario = ControladorInventario()


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

####################################################################################

@app.route("/categoria/<string:id>",methods=['GET'])
def getCategorias():
    json = miControladorCategoria.index()
    return jsonify(json)

@app.route("/categoria/<string:id>",methods=['GET'])
def getCategoria(id):
    json=miControladorCategoria.show(id)
    return jsonify(json)

@app.route("/categoria/<string:id>",methods=['POST'])
def crearCategoria():
    data = request.get_json()
    json = miControladorCategoria.create(data)
    return jsonify(json)

@app.route("/categoria/<string:id>",methods=['PUT'])
def modificarCategoria(id):
    data = request.get_json()
    json = miControladorCategoria.update(id, data)
    return jsonify(json)

@app.route("/categoria/<string:id>", methods=['DELETE'])
def eliminarCategoria(id):
    json = miControladorCategoria.delete(id)
    return jsonify(json)
#######################################################################################

@app.route("/producto", methods=['GET'])
def getProductos():
    json = miControladorProducto.index()
    return jsonify(json)

@app.route("/producto/<string:id>", methods=['GET'])
def getProducto(id):
    json = miControladorProducto.show(id)
    return jsonify(json)

@app.route("/producto", methods=['POST'])
def crearProducto():
    data = request.get_json()
    json = miControladorProducto.create(data)
    return jsonify(json)

@app.route("/producto/<string:id>", methods=['PUT'])
def modificarProducto(id):
    data = request.get_json()
    json = miControladorProducto.update(id, data)
    return jsonify(json)

@app.route("/producto/<string:id>", methods=['DELETE'])
def eliminarProducto(id):
    json = miControladorProducto.delete(id)
    return jsonify(json)

@app.route("/producto/<string:id>/categoria/<string:id_categoria>", methods=['PUT'])
def asignarCategoriaAProducto(id, id_categoria):
    json = miControladorProducto.asignarCategoria(id, id_categoria)
    return jsonify(json)
#######################################################################################################

@app.route("/inventario", methods=['GET'])
def getInventarios():
    json = miControladorInventario.index()
    return jsonify(json)


@app.route("/inventario/<string:id>", methods=['GET'])
def getInventario(id):
    json = miControladorInventario.show(id)
    return jsonify(json)

@app.route("/inventario/empleado/<string:identificacion>/producto/<string:id_producto>", methods=['POST'])
def crearInventario(identificacion, id_producto):
    data = request.get_json()
    json = miControladorInventario.create(data, identificacion, id_producto)
    return jsonify(json)


@app.route("/inventario/<string:id_inventario>/empleado/<string:identificacion>/producto/<string:id_producto>", methods=['PUT'])
def modificarInventario(id_inventario, identificacion, id_producto):
    data = request.get_json()
    json = miControladorInventario.update(id_inventario, data, identificacion, id_producto)
    return jsonify(json)

@app.route("/inventario/<string:id_inventario>", methods=['DELETE'])
def eliminarInventario(id_inventario):
    json = miControladorInventario.delete(id_inventario)
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
