# Vortex

# Dependencias 

asgiref    3.6.0  
Django     4.2    
pip        23.0.1 
psycopg2   2.9.6  
setuptools 65.5.0 
sqlparse   0.4.3  
tzdata     2023.3 


ejecutar venv 
Vortex/venv/Scripts/python.exe

para visualisar los cambios en el administrador de django 

python manage.py createsuperuser

http://127.0.0.1:8000/admin/login/?next=/admin/



Http

# GET

http://127.0.0.1:8000/api/conductor/
http://127.0.0.1:8000/api/pedido/
http://127.0.0.1:8000/api/vehiculos/

agregar id al final para ver solo un registro


# POST

http://127.0.0.1:8000/api/conductor/
{
  "identificacion": "12312",
  "apellido": "holk",
  "nombre": "gato",
  "telefono": "12312",
  "direccion": "cra 123"
}


http://127.0.0.1:8000/api/pedido/
{
  "tipo_pedido": "prueba21",
  "direccion": "Cra 17  66-41dd",
  "conductor_id": 1
}


http://127.0.0.1:8000/api/vehiculos/
{
    "modelo": "2020",
    "placa": "ABC1234",
    "capacidad": "4"
}

# PUT 

http://127.0.0.1:8000/api/conductor/1
{
  "identificacion": "12312",
  "apellido": "holk",
  "nombre": "gato",
  "telefono": "12312",
  "direccion": "cra 123"
}


http://127.0.0.1:8000/api/pedido/1
{
  "tipo_pedido": "prueba21",
  "direccion": "Cra 17  66-41dd",
  "conductor_id": 1
}


http://127.0.0.1:8000/api/vehiculos/1
{
    "modelo": "2020",
    "placa": "ABC1234",
    "capacidad": "4"
}

# DELETE 


http://127.0.0.1:8000/api/conductor/1
http://127.0.0.1:8000/api/pedido/1
http://127.0.0.1:8000/api/vehiculos/1