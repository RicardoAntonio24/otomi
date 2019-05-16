import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_palabra, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_palabra) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_palabra, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_palabra) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_palabra, **k):

    @staticmethod
    def POST_EDIT(id_palabra, **k):
        
    '''

    def GET(self, id_palabra, **k):
        message = None # Error message
        id_palabra = config.check_secure_val(str(id_palabra)) # HMAC id_palabra validate
        result = config.model.get_partes_de_cuerpo(int(id_palabra)) # search for the id_palabra
        result.id_palabra = config.make_secure_val(str(result.id_palabra)) # apply HMAC for id_palabra
        return config.render.edit(result, message) # render partes_de_cuerpo edit.html

    def POST(self, id_palabra, **k):
        form = config.web.input()  # get form data
        form['id_palabra'] = config.check_secure_val(str(form['id_palabra'])) # HMAC id_palabra validate
        # edit user with new data
        result = config.model.edit_partes_de_cuerpo(
            form['id_palabra'],form['palabra_uno'],form['palabra_dos'],form['palabra_tres'],form['palabra_cuatro'],form['palabra_oto_uno'],form['palabra_oto_dos'],form['palabra_oto_tres'],form['palabra_oto_cuatro'],
        )
        if result == None: # Error on udpate data
            id_palabra = config.check_secure_val(str(id_palabra)) # validate HMAC id_palabra
            result = config.model.get_partes_de_cuerpo(int(id_palabra)) # search for id_palabra data
            result.id_palabra = config.make_secure_val(str(result.id_palabra)) # apply HMAC to id_palabra
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/partes_de_cuerpo') # render partes_de_cuerpo index.html
