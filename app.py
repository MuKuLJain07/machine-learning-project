from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from src.logger import logging
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application=Flask(__name__)
logging.info("Flask app started")
app=application

# Route for Homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        form_data = {
            'gender': request.form.get('gender'),
            'race_ethnicity': request.form.get('race_ethnicity'),
            'parental_level_of_education': request.form.get('parental_level_of_education'),
            'lunch': request.form.get('lunch'),
            'test_preparation_course': request.form.get('test_preparation_course'),
            'total_score': request.form.get('total_score')
        }

        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            total_score=request.form.get('total_score')
        )

        pred_df=data.get_data_as_frame()

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        formatted_result = "{:.2f}".format(float(results[0]))
        return render_template('home.html', results=formatted_result, form_data=form_data)
    
if __name__=="__main__":
    app.run(debug=True)