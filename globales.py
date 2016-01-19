import jinja2

jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader('html'))
index = jinja_environment.get_template('index.html')
#login = jinja_environment.get_template('login.html')
