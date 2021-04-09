import json
import pickle
import numpy as np
__data_columns = None
__model = None


def get_diabetes_predicted(glucose, bmi, age):
  load_model()
  global __data_columns
  x = np.zeros(len(__data_columns))
  x[0] = glucose
  x[1] = bmi 
  x[2] = age
  return round(__model.predict_proba([x])[0][1]*100)


def load_model():
  global __data_columns
  global __model
  with open(r'Model/columns_diabetes.json', 'rb') as f:
    __data_columns = json.load(f)['data_columns']
  with open(r'Model/model_diabetes', 'rb') as f:
    __model = pickle.load(f)
  print('Cargando artefactos...hecho')



