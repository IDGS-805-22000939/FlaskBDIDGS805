from . import maestros
from flask import render_template,request,redirect,url_for
import forms

from models import db, Maestros


@maestros.route('/maestros', methods=['GET','POST'])
def maestro():
    create_form=forms.UserForm2(request.form)
    maestro=Maestros.query.all()
    return render_template("maestros/listadoMest.html",form=create_form,maestros=maestro)

@maestros.route("/Agregar", methods=['GET','POST'])
def agregar():
    create_form=forms.UserForm2(request.form)
    if request.method=='POST':
        maes=Maestros(nombre=create_form.nombre.data,
                     apellidos=create_form.apellidos.data,
                     especialidad=create_form.especialidad.data,
                     email=create_form.email.data)
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.maestro'))
    return render_template("maestros/Agregar.html",form=create_form)


@maestros.route("/info",methods=['GET','POST'])
def info():
    
    if request.method=='GET':
        id=request.args.get('id')
        #select * from maestros  where id=id
        maes1=db.session.query(Maestros).filter(Maestros.matricula==id).first()
        nombre=maes1.nombre
        apellidos=maes1.apellidos
        especialidad=maes1.especialidad
        email=maes1.email
        cursos=maes1.cursos
    return render_template('maestros/info.html', id=id,nombre=nombre,apellidos=apellidos,
                           especialidad=especialidad,email=email,cursos=cursos)


@maestros.route("/editarMa", methods=['GET','POST'])
def editar():
    create_form=forms.UserForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #select * from maestros  where id=id
        maes1=db.session.query(Maestros).filter(Maestros.matricula==id).first()
        create_form.matricula.data=maes1.matricula
        create_form.nombre.data=maes1.nombre
        create_form.apellidos.data=maes1.apellidos
        create_form.especialidad.data=maes1.especialidad
        create_form.email.data=maes1.email
    if request.method=='POST':
        id=create_form.matricula.data
        maes=db.session.query(Maestros).filter(Maestros.matricula==id).first()
        maes.nombre=create_form.nombre.data
        maes.apellidos=create_form.apellidos.data
        maes.especialidad=create_form.especialidad.data
        maes.email=create_form.email.data
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.maestro'))
    return render_template("maestros/editarMa.html",form=create_form)


@maestros.route("/borrar", methods=['GET','POST'])
def borrar():
    create_form=forms.UserForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #select * from maestros  where id=id
        maes1=db.session.query(Maestros).filter(Maestros.matricula==id).first()
        create_form.matricula.data=maes1.matricula
        create_form.nombre.data=maes1.nombre
        create_form.apellidos.data=maes1.apellidos
        create_form.especialidad.data=maes1.especialidad
        create_form.email.data=maes1.email
    if request.method=='POST':
        id=create_form.matricula.data
        maes=Maestros.query.get(id)
        db.session.delete(maes)
        db.session.commit()
        return redirect(url_for('maestros.maestro'))
    return render_template("maestros/borrar.html",form=create_form)