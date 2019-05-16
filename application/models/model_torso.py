import web
import config

db = config.db


def get_all_torso():
    try:
        return db.select('torso')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_torso(id_palabra_torso):
    try:
        return db.select('torso', where='id_palabra_torso=$id_palabra_torso', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_torso(id_palabra_torso):
    try:
        return db.delete('torso', where='id_palabra_torso=$id_palabra_torso', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_torso(palabra,traduccion):
    try:
        return db.insert('torso',palabra=palabra,
traduccion=traduccion)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_torso(id_palabra_torso,palabra,traduccion):
    try:
        return db.update('torso',id_palabra_torso=id_palabra_torso,
palabra=palabra,
traduccion=traduccion,
                  where='id_palabra_torso=$id_palabra_torso',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
