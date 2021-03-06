import web
import config

db = config.db


def get_all_pies():
    try:
        return db.select('pies')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_pies(id_palabra_pies):
    try:
        return db.select('pies', where='id_palabra_pies=$id_palabra_pies', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_pies(id_palabra_pies):
    try:
        return db.delete('pies', where='id_palabra_pies=$id_palabra_pies', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_pies(palabra,traduccion):
    try:
        return db.insert('pies',palabra=palabra,
traduccion=traduccion)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_pies(id_palabra_pies,palabra,traduccion):
    try:
        return db.update('pies',id_palabra_pies=id_palabra_pies,
palabra=palabra,
traduccion=traduccion,
                  where='id_palabra_pies=$id_palabra_pies',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
