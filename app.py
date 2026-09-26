from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    
    nombre_estudiante = "Jabes"
    
    
    apellidos_estudiante = {
        "primer": "Nolasco",
        "segundo": "Rosario"
    }
    
    
    lista_asignaturas = ["MACHINE LEARNING"]
    lista_hobbies = ["Videojuegos", "Tocar guitarra", "Leer"]
    
    
    return render_template('index.html', 
                           nombre=nombre_estudiante, 
                           apellidos=apellidos_estudiante, 
                           asignaturas=lista_asignaturas, 
                           hobbies=lista_hobbies)

if __name__ == '__main__':
    app.run(debug=True)