from app import web
from app.controllers import MyViewController

web.add_resource(MyViewController.MyViewController, '/dua-parameter')
