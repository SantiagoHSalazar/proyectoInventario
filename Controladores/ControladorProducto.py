from Repositorio.RepositorioProducto import RepositorioProducto
from Repositorio.RepositorioCategoria import RepositorioCategoria
from Modelos.Producto import Producto
from Modelos.Categoria import Categoria

class ControladorProducto:
    def __init__(self):
        self.repositorioProducto = RepositorioProducto()
        self.repositorioCategoria = RepositorioCategoria()

    def __index__(self):
        return self.repositorioProducto.findAll()

    def create(self, infoProducto):
        nuevoProducto = Producto(infoProducto)
        return self.repositorioProducto.save()

    def Show(self, id):
        eLProducto = Producto(self.repositorioProducto.findById(id))
        return eLProducto.__dict__

    def update(self, id, infoProducto):
        productoActual = Producto(self.repositorioProducto.findById(id))
        productoActual.nombre = infoProducto["nombre"]
        productoActual.cantidad = infoProducto["cantidad"]
        productoActual.referencia = infoProducto["referencia"]
        productoActual.precio = infoProducto["precio"]
        return self.repositorioProducto.save(productoActual)

    def delete(self,id):
        return self.repositorioProducto.delete(id)

    def asignarCategoria(self,id,id_categoria):
        productoActual = Producto(self.repositorioProducto.findById(id))
        categoriaActual = Categoria(self.repositorioCategoria.findById(id_categoria))
        productoActual.categoria = categoriaActual
        return self.repositorioProducto.save(productoActual)


