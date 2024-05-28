from Modelos.Inventario import Inventario
from Modelos.Empleado import Empleado
from Modelos.Producto import Producto
from Repositorio.RepositorioInventario import RepositorioInventario
from Repositorio.RepositorioEmpleado import RepositorioEmpleado
from Repositorio.RepositorioProducto import RepositorioProducto

class ControladorInventario():
    def __init__(self):
        self.repositorioInventario = RepositorioInventario()
        self.repositorioEmpleado = RepositorioEmpleado()
        self.repositorioProducto = RepositorioProducto()

    def index(self):
        return self.repositorioInventario.findAll()

    def create(self, infoInventario, id_empleado, id_producto):
        nuevoInventario = Inventario(infoInventario)
        elEmpleado = Empleado(self.repositorioEmpleado.findById(id_empleado))
        elProducto = Producto(self.repositorioProducto.findById(id_producto))
        nuevoInventario.empleado = elEmpleado
        nuevoInventario.producto = elProducto
        return self.repositorioInventario.save(nuevoInventario)

    def show(self, id):
        elInventario = Inventario(self.repositorioInventario.findById(id))
        return elInventario.__dict__

    def update(self, id, infoInventario, id_empleado, id_producto):
        elInventario = Inventario(self.repositorioInventario.findById(id))
        elInventario.fecha = infoInventario["fecha"]
        elInventario.cantidad = infoInventario["cantidad"]
        elInventario.cantidadEnStock = infoInventario["cantidad_en_stock"]
        elInventario.observacion = infoInventario["observacion"]
        elEmpleado = Empleado(self.repositorioEmpleado.findById(id_empleado))
        elProducto = Producto(self.repositorioProducto.findById(id_producto))
        elInventario.empleado = elEmpleado
        elInventario.producto = elProducto
        return self.repositorioInventario.save(elInventario)

    def delete(self, id):
        return self.repositorioInventario.delete(id)
