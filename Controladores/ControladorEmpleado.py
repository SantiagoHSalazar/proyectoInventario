from Repositorio.RepositorioEmpleado import RepositorioEmpleado
from Modelos.Empleado import Empleado


class ControladorEmpleado():
    def __init__(self):
        self.repositorioEmpleado = RepositorioEmpleado()

    def index(self):
        return self.repositorioEmpleado.findAll()

    def create(self, infoEmpleado):
        nuevoEmpleado = Empleado(infoEmpleado)
        return self.repositorioEmpleado.save(nuevoEmpleado)

    def show(self, id):
        elEmpleado = Empleado(self.repositorioEmpleado.findById(id))
        return elEmpleado.__dict__

    def update(self, id, infoEmpleado):
        empleadoActual = Empleado(self.repositorioEmpleado.findById(id))
        empleadoActual.identificacion = infoEmpleado["identificacion"]
        empleadoActual.nombre = infoEmpleado["nombre"]
        empleadoActual.apellido = infoEmpleado["apellido"]
        empleadoActual.direccion = infoEmpleado["direccion"]
        empleadoActual.correo = infoEmpleado["correo"]
        return self.repositorioEmpleado.save(empleadoActual)

    def delete(self, id):
        return self.repositorioEmpleado.delete(id)
