from source.config.flaskConfig import *
from source.config.blueprints import *
from flask import request, render_template






@appBlueprint.route('/main', methods=['GET'])
def getMainTest():
    return render_template('main.html', img='Files/img.jpg')

