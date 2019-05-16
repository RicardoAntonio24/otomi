import web
import config
import json


class Api_partes_de_cuerpo:
    def get(self, id_palabra):
        try:
            # http://192.168.1.114:8080/api_partes_de_cuerpo?user_hash=12345&action=get
            if id_palabra is None:
                result = config.model.get_all_partes_de_cuerpo()
                partes_de_cuerpo_json = []
                for row in result:
                    tmp = dict(row)
                    partes_de_cuerpo_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(partes_de_cuerpo_json)
            else:
                # http://0.0.0.0:8080/api_partes_de_cuerpo?user_hash=12345&action=get&id_palabra=1
                result = config.model.get_partes_de_cuerpo(int(id_palabra))
                partes_de_cuerpo_json = []
                partes_de_cuerpo_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(partes_de_cuerpo_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            partes_de_cuerpo_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(partes_de_cuerpo_json)

# http://0.0.0.0:8080/api_partes_de_cuerpo?user_hash=12345&action=put&id_palabra=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, palabra_uno,palabra_dos,palabra_tres,palabra_cuatro,palabra_oto_uno,palabra_oto_dos,palabra_oto_tres,palabra_oto_cuatro):
        try:
            config.model.insert_partes_de_cuerpo(palabra_uno,palabra_dos,palabra_tres,palabra_cuatro,palabra_oto_uno,palabra_oto_dos,palabra_oto_tres,palabra_oto_cuatro)
            partes_de_cuerpo_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(partes_de_cuerpo_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_partes_de_cuerpo?user_hash=12345&action=delete&id_palabra=1
    def delete(self, id_palabra):
        try:
            config.model.delete_partes_de_cuerpo(id_palabra)
            partes_de_cuerpo_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(partes_de_cuerpo_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_partes_de_cuerpo?user_hash=12345&action=update&id_palabra=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_palabra, palabra_uno,palabra_dos,palabra_tres,palabra_cuatro,palabra_oto_uno,palabra_oto_dos,palabra_oto_tres,palabra_oto_cuatro):
        try:
            config.model.edit_partes_de_cuerpo(id_palabra,palabra_uno,palabra_dos,palabra_tres,palabra_cuatro,palabra_oto_uno,palabra_oto_dos,palabra_oto_tres,palabra_oto_cuatro)
            partes_de_cuerpo_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(partes_de_cuerpo_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            partes_de_cuerpo_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(partes_de_cuerpo_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_palabra=None,
            palabra_uno=None,
            palabra_dos=None,
            palabra_tres=None,
            palabra_cuatro=None,
            palabra_oto_uno=None,
            palabra_oto_dos=None,
            palabra_oto_tres=None,
            palabra_oto_cuatro=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_palabra=user_data.id_palabra

            palabra_uno=user_data.palabra_uno

            palabra_dos=user_data.palabra_dos

            palabra_tres=user_data.palabra_tres

            palabra_cuatro=user_data.palabra_cuatro

            palabra_oto_uno=user_data.palabra_oto_uno

            palabra_oto_dos=user_data.palabra_oto_dos

            palabra_oto_tres=user_data.palabra_oto_tres

            palabra_oto_cuatro=user_data.palabra_oto_cuatro

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_palabra)
                elif action == 'put':
                    return self.put(palabra_uno,palabra_dos,palabra_tres,palabra_cuatro,palabra_oto_uno,palabra_oto_dos,palabra_oto_tres,palabra_oto_cuatro)
                elif action == 'delete':
                    return self.delete(id_palabra)
                elif action == 'update':
                    return self.update(id_palabra, palabra_uno,palabra_dos,palabra_tres,palabra_cuatro,palabra_oto_uno,palabra_oto_dos,palabra_oto_tres,palabra_oto_cuatro)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
