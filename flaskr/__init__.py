import os

from flask import Flask

def create_app(test_config=None):
	# create and configures the app
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY="dev",
		DATABASE=os.path.join(app.instance_path, 'flask.sqlite')
	)
	

	if test_config is None:
		# loads the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)

	# ensures the instance foler exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	@app.route('/hello')
	def hello():
		return 'Hello world!'

	from . import (auth, blog, db)
	db.init_app(app)
	app.register_blueprint(auth.bp)
	app.register_blueprint(blog.bp)
	app.add_url_rule('/', endpoint='index')

	return app