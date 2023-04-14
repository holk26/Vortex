# Vortex

# Dependencias 


Django     4.2    
psycopg2   2.9.6  


Activar el entorno virtual Ejecuta el siguiente comando  en la consola en la carpeta raiz de del proyecto 

<code>.\venv\Scripts\activate</code>

Si genera error ejecuta esto en con permisos de administrador

<code>Set-ExecutionPolicy Unrestricted</code>

para visualisar los cambios en el administrador de django 

python manage.py createsuperuser

http://127.0.0.1:8000/admin/login/?next=/admin/



# configurar la base de datos Trasporte/settings.py 
Linea: 77 
<code>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'trasporte',
        'USER': 'postgres',
        'PASSWORD': 'holk',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
</code>
y ejecutar las migraciones 

crear una BD en postgreSQL: trasporte

 python manage.py makemigrations

 python manage.py migrate       

Http

# GET
<code>
http://127.0.0.1:8000/api/conductor/
http://127.0.0.1:8000/api/pedido/
http://127.0.0.1:8000/api/vehiculos/
</code>
agregar id al final para ver solo un registro


# POST
<code>
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
</code>
# PUT 
<code>
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
</code>
# DELETE 
<code>

http://127.0.0.1:8000/api/conductor/1
http://127.0.0.1:8000/api/pedido/1
http://127.0.0.1:8000/api/vehiculos/1

</code>

