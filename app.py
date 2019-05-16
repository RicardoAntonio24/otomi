# Author : Salvador Hernandez Mendoza
# Email  : salvadorhm@gmail.com
# Twitter: @salvadorhm
import web
import config


#activate ssl certificate
ssl = False

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    '/users', 'application.controllers.users.index.Index',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/partes_de_cuerpo', 'application.controllers.partes_de_cuerpo.index.Index',
'/partes_de_cuerpo/view/(.+)', 'application.controllers.partes_de_cuerpo.view.View',
'/partes_de_cuerpo/edit/(.+)', 'application.controllers.partes_de_cuerpo.edit.Edit',
'/partes_de_cuerpo/delete/(.+)', 'application.controllers.partes_de_cuerpo.delete.Delete',
'/partes_de_cuerpo/insert', 'application.controllers.partes_de_cuerpo.insert.Insert',
'/api_partes_de_cuerpo/?', 'application.api.partes_de_cuerpo.api_partes_de_cuerpo.Api_partes_de_cuerpo',
'/cabeza', 'application.controllers.cabeza.index.Index',
'/cabeza/view/(.+)', 'application.controllers.cabeza.view.View',
'/cabeza/edit/(.+)', 'application.controllers.cabeza.edit.Edit',
'/cabeza/delete/(.+)', 'application.controllers.cabeza.delete.Delete',
'/cabeza/insert', 'application.controllers.cabeza.insert.Insert',
'/api_cabeza/?', 'application.api.cabeza.api_cabeza.Api_cabeza',
'/manos', 'application.controllers.manos.index.Index',
'/manos/view/(.+)', 'application.controllers.manos.view.View',
'/manos/edit/(.+)', 'application.controllers.manos.edit.Edit',
'/manos/delete/(.+)', 'application.controllers.manos.delete.Delete',
'/manos/insert', 'application.controllers.manos.insert.Insert',
'/torso', 'application.controllers.torso.index.Index',
'/torso/view/(.+)', 'application.controllers.torso.view.View',
'/torso/edit/(.+)', 'application.controllers.torso.edit.Edit',
'/torso/delete/(.+)', 'application.controllers.torso.delete.Delete',
'/torso/insert', 'application.controllers.torso.insert.Insert',
'/pies', 'application.controllers.pies.index.Index',
'/pies/view/(.+)', 'application.controllers.pies.view.View',
'/pies/edit/(.+)', 'application.controllers.pies.edit.Edit',
'/pies/delete/(.+)', 'application.controllers.pies.delete.Delete',
'/pies/insert', 'application.controllers.pies.insert.Insert',
'/cabeza', 'application.controllers.cabeza.index.Index',
'/cabeza/view/(.+)', 'application.controllers.cabeza.view.View',
'/cabeza/edit/(.+)', 'application.controllers.cabeza.edit.Edit',
'/cabeza/delete/(.+)', 'application.controllers.cabeza.delete.Delete',
'/cabeza/insert', 'application.controllers.cabeza.insert.Insert',
'/api_cabeza/?', 'application.api.cabeza.api_cabeza.Api_cabeza',
'/api_torso/?', 'application.api.torso.api_torso.Api_torso',
'/api_manos/?', 'application.api.manos.api_manos.Api_manos',
'/api_pies/?', 'application.api.pies.api_pies.Api_pies',
)


app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'kuorra'
    web.config.session_parameters['timeout'] = 10
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


def InternalError(): 
    raise config.web.seeother('/')


def NotFound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = False # hide db transactions
    web.config.debug = False # hide debug print
    web.config.db_printing = False # hide db transactions
    app.internalerror = InternalError
    app.notfound = NotFound
    app.run()
