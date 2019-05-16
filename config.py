import web

db_host = 'o3iyl77734b9n3tg.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'do1vahgpsgnwn10g'
db_user = 'z8sv0cktp7fm1yn9'
db_pw = 'zk23w128mhgre1by'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )