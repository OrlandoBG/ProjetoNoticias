from ..extensions import db


class Noticia(db.Model):
    __tablename__ = "tb_noticia"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    publicacao = db.Column(db.Date)
    titulo_pricipal = db.Column(db.String(100))
    titulo_auxiliar = db.Column(db.String(100))
    noticia = db.Column(db.Text)
    primeiro_nome_autor = db.Column(db.String(50))
    sobrenome_autor = db.Column(db.String(50))
    fonte = db.Column(db.String(150))

    def __repr__(self):
        return "publicacao={}, titulo_pricipal={}, titulo_auxiliar={}, noticia={}, primeiro_nome_autor={}, fonte={}".format(
            self.publicacao, self.titulo_pricipal, self.titulo_auxiliar, self. noticia,
            self.primeiro_nome_autor, self.sobrenome_autor, self.fonte )
