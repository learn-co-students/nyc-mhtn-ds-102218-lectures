from program.routes import X_test, y_test, model_dict, make_roc_curve, custom_confusion_matrix
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash
from program import app

model = model_dict['Multinomial NB']

#####################################################################
### Confusion Matrix
#####################################################################

app.css.append_css({"external_url": "https://codepen.io/amyoshino/pen/jzXypZ.css"})

app.layout = html.Div([html.H1('SMS Spam Detector'),
                html.Div(className='five columns',children = [
                    dcc.Graph(id ='confusion_matrix'),
                        dcc.Dropdown(
                            id='model_name',
                            options=[{'label': i, 'value': i} for i in model_dict.keys()],
                            value='Multinomial NB'
                            ),

                    dcc.RadioItems(
                        id='normalize',
                        options=[{'label': i, 'value': i} for i in ['Normalized', 'Not Normalized']],
                        value='Not Normalized',
                        labelStyle={'display': 'inline-block'}
                        )
                        ]) ,
                html.Div(className='six columns', children=[
        dcc.Graph(id ='ROC_curve',
                figure= make_roc_curve(X_test,y_test))
                ]),

        html.Div(className='nine columns',children =[
        html.H1(children='Try it for yourself!!'),
        html.H4('Enter text here to determine if a text is spam.'),
        dcc.Input(id='input1', type='text', value='Special offer just for you!',size='40'),
        html.Button(id='submit-button', children='Submit'),
        html.Div(id='output-state'),
        html.Br()
        ])])




@app.callback(
    dash.dependencies.Output('confusion_matrix','figure'),
    [dash.dependencies.Input('model_name','value'),
    dash.dependencies.Input('normalize','value')])


def make_confusion_matrix(model_name,normalize):
    c = custom_confusion_matrix(X_test,y_test,model_name, normalize=normalize)

    return c



@app.callback(Output('output-state', 'children'),
              [Input('submit-button','n_clicks')],
              [State('input1', 'value')])

def make_prediction(clicks,input1):
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
