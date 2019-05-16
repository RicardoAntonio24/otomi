import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_palabra_torso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_palabra_torso) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_palabra_torso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_palabra_torso) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_palabra_torso, **k):

    @staticmethod
    def POST_EDIT(id_palabra_torso, **k):
        
    '''

    def GET(self, id_palabra_torso, **k):
        message = None # Error message
        id_palabra_torso = config.check_secure_val(str(id_palabra_torso)) # HMAC id_palabra_torso validate
        result = config.model.get_torso(int(id_palabra_torso)) # search for the id_palabra_torso
        result.id_palabra_torso = config.make_secure_val(str(result.id_palabra_torso)) # apply HMAC for id_palabra_torso
        return config.render.edit(result, message) # render torso edit.html

    def POST(self, id_palabra_torso, **k):
        form = config.web.input()  # get form data
        form['id_palabra_torso'] = config.check_secure_val(str(form['id_palabra_torso'])) # HMAC id_palabra_torso validate
        # edit user with new data
        result = config.model.edit_torso(
            form['id_palabra_torso'],form['palabra'],form['traduccion'],
        )
        if result == None: # Error on udpate data
            id_palabra_torso = config.check_secure_val(str(id_palabra_torso)) # validate HMAC id_palabra_torso
            result = config.model.get_torso(int(id_palabra_torso)) # search for id_palabra_torso data
            result.id_palabra_torso = config.make_secure_val(str(result.id_palabra_torso)) # apply HMAC to id_palabra_torso
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/torso') # render torso index.html
