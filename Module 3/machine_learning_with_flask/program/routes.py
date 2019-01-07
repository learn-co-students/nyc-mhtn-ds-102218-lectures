from sklearn.metrics import confusion_matrix, auc, roc_curve
from sklearn.model_selection import train_test_split
import plotly.graph_objs as go
import pickle
import pandas as pd
import numpy as np

df = pd.read_csv('./program/data/testing_data.csv',encoding='latin1')

X_test, y_test = df['text'] , df['spam']

with open('./program/data/mnb.pkl','rb') as pickled:
    model_mnb = pickle.load(pickled)

with open('./program/data/rf.pkl','rb') as pickled:
    model_rf = pickle.load(pickled)

with open('./program/data/lr.pkl','rb') as pickled:
    model_lr = pickle.load(pickled)


model_dict = {'Multinomial NB': model_mnb,
              'Random Forest': model_rf,
              'Logistic Regression': model_lr}



def make_roc_curve(X_test,y_test):
    lw = 2

    trace1 = go.Scatter(x=[0, 1], y=[0, 1],
                        mode='lines',
                        line=dict(color='navy', width=lw, dash='dash'),
                        showlegend=False)
    traces = [trace1]
    for name,model in model_dict.items():
        y_pred = model.predict_proba(X_test)[:,1]
        fpr, tpr, threshold = roc_curve(y_test,y_pred)
        roc_auc = auc(fpr,tpr)
        trace = go.Scatter(x=fpr, y=tpr,
                            mode='lines',
                            line=dict(width=lw),
                            name='ROC curve {} (area = {:0.4f})'.format(name,roc_auc)
                           )
        traces.append(trace)

    layout = go.Layout(title='Receiver Operator Characteristic',
                       xaxis=dict(title='False Positive Rate'),
                       yaxis=dict(title='True Positive Rate'),
                       height=600,
                       width=600,
                       legend=dict(orientation='h'))


    return {'data':traces,'layout':layout}



def make_prediction(clicks,input1):
    """Makes a classification based off of user inputted data"""
    text = [input1]
    prediction = model.predict(text)
    probability = model.predict_proba(text)

    if prediction[0] == 0:
        output = 'Not Spam'
        spam_prob = probability[0][0]
    else:
        output = 'Spam'
        spam_prob = probability[0][1]

    return """ This message has been predicted as {}! The model predicts it at a
                probability of {}""".format(output,spam_prob)


def custom_confusion_matrix(X_test,y_test,model_name,normalize):
    """Construct a confusion matrix.
    """
    model = model_dict[model_name]
    y_pred = model.predict(X_test)

    cm = confusion_matrix(y_test,y_pred)
    if normalize == 'Normalized':
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    trace = go.Heatmap(z= cm,
                   x=['Not Spam','Spam'],
                   y=['Not Spam','Spam']
                   )

    layout = go.Layout(title='Confusion Matrix: {}'.format(model_name),
                   xaxis=dict(title='Predicted Values'),
                   yaxis=dict(title='Actual Values'),
                   margin = {'l': 80}
                      )

    return {'data':[trace],'layout':layout}
