# import pandas as pd
# from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

port = int(os.getenv('PORT', 8000))
reload = bool(os.getenv('RELOAD', 1))
host=str(os.getenv('HOST','0.0.0.0'))

@app.get('/')
def Home():
    return "Service is Running..."

# This is meant to 
@app.get('/options-attributes')
def OptionsAttrubutes():
    attributes = ['attribute_1', 'attribute_2', 'attribute_3', 'attribute_4', 'attribute_5']
    return attributes

# #. Load trained Pipeline
# model = load_model('diamond-pipeline')

# # Define predict function
# @app.post('/predict')
# def predict(carat_weight, cut, color, clarity, polish, symmetry, report):
#     data = pd.DataFrame([[carat_weight, cut, color, clarity, polish, symmetry, report]])
#     data.columns = ['Carat Weight', 'Cut', 'Color', 'Clarity', 'Polish', 'Symmetry', 'Report']

#     predictions = predict_model(model, data=data) 
#     return {'prediction': int(predictions['Label'][0])}


if __name__ == "__main__":
    print('port => ', port)
    print('reload => ', reload)
    print('host => ', host)
    uvicorn.run('main:app', port=port, reload=reload, host=host)
