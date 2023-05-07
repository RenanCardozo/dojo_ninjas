from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo

#---------------------- Display create/dojos

@app.route('/')
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojo.html", dojos = dojos)

@app.route('/create/dojo', methods=['PoST'])
def create_dojo():
    Dojo.save_one_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_one_dojo(data)
    return render_template('display.html' , dojo = dojo )


