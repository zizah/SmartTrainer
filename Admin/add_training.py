import cgi
import json
import pickle
from json import JSONEncoder

import webapp2

from model.Exercice import Exercice


class AddTraining(webapp2.RequestHandler):
    def post(self):
        titleDescription = cgi.escape(self.request.get('titleDescription'))
        exerciceDescription = cgi.escape(self.request.get('exerciceDescription'))
        duree = cgi.escape(self.request.get('duree'))

        exercice = Exercice()
        exercice.titleDescription = titleDescription
        exercice.exerciceDescription = exerciceDescription
        exercice.duree = duree
        exercice.put()

        data = exercice.get_all_exercices_by_plan()
        result = json.dumps(self.traitement_data(), cls=JSONEncoder)
        self.response.out.write(result)


    def traitement_data(self, data):
        data_tmp = []
        for exercice in data:
            json = {
                'id': exercice.key.id(),
                'titleDescription': exercice.titleDescription,
                'exerciceDescription': exercice.exerciceDescription,
                'duree': exercice.duree
            }
            data_tmp.append(json.copy())
            json.clear()
        return data_tmp

class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}

def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(str(dct['_python_object']))
    return dct
