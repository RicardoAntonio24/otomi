import web
import config

db = config.db


def get_all_manos():
    try:
        return db.select('manos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_manos(id_palabra_manos):
    try:
        return db.select('manos', where='id_palabra_manos=$id_palabra_manos', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_manos(id_palabra_manos):
    try:
        return db.delete('manos', where='id_palabra_manos=$id_palabra_manos', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_manos(palabra,traduccion):
    try:
        return db.insert('manos',palabra=palabra,
traduccion=traduccion)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_manos(id_palabra_manos,palabra,traduccion):
    try:
        return db.update('manos',id_palabra_manos=id_palabra_manos,
palabra=palabra,
traduccion=traduccion,
                  where='id_palabra_manos=$id_palabra_manos',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
