from source.config.flaskConfig import *
from source.config.blueprints import *
from flask import request, render_template, url_for,redirect




@fileSystemBlueprint.route('/saveImage', methods=['GET', 'POST'])
def saveImageFoo():
    file = request.files.get('file')
    
    try:
        file.save(path.join(fileSystemBlueprint.static_folder, 'Files', 'img.jpg'))
    except:
        pass
    return redirect(url_for('app.getMainTest'))

