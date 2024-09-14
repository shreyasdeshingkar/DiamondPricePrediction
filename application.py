from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')

    else:
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )
        final_new_data = data.get_data_as_dataframe()
        
        if final_new_data is None:
            return jsonify({'error': 'Error occurred while creating the dataframe'}), 500

        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        
        if pred is None:
            return jsonify({'error': 'Prediction failed. Check logs for more details.'}), 500

        results = round(pred[0], 2)
        return render_template('form.html', final_result=results)

    


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)