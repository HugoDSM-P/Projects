from flask import Flask, render_template, request
import re
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Datos de configuración de la base de datos
db_config = {
    'host': 'localhost',  # Nombre del contenedor o servicio de MySQL en el pod
    'user': 'root',            # Usuario de MySQL
    'password': 'contra',            # Contraseña vacía para root
    'database': 'usuarios'     # Nombre de la base de datos
}

# Función para validar los datos del formulario
def validate_form(email, username, password, phone):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    phone_regex = r'^\d{10}$'
    if not re.match(email_regex, email):
        return "Correo electrónico no válido."
    if len(username) < 3:
        return "El nombre de usuario debe tener al menos 3 caracteres."
    if len(password) < 6:
        return "La contraseña debe tener al menos 6 caracteres."
    if not re.match(phone_regex, phone):
        return "El número de teléfono debe tener 10 dígitos."
    return None

# Función para insertar los datos del formulario en la base de datos
def insert_user(email, username, password, phone):
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**db_config)
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Consulta SQL para insertar el nuevo usuario
            insert_query = """INSERT INTO usuarios (email, usuario, pwd, phone)
                              VALUES (%s, %s, %s, %s)"""
            # Ejecutar la consulta con los datos proporcionados
            cursor.execute(insert_query, (email, username, password, phone))
            connection.commit()
            cursor.close()
            return None
    except Error as e:
        return f"Error al insertar datos: {e}"
    finally:
        if connection.is_connected():
            connection.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        
        validation_error = validate_form(email, username, password, phone)
        if validation_error:
            message = validation_error
        else:
            insert_error = insert_user(email, username, password, phone)
            if insert_error:
                message = insert_error
            else:
                message = f"Registro exitoso para {username}!"
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
