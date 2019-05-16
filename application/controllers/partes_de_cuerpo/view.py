import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_palabra):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_palabra) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_palabra):
    '''

    def GET(self, id_palabra):
        id_palabra = config.check_secure_val(str(id_palabra)) # HMAC id_palabra validate
        result = config.model.get_partes_de_cuerpo(id_palabra) # search for the id_palabra data
        return config.render.view(result) # render view.html with id_palabra data
