from flask import Flask


app = Flask(__name__, static_folder='static')

app.config["DEBUG"] = True

app.config['MONGODB_SETTINGS'] = {
    "db": "finalhackaton",
    'host': '127.0.0.1',
    'port': 27017
}

from models import db

db.init_app(app)

from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)


import views

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/addrasp', view_func=views.add_rasp)
app.add_url_rule('/show_rasps', view_func=views.show_rasps)
app.add_url_rule('/add_member', view_func=views.add_member, methods=['GET', 'POST'])
app.add_url_rule('/show_members', view_func=views.show_members)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
