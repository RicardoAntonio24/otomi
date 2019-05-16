import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_palabra_manos):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_palabra_manos) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_palabra_manos):
    '''

    def GET(self, id_palabra_manos):
        id_palabra_manos = config.check_secure_val(str(id_palabra_manos)) # HMAC id_palabra_manos validate
        result = config.model.get_manos(id_palabra_manos) # search for the id_palabra_manos data
        return config.render.view(result) # render view.html with id_palabra_manos data
