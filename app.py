from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    # Estructuras de datos (puedes cambiar estos textos por tus datos reales)
    nombre_estudiante = "Jabes"
    
    # Uso de un Diccionario para los apellidos
    apellidos_estudiante = {
        "primer": "Nolasco",
        "segundo": "Rosario"
    }
    
    # Uso de Listas para asignaturas y hobbies (mínimo 2)
    lista_asignaturas = ["MACHINE LEARNING"]
    lista_hobbies = ["Videojuegos", "Tocar guitarra", "Leer"]
    
    # Enviar la información desde Flask al template
    return render_template('index.html', 
                           nombre=nombre_estudiante, 
                           apellidos=apellidos_estudiante, 
                           asignaturas=lista_asignaturas, 
                           hobbies=lista_hobbies)

if __name__ == '__main__':
    app.run(debug=True)