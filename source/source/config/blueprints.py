from source.config.flaskConfig import *
from flask import Blueprint

fileSystemBlueprint = Blueprint('FileSys', __name__, 
                           static_folder=path.join(kis.config['rootDir'], 'FileSys'), 
                           url_prefix='/FileSys')

appBlueprint = Blueprint('app', __name__, 
                           template_folder=path.join(kis.config['rootDir'], 'source/templates'), 
                           static_folder=path.join(kis.config['rootDir'], 'source/static'), 
                           url_prefix='/app')
