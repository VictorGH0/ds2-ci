from conexion import *

@app.route("/login", methods = ['POST'])
def login():
    id = request.form['id']
    pas = request.form['pass']
    return render_template("principal.html")