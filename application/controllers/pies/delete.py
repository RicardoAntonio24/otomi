import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_palabra_pies, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_palabra_pies) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_palabra_pies, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_palabra_pies) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_palabra_pies, **k):

    @staticmethod
    def POST_DELETE(id_palabra_pies, **k):
    '''

    def GET(self, id_palabra_pies, **k):
        message = None # Error message
        id_palabra_pies = config.check_secure_val(str(id_palabra_pies)) # HMAC id_palabra_pies validate
        result = config.model.get_pies(int(id_palabra_pies)) # search  id_palabra_pies
        result.id_palabra_pies = config.make_secure_val(str(result.id_palabra_pies)) # apply HMAC for id_palabra_pies
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_palabra_pies, **k):
        form = config.web.input() # get form data
        form['id_palabra_pies'] = config.check_secure_val(str(form['id_palabra_pies'])) # HMAC id_palabra_pies validate
        result = config.model.delete_pies(form['id_palabra_pies']) # get pies data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_palabra_pies = config.check_secure_val(str(id_palabra_pies))  # HMAC user validate
            id_palabra_pies = config.check_secure_val(str(id_palabra_pies))  # HMAC user validate
            result = config.model.get_pies(int(id_palabra_pies)) # get id_palabra_pies data
            result.id_palabra_pies = config.make_secure_val(str(result.id_palabra_pies)) # apply HMAC to id_palabra_pies
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/pies') # render pies delete.html 
