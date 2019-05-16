import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_palabra, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_palabra) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_palabra, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_palabra) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_palabra, **k):

    @staticmethod
    def POST_DELETE(id_palabra, **k):
    '''

    def GET(self, id_palabra, **k):
        message = None # Error message
        id_palabra = config.check_secure_val(str(id_palabra)) # HMAC id_palabra validate
        result = config.model.get_partes_de_cuerpo(int(id_palabra)) # search  id_palabra
        result.id_palabra = config.make_secure_val(str(result.id_palabra)) # apply HMAC for id_palabra
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_palabra, **k):
        form = config.web.input() # get form data
        form['id_palabra'] = config.check_secure_val(str(form['id_palabra'])) # HMAC id_palabra validate
        result = config.model.delete_partes_de_cuerpo(form['id_palabra']) # get partes_de_cuerpo data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_palabra = config.check_secure_val(str(id_palabra))  # HMAC user validate
            id_palabra = config.check_secure_val(str(id_palabra))  # HMAC user validate
            result = config.model.get_partes_de_cuerpo(int(id_palabra)) # get id_palabra data
            result.id_palabra = config.make_secure_val(str(result.id_palabra)) # apply HMAC to id_palabra
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/partes_de_cuerpo') # render partes_de_cuerpo delete.html 
