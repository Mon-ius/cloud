# -*-coding: utf-8-*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_uploads import UploadSet, configure_uploads, IMAGES


app = Flask(__name__)
import cloud.views

if __name__ == '__main__':
    app.run()
