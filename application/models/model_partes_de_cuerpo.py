import web
import config

db = config.db


def get_all_partes_de_cuerpo():
    try:
        return db.select('partes_de_cuerpo')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_partes_de_cuerpo(id_palabra):
    try:
        return db.select('partes_de_cuerpo', where='id_palabra=$id_palabra', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_partes_de_cuerpo(id_palabra):
    try:
        return db.delete('partes_de_cuerpo', where='id_palabra=$id_palabra', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_partes_de_cuerpo(palabra_uno,palabra_dos,palabra_tres,palabra_cuatro,palabra_oto_uno,palabra_oto_dos,palabra_oto_tres,palabra_oto_cuatro):
    try:
        return db.insert('partes_de_cuerpo',palabra_uno=palabra_uno,
palabra_dos=palabra_dos,
palabra_tres=palabra_tres,
palabra_cuatro=palabra_cuatro,
palabra_oto_uno=palabra_oto_uno,
palabra_oto_dos=palabra_oto_dos,
palabra_oto_tres=palabra_oto_tres,
palabra_oto_cuatro=palabra_oto_cuatro)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_partes_de_cuerpo(id_palabra,palabra_uno,palabra_dos,palabra_tres,palabra_cuatro,palabra_oto_uno,palabra_oto_dos,palabra_oto_tres,palabra_oto_cuatro):
    try:
        return db.update('partes_de_cuerpo',id_palabra=id_palabra,
palabra_uno=palabra_uno,
palabra_dos=palabra_dos,
palabra_tres=palabra_tres,
palabra_cuatro=palabra_cuatro,
palabra_oto_uno=palabra_oto_uno,
palabra_oto_dos=palabra_oto_dos,
palabra_oto_tres=palabra_oto_tres,
palabra_oto_cuatro=palabra_oto_cuatro,
                  where='id_palabra=$id_palabra',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
