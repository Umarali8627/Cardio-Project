from flask import Flask,render_template,request
import pickle
import numpy as np

# load the model 
with open('model/Heart disease prediction.pkl','rb') as file:
    model=pickle.load(file)
# now create the app 
app=Flask(__name__)
# get the class 
def predict_class(predictions):
   pred_clas=''
   if predictions[0]==1:
       pred_clas='detect Heart Problem'
   else:
       pred_clas='No Disease Found '
   return pred_clas
# route the app
@app.route('/')
def home():
    return render_template('index.html')
# now route the prediction 
@app.route('/predict',methods=['POST'])
def predict():
  try:
    # get the columns values from page using request
    features=[[float(x) for x in request.form.values()]]
    # do the predictions 
    prediction=model.predict(features)
    # get the class 
    pred_clas=predict_class(prediction)
    return render_template('index.html',predicted_text=pred_clas)
  except Exception as ex:
      return render_template('index.html', predicted_text=f"Error: {str(ex)}")


if __name__ == "__main__":
    app.run(debug=True)