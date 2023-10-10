from django.shortcuts import render
import numpy as np
import pickle
import os
from project.settings import BASE_DIR

loaded_model = pickle.load(open(os.path.join(BASE_DIR, "xgb_regressor.unknown"), 'rb'))


def home(req):
    return render(req, 'index.html', {'result': ''})


def evaluate(req):
    if req.method == 'POST':
        a = eval(req.POST['a'])
        b = eval(req.POST['b'])
        c = eval(req.POST['c'])
        d = eval(req.POST['d'])

        test = [a, b, c, d]
        test = np.asarray(test)
        test_reshaped = test.reshape(1, -1)
        y_pred = loaded_model.predict(test_reshaped)

        return render(req, 'index.html', {'result':  int(y_pred)})
