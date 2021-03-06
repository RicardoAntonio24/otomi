import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_palabra_manos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_palabra_manos) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_palabra_manos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_palabra_manos) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_palabra_manos, **k):

    @staticmethod
    def POST_DELETE(id_palabra_manos, **k):
    '''

    def GET(self, id_palabra_manos, **k):
        message = None # Error message
        id_palabra_manos = config.check_secure_val(str(id_palabra_manos)) # HMAC id_palabra_manos validate
        result = config.model.get_manos(int(id_palabra_manos)) # search  id_palabra_manos
        result.id_palabra_manos = config.make_secure_val(str(result.id_palabra_manos)) # apply HMAC for id_palabra_manos
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_palabra_manos, **k):
        form = config.web.input() # get form data
        form['id_palabra_manos'] = config.check_secure_val(str(form['id_palabra_manos'])) # HMAC id_palabra_manos validate
        result = config.model.delete_manos(form['id_palabra_manos']) # get manos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_palabra_manos = config.check_secure_val(str(id_palabra_manos))  # HMAC user validate
            id_palabra_manos = config.check_secure_val(str(id_palabra_manos))  # HMAC user validate
            result = config.model.get_manos(int(id_palabra_manos)) # get id_palabra_manos data
            result.id_palabra_manos = config.make_secure_val(str(result.id_palabra_manos)) # apply HMAC to id_palabra_manos
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/manos') # render manos delete.html 
