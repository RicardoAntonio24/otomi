import web
import config

db = config.db


def get_all_cabeza():
    try:
        return db.select('cabeza')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_cabeza(id_palabra_cabeza):
    try:
        return db.select('cabeza', where='id_palabra_cabeza=$id_palabra_cabeza', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_cabeza(id_palabra_cabeza):
    try:
        return db.delete('cabeza', where='id_palabra_cabeza=$id_palabra_cabeza', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_cabeza(palabra,traduccion):
    try:
        return db.insert('cabeza',palabra=palabra,
traduccion=traduccion)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_cabeza(id_palabra_cabeza,palabra,traduccion):
    try:
        return db.update('cabeza',id_palabra_cabeza=id_palabra_cabeza,
palabra=palabra,
traduccion=traduccion,
                  where='id_palabra_cabeza=$id_palabra_cabeza',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
