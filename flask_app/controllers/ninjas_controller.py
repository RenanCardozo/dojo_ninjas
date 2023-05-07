from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo



#-------------------create ninja display route
@app.route('/ninjas')
def create_ninja():
    dojos = Dojo.get_all()
    return render_template('ninja.html' , dojos=dojos)


#-------------------------- action route for adding new ninjas
@app.route('/add',methods=['post'])
def add():
    Ninja.save_one_ninja(request.form)
    return redirect ('/dojos')

@app.route('/ninja/delete/<int:id>')
def delete_ninjas(id):
    data = {
        "id": id
    }
    Ninja.delete_one_ninja(data)
    return redirect('/dojo/{{one_dojo.id}}')

