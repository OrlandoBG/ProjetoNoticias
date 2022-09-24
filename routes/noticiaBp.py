from flask import Blueprint, render_template, request, redirect, url_for
from datetime import date, datetime

from ..models.noticia import Noticia
from ..extensions import db

noticiaBp = Blueprint('noticiaBp', __name__)

@noticiaBp.route('/')
def lista_de_noticia():
    noticias_query = Noticia.query.all()
    return render_template('noticia_list.html', noticias=noticias_query)

@noticiaBp.route('/noticias/create')
def create_noticia():
    return render_template('noticia_create.html')

@noticiaBp.route('/noticias/add', methods=["POST"])
def add_noticia():
    r_publicacao = datetime.strptime(request.form["publicacao"], '%Y-%m-%d')
    r_titulo_pricipal = request.form["titulo_pricipal"]
    r_titulo_auxiliar = request.form["titulo_auxiliar"]
    r_noticia = request.form["noticia"]
    r_primeiro_nome_autor = request.form["primeiro_nome_autor"]
    r_sobrenome_autor = request.form["sobrenome_autor"]
    r_fonte = request.form["fonte"]

    obj_noticia = Noticia(publicacao = r_publicacao, titulo_pricipal = r_titulo_pricipal, titulo_auxiliar = r_titulo_auxiliar,
    noticia = r_noticia, primeiro_nome_autor = r_primeiro_nome_autor, sobrenome_autor = r_sobrenome_autor, fonte = r_fonte)

    db.session.add(obj_noticia)
    db.session.commit()

    return redirect(url_for("noticiaBp.lista_de_noticia"))

@noticiaBp.route('/noticias/update/<noticia_id>')
def update_noticia(noticia_id=0):
    noticia_query = Noticia.query.filter_by(id = noticia_id).first()
    return render_template('noticia_update.html', noticia=noticia_query)

@noticiaBp.route('/noticias/updt', methods=["POST"])
def updt_noticia():
    r_id = request.form["id"]
    r_publicacao = datetime.strptime(request.form["publicacao"], '%Y-%m-%d')
    r_titulo_pricipal = request.form["titulo_pricipal"]
    r_titulo_auxiliar = request.form["titulo_auxiliar"]
    r_noticia = request.form["noticia"]
    r_primeiro_nome_autor = request.form["primeiro_nome_autor"]
    r_sobrenome_autor = request.form["sobrenome_autor"]
    r_fonte = request.form["fonte"]

    obj_noticia = Noticia.query.filter_by(id = r_id).first()
    obj_noticia.publicacao = r_publicacao
    obj_noticia.titulo_pricipal = r_titulo_pricipal
    obj_noticia.titulo_auxiliar = r_titulo_auxiliar
    obj_noticia.noticia = r_noticia
    obj_noticia.primeiro_nome_autor = r_primeiro_nome_autor
    obj_noticia.sobrenome_autor = r_sobrenome_autor
    obj_noticia.fonte = r_fonte

    db.session.add(obj_noticia)
    db.session.commit()

    return redirect(url_for("noticiaBp.lista_de_noticia"))

@noticiaBp.route('/noticias/delete/<noticia_id>')
def delete_noticia(noticia_id=0):
    noticia_query = Noticia.query.filter_by(id = noticia_id).first()
    return render_template('noticia_delete.html', noticia=noticia_query)

@noticiaBp.route('/noticias/dlt', methods=["POST"])
def dlt_noticia():
    r_id = request.form["id"]
    obj_noticia = Noticia.query.filter_by(id = r_id).first()
    db.session.delete(obj_noticia)
    db.session.commit()
    return redirect(url_for("noticiaBp.lista_de_noticia"))
