import os
import subprocess

from flask import Flask
from . import db  # add this line

def run_fake_data_script():
    # Get the directory of the current file (__init__.py)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    # Construct the full path to the fake-data.py script
    script_path = os.path.join(dir_path, "templates", "fake-data.py")
    
    subprocess.run(["python", script_path], check=True)
    print("Generated Fake Data")

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # register the database commands
    db.init_app(app)  # ensure this line is present

    # apply the blueprints to the app
    from . import auth
    from . import blog
    from . import maintenance
    from . import engineer
    from . import operatorInit

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(maintenance.bp, url_prefix='/maintenance')
    app.register_blueprint(engineer.bp, url_prefix='/engineer')
    app.register_blueprint(operatorInit.bp, url_prefix='/operatorInit')

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    # Call init_db to initialize the database
    with app.app_context():
        db.init_db()

    return app
