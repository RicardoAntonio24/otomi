import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_palabra_manos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_palabra_manos) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_palabra_manos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_palabra_manos) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_palabra_manos, **k):

    @staticmethod
    def POST_EDIT(id_palabra_manos, **k):
        
    '''

    def GET(self, id_palabra_manos, **k):
        message = None # Error message
        id_palabra_manos = config.check_secure_val(str(id_palabra_manos)) # HMAC id_palabra_manos validate
        result = config.model.get_manos(int(id_palabra_manos)) # search for the id_palabra_manos
        result.id_palabra_manos = config.make_secure_val(str(result.id_palabra_manos)) # apply HMAC for id_palabra_manos
        return config.render.edit(result, message) # render manos edit.html

    def POST(self, id_palabra_manos, **k):
        form = config.web.input()  # get form data
        form['id_palabra_manos'] = config.check_secure_val(str(form['id_palabra_manos'])) # HMAC id_palabra_manos validate
        # edit user with new data
        result = config.model.edit_manos(
            form['id_palabra_manos'],form['palabra'],form['traduccion'],
        )
        if result == None: # Error on udpate data
            id_palabra_manos = config.check_secure_val(str(id_palabra_manos)) # validate HMAC id_palabra_manos
            result = config.model.get_manos(int(id_palabra_manos)) # search for id_palabra_manos data
            result.id_palabra_manos = config.make_secure_val(str(result.id_palabra_manos)) # apply HMAC to id_palabra_manos
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/manos') # render manos index.html
