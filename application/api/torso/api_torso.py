import web
import config
import json


class Api_torso:
    def get(self, id_palabra_torso):
        try:
            # http://0.0.0.0:8080/api_torso?user_hash=12345&action=get
            if id_palabra_torso is None:
                result = config.model.get_all_torso()
                torso_json = []
                for row in result:
                    tmp = dict(row)
                    torso_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(torso_json)
            else:
                # http://0.0.0.0:8080/api_torso?user_hash=12345&action=get&id_palabra_torso=1
                result = config.model.get_torso(int(id_palabra_torso))
                torso_json = []
                torso_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(torso_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            torso_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(torso_json)

# http://0.0.0.0:8080/api_torso?user_hash=12345&action=put&id_palabra_torso=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, palabra,traduccion):
        try:
            config.model.insert_torso(palabra,traduccion)
            torso_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(torso_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_torso?user_hash=12345&action=delete&id_palabra_torso=1
    def delete(self, id_palabra_torso):
        try:
            config.model.delete_torso(id_palabra_torso)
            torso_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(torso_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_torso?user_hash=12345&action=update&id_palabra_torso=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_palabra_torso, palabra,traduccion):
        try:
            config.model.edit_torso(id_palabra_torso,palabra,traduccion)
            torso_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(torso_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            torso_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(torso_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_palabra_torso=None,
            palabra=None,
            traduccion=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_palabra_torso=user_data.id_palabra_torso
            palabra=user_data.palabra
            traduccion=user_data.traduccion
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_palabra_torso)
                elif action == 'put':
                    return self.put(palabra,traduccion)
                elif action == 'delete':
                    return self.delete(id_palabra_torso)
                elif action == 'update':
                    return self.update(id_palabra_torso, palabra,traduccion)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
