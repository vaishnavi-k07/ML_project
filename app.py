from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)


# Home route (ONLY ONE TEMPLATE)
@app.route('/')
def index():
    return render_template('home.html')


# Prediction route
@app.route('/predictdata', methods=['POST'])
def predict_datapoint():

    # DEBUG (VERY IMPORTANT)
    print("Form Data:", request.form)

    data = CustomData(
        gender=request.form.get('gender'),
        race_ethnicity=request.form.get('race_ethnicity'),
        parental_level_of_education=request.form.get('parental_level_of_education'),
        lunch=request.form.get('lunch'),
        test_preparation_course=request.form.get('test_preparation_course'),
        reading_score=float(request.form.get('reading_score')),
        writing_score=float(request.form.get('writing_score'))
    )

    pred_df = data.get_data_as_data_frame()
    print("Input DF:\n", pred_df)

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    return render_template('home.html', results=results)


if __name__ == "__main__":
    app.run(debug=True)