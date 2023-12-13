from flask import Blueprint,render_template,request,send_file
from io import BytesIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

score = Blueprint("score",__name__)

@score.route('/page4')
def page4():
  return render_template("page4.html")


def sigmoid(reg, x):
  m = reg.coef_
  b = reg.intercept_
  y = m * x + b
  P = 1 / (1 + (np.exp(-y)))
  P = P.reshape(-1)
  return P
#로지스틱회귀 모델링
def logistic():
  df = pd.read_csv('./data/LogisticRegressionData.csv')
  X= df.iloc[:,:-1]
  y = df.iloc[:,-1]
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
  reg = LogisticRegression()
  reg.fit(X_train, y_train)
  return reg,X_train,y_train

#로지스틱회귀 그래프출력
@score.route('/logistic/graph')
def logistic_graph():
  reg = logistic()[0]
  X_train = logistic()[1]
  y_train = logistic()[2]
  
  X_numeric = pd.to_numeric(X_train.iloc[:, 0], errors='coerce')
  X_numeric = X_numeric.dropna()
  X_range = np.arange(min(X_numeric), max(X_numeric), 0.1)
  # X_range = np.arange(min(X_train), max(X_train), 0.1)
  
  p=sigmoid(reg, X_range)
  plt.figure(figsize=(10,5),dpi=50)
  plt.scatter(X_train, y_train, color='blue')
  plt.plot(X_range, np.full(len(X_range), 0.5), color='red')
  plt.plot(X_range, sigmoid(reg,X_range), color='green')
  img = BytesIO()
  plt.savefig(img, format='png', dpi=50)
  img.seek(0)
  return send_file(img, mimetype='image/png')

#로지스틱회귀 예측값출력
@score.route('/logistic/<hour>')
def logistic_result(hour):
  
  hour = float(hour)
  reg = logistic()[0]
  pred = reg.predict_proba([[hour]])
  pred = pred[0,1]*100
  return str(pred)

@score.route('/page5')
def page4():
  return render_template("page5.html")
