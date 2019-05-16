import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_palabra_cabeza, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_palabra_cabeza) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_palabra_cabeza, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_palabra_cabeza) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_palabra_cabeza, **k):

    @staticmethod
    def POST_DELETE(id_palabra_cabeza, **k):
    '''

    def GET(self, id_palabra_cabeza, **k):
        message = None # Error message
        id_palabra_cabeza = config.check_secure_val(str(id_palabra_cabeza)) # HMAC id_palabra_cabeza validate
        result = config.model.get_cabeza(int(id_palabra_cabeza)) # search  id_palabra_cabeza
        result.id_palabra_cabeza = config.make_secure_val(str(result.id_palabra_cabeza)) # apply HMAC for id_palabra_cabeza
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_palabra_cabeza, **k):
        form = config.web.input() # get form data
        form['id_palabra_cabeza'] = config.check_secure_val(str(form['id_palabra_cabeza'])) # HMAC id_palabra_cabeza validate
        result = config.model.delete_cabeza(form['id_palabra_cabeza']) # get cabeza data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_palabra_cabeza = config.check_secure_val(str(id_palabra_cabeza))  # HMAC user validate
            id_palabra_cabeza = config.check_secure_val(str(id_palabra_cabeza))  # HMAC user validate
            result = config.model.get_cabeza(int(id_palabra_cabeza)) # get id_palabra_cabeza data
            result.id_palabra_cabeza = config.make_secure_val(str(result.id_palabra_cabeza)) # apply HMAC to id_palabra_cabeza
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/cabeza') # render cabeza delete.html 
