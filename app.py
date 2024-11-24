# Importación de Flask y funciones necesarias
from flask import Flask, render_template, request

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    # Renderiza la plantilla HTML para la página principal
    return render_template('index.html')

# Ruta para el formulario de cálculo de pintura (Ejercicio 1)
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None  # Variable para almacenar el resultado del cálculo
    if request.method == 'POST':  # Verifica si el formulario fue enviado
        # Obtención de los valores enviados en el formulario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        # Definición del precio unitario de cada tarro de pintura
        precio_unitario = 9000
        total_sin_descuento = tarros * precio_unitario  # Cálculo del precio total sin descuento

        # Aplicación de descuentos según la edad del usuario
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15  # Descuento del 15% para edades entre 18 y 30
        elif edad > 30:
            descuento = total_sin_descuento * 0.25  # Descuento del 25% para mayores de 30 años
        else:
            descuento = 0  # Sin descuento para menores de 18

        # Cálculo del total con el descuento aplicado
        total_con_descuento = total_sin_descuento - descuento

        # Creación de un diccionario con los resultados del cálculo
        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento': descuento,
            'total_con_descuento': total_con_descuento
        }
    # Renderiza la plantilla del ejercicio 1 con los resultados
    return render_template('ejercicio1.html', resultado=resultado)

# Ruta para el formulario de inicio de sesión (Ejercicio 2)
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None  # Variable para almacenar el mensaje de resultado
    # Diccionario con usuarios y contraseñas predefinidos
    usuarios = {'juan': 'admin', 'pepe': 'user'}
    if request.method == 'POST':  # Verifica si el formulario fue enviado
        # Obtención de los valores enviados en el formulario
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        # Validación de usuario y contraseña
        if usuario in usuarios and usuarios[usuario] == contraseña:
            # Mensaje según el tipo de usuario
            if usuario == 'juan':
                mensaje = f"Bienvenido Administrador {usuario}"
            else:
                mensaje = f"Bienvenido Usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos."  # Mensaje de error
    # Renderiza la plantilla del ejercicio 2 con el mensaje
    return render_template('ejercicio2.html', mensaje=mensaje)

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración







