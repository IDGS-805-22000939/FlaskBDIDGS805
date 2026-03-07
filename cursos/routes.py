from . import cursos
from flask import render_template,request,redirect,url_for
import forms

from models import db, Curso, Maestros, Alumnos, Inscripcion

@cursos.route("/cursos", methods=['GET','POST'])
def curso():
    create_form=forms.UserForm3(request.form)
    cursos=Curso.query.all()
    return render_template("cursos/listaCursos.html",form=create_form,cursos=cursos)

@cursos.route("/agregarCurso", methods=['GET','POST'])
def agregar():
    create_form=forms.UserForm3(request.form)
    
    maestros = Maestros.query.all()
    
    create_form.maestro_id.choices = [
        (m.matricula, m.nombre + " " + m.apellidos) for m in maestros
    ]
    
    if request.method=='POST' and create_form.validate():
        cur=Curso(nombre=create_form.nombre.data,
                     descripcion=create_form.descripcion.data,
                     maestro_id=create_form.maestro_id.data)
        db.session.add(cur)
        db.session.commit()
        return redirect(url_for('cursos.curso'))
    return render_template("cursos/agregarCurso.html",form=create_form)

@cursos.route("/detallesCurso",methods=['GET','POST'])
def detalle():
    
    if request.method=='GET':
        id=request.args.get('id')
        #select * from alumnos  where id=id
        cur1=db.session.query(Curso).filter(Curso.id==id).first()
        nombre=cur1.nombre
        descripcion=cur1.descripcion
        maestro_id=cur1.maestro_id
        alumnos=cur1.alumnos
    return render_template('cursos/detallesCurso.html', id=id,nombre=nombre,
                           descripcion=descripcion,
                           maestro_id=maestro_id, cursos=cur1,alumnos=alumnos)

@cursos.route("/editarCurso", methods=['GET','POST'])
def editar():
    create_form=forms.UserForm3(request.form)
    
    maestros = Maestros.query.all()
    
    create_form.maestro_id.choices = [
        (m.matricula, m.nombre + " " + m.apellidos) for m in maestros
    ]
    
    if request.method=='GET':
        id=request.args.get('id')
        #select * from alumnos  where id=id
        cur1=db.session.query(Curso).filter(Curso.id==id).first()
        create_form.id.data=cur1.id
        create_form.nombre.data=cur1.nombre
        create_form.descripcion.data=cur1.descripcion
        create_form.maestro_id.data=cur1.maestro_id
    if request.method=='POST' and create_form.validate():
        id=create_form.id.data
        cur=db.session.query(Curso).filter(Curso.id==id).first()
        cur.nombre=create_form.nombre.data
        cur.descripcion=create_form.descripcion.data
        cur.maestro_id=create_form.maestro_id.data
        db.session.add(cur)
        db.session.commit()
        return redirect(url_for('cursos.curso'))
    return render_template("cursos/editarCurso.html",form=create_form)

@cursos.route("/eliminarCurso", methods=['GET','POST'])
def eliminar():
    create_form=forms.UserForm3(request.form)
    
    maestros = Maestros.query.all()
    
    create_form.maestro_id.choices = [
        (m.matricula, m.nombre + " " + m.apellidos) for m in maestros
    ]
    
    if request.method=='GET':
        id=request.args.get('id')
        #select * from alumnos  where id=id
        cur1=db.session.query(Curso).filter(Curso.id==id).first()
        create_form.id.data=cur1.id
        create_form.nombre.data=cur1.nombre
        create_form.descripcion.data=cur1.descripcion
        create_form.maestro_id.data=cur1.maestro_id
    if request.method=='POST':
        id=create_form.id.data
        cur=Curso.query.get(id)
        db.session.delete(cur)
        db.session.commit()
        return redirect(url_for('cursos.curso'))
    return render_template("cursos/eliminarCurso.html",form=create_form)


@cursos.route("/inscripciones", methods=['GET','POST'])
def inscribir():
    create_form=forms.UserForm4(request.form)
    
    alumnos = Alumnos.query.all()
    
    create_form.alumno_id.choices = [
        (a.id, a.nombre + " " + a.apellidos) for a in alumnos
    ]
    
    cursos = Curso.query.all()
    
    create_form.curso_id.choices = [
        (c.id, c.nombre) for c in cursos
    ]
    
    if request.method=='POST' and create_form.validate():
        ins=Inscripcion(alumno_id=create_form.alumno_id.data,
                     curso_id=create_form.curso_id.data)
        db.session.add(ins)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("cursos/inscripciones.html",form=create_form)