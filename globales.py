import jinja2

jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader('html'))
index = jinja_environment.get_template('index.html')
add_training = jinja_environment.get_template('ha-addTraining.html')
result_detail = jinja_environment.get_template('ha-result-detail-screen.html')
result = jinja_environment.get_template('ha-result-screen.html')
search = jinja_environment.get_template('ha-search-screen.html')
