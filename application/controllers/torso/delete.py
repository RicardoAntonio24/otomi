import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_palabra_torso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_palabra_torso) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_palabra_torso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_palabra_torso) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_palabra_torso, **k):

    @staticmethod
    def POST_DELETE(id_palabra_torso, **k):
    '''

    def GET(self, id_palabra_torso, **k):
        message = None # Error message
        id_palabra_torso = config.check_secure_val(str(id_palabra_torso)) # HMAC id_palabra_torso validate
        result = config.model.get_torso(int(id_palabra_torso)) # search  id_palabra_torso
        result.id_palabra_torso = config.make_secure_val(str(result.id_palabra_torso)) # apply HMAC for id_palabra_torso
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_palabra_torso, **k):
        form = config.web.input() # get form data
        form['id_palabra_torso'] = config.check_secure_val(str(form['id_palabra_torso'])) # HMAC id_palabra_torso validate
        result = config.model.delete_torso(form['id_palabra_torso']) # get torso data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_palabra_torso = config.check_secure_val(str(id_palabra_torso))  # HMAC user validate
            id_palabra_torso = config.check_secure_val(str(id_palabra_torso))  # HMAC user validate
            result = config.model.get_torso(int(id_palabra_torso)) # get id_palabra_torso data
            result.id_palabra_torso = config.make_secure_val(str(result.id_palabra_torso)) # apply HMAC to id_palabra_torso
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/torso') # render torso delete.html 
