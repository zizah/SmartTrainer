import jinja2

#Template to manage the view
jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader('html'))
INDEX = jinja_environment.get_template('index.html')
ADD_TRAINING = jinja_environment.get_template('ha-addTraning.html')
RESULT_DETAIL = jinja_environment.get_template('ha-result-detail-screen.html')
RESULT = jinja_environment.get_template('ha-result-screen.html')
SEARCH = jinja_environment.get_template('ha-search-screen.html')

