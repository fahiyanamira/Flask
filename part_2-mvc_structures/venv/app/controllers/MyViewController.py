from flask_restful import Resource
from flask import render_template, make_response, request

class MyViewController(Resource):
    def get(self):
        x = request.args.get("x", type=int)
        y = request.args.get("y", type=int)
        
        if not x or not y:
            x = "Salah satu parameter tidak diisi"
            y = "harap diisi terlebih dahulu"
            view = render_template('index2.html', x=x, y=y)
            return make_response(view)
        else:
            view2 = render_template('index.html', x=x, y=y)
            return make_response(view2)
