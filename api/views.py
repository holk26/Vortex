#from django.shortcuts import render
import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Driver, Order, Vehicle

# Create your views here.

class TrasporteView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        try:
            if (id>0):
                conductores = list(Driver.objects.filter(id=id).values())
                if len(conductores) > 0:
                    conductor = conductores[0]
                    datos = {'message': "Success", 'conductor': conductor}
                else:
                    datos = {'message': "Conductores not found.."}
                return JsonResponse(datos)
            else:
                conductores = list(Driver.objects.values())
                if len(conductores) > 0:
                    datos = {'message': "Success", 'conductores': conductores}
                else:
                    datos = {'message': "Conductores not found.."}
        except Exception as e:
            datos = {'message': str(e)}
        return JsonResponse(datos)

    def post(self, request):
        try:
            jd = json.loads(request.body)
            Driver.objects.create(identificacion=jd['identificacion'], apellido=jd['apellido'], nombre=jd['nombre'], telefono=jd['telefono'], direccion=jd['direccion'])
            datos = {'message': "Success"}
        except Exception as e:
            datos = {'message': str(e)}
        return JsonResponse(datos)

    def put(self, request, id):
        try:
            jd = json.loads(request.body)
            conductores = list(Driver.objects.filter(id=id).values())
            if len(conductores)>0:
                conductor = Driver.objects.get(id=id)
                conductor.identificacion = jd['identificacion']
                conductor.apellido = jd['apellido']
                conductor.nombre = jd['nombre']
                conductor.telefono = jd['telefono']
                conductor.direccion = jd['direccion']
                conductor.save()
                datos = {'message': "Success"}
            else:
                datos = {'message': "Conductor not found.."}
            
        except Exception as e:
            datos = {'message': str(e)}
        return JsonResponse(datos)

    def delete(self, request, id):
        try:
            conductores = list(Driver.objects.filter(id=id).values())
            if len(conductores)>0:
                Driver.objects.filter(id=id).delete()
                datos = {'message': "Success"}
            else:
                datos = {'message': "Conductor not found.."}
        except Exception as e:
            datos = {'message': str(e)}

        return JsonResponse(datos)


class PedidoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        try:
            if (id>0):
                ordenes = list(Order.objects.filter(id=id).values())
                if len(ordenes) > 0:
                    orden = ordenes[0]
                    datos = {'message': "Success", 'conductor': orden}
                else:
                    datos = {'message': "Pedido not found.."}
                return JsonResponse(datos)
            else:
                ordenes = list(Order.objects.values())
                if len(ordenes) > 0:
                    datos = {'message': "Success", 'pedidos': ordenes}
                else:
                    datos = {'message': "Pedido not found.."}
        except Exception as e:
            datos = {'message': str(e)}
        return JsonResponse(datos)

    def post(self, request):
        try:
            jd = json.loads(request.body)
            
            # Verificar que los campos obligatorios no estén vacíos
            if not jd.get('tipo_pedido'):
                raise ValueError('El campo tipo_pedido es obligatorio')
            if not jd.get('direccion'):
                raise ValueError('El campo direccion es obligatorio')
            if not jd.get('conductor_id'):
                raise ValueError('El campo conductor_id es obligatorio')
            
            # Verificar que el conductor existe en la base de datos
            driver_id = jd['conductor_id']
            try:
                driver = Driver.objects.get(id=driver_id)
            except Driver.DoesNotExist:
                raise ValueError(f'El conductor con ID {driver_id} no existe')
            
            # Crear la orden
            order = Order.objects.create(tipo_pedido=jd['tipo_pedido'], direccion=jd['direccion'], conductor=driver)
            datos = {'message': "Success", 'order_id': order.id}
        except ValueError as e:
            datos = {'message': str(e)}
        except Exception as e:
            datos = {'message': str(e)}
        return JsonResponse(datos)


    def put(self, request, id):
        try:
            jd = json.loads(request.body)
            order = Order.objects.get(id=id)
            if 'tipo_pedido' in jd:
                order.tipo_pedido = jd['tipo_pedido']
            if 'direccion' in jd:
                order.direccion = jd['direccion']
            if 'conductor_id' in jd:
                driver_id = jd['conductor_id']
                try:
                    driver = Driver.objects.get(id=driver_id)
                    order.conductor = driver
                except Driver.DoesNotExist:
                    datos = {'message': "Driver not found.."}
                    return JsonResponse(datos)
            order.save()
            datos = {'message': "Success"}
        except Order.DoesNotExist:
            datos = {'message': "Order not found.."}
        except Exception as e:
            datos = {'message': str(e)}
        return JsonResponse(datos)


    def delete(self, request, id):
        try:
            order = Order.objects.get(id=id)
            order.delete()
            datos = {'message': "Success"}
        except Order.DoesNotExist:
            datos = {'message': "Order not found.."}
        except Exception as e:
            datos = {'message': str(e)}
        return JsonResponse(datos)

    


class VehiculoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        try:
            if (id>0):
                vehiculos = list(Vehicle.objects.filter(id=id).values())
                if len(vehiculos) > 0:
                    vehiculo = vehiculos[0]
                    datos = {'message': "Success", 'vehiculo': vehiculo}
                else:
                    datos = {'message': "Vehículo no encontrado."}
                return JsonResponse(datos)
            else:
                vehiculos = list(Vehicle.objects.values())
                if len(vehiculos) > 0:
                    datos = {'message': "Success", 'vehiculos': vehiculos}
                else:
                    datos = {'message': "Vehículos no encontrados."}
        except Exception as e:
            datos = {'message': str(e)}
        return JsonResponse(datos)

    def post(self, request):
        try:
            jd = json.loads(request.body)
            driver_id = jd['conductor_id']
            driver = Driver.objects.get(id=driver_id)

            # Verificar si la placa ya existe
            if Vehicle.objects.filter(placa=jd['placa']).exists():
                datos = {'message': "La placa ya existe"}
            else:
                vehicle = Vehicle.objects.create(
                    modelo=jd['modelo'], 
                    placa=jd['placa'], 
                    capacidad=jd['capacidad'], 
                    conductor=driver
                )
                datos = {'message': "Success", 'vehicle_id': vehicle.id}
        except Driver.DoesNotExist:
            datos = {'message': "Conductor no encontrado"}
        except Exception as e:
            datos = {'message': str(e)}
        return JsonResponse(datos)

    def put(self, request, id):
        try:
            jd = json.loads(request.body)
            vehicles = list(Vehicle.objects.filter(id=id).values())
            if len(vehicles)>0:
                vehicle = Vehicle.objects.get(id=id)
                if 'modelo' in jd:
                    vehicle.modelo = jd['modelo']
                if 'placa' in jd:
                    vehicle.placa = jd['placa']
                if 'capacidad' in jd:
                    vehicle.capacidad = jd['capacidad']
                if 'conductor_id' in jd:
                    driver_id = jd['conductor_id']
                    driver = Driver.objects.get(id=driver_id)
                    vehicle.conductor = driver
                vehicle.save()
                datos = {'message': "Success"}
            else:
                datos = {'message': "Vehicle not found.."}
        except Driver.DoesNotExist:
            datos = {'message': "Driver not found.."}
        except Exception as e:
            datos = {'message': str(e)}
        return JsonResponse(datos)


    def delete(self, request, id):
        try:
            vehicles = list(Vehicle.objects.filter(id=id).values())
            if len(vehicles) > 0:
                Vehicle.objects.filter(id=id).delete()
                datos = {'message': "Success"}
            else:
                datos = {'message': "Vehicle not found.."}
        except Exception as e:
            datos = {'message': str(e)}
        return JsonResponse(datos)


