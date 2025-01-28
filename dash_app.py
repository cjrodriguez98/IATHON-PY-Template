
import dash
from dash import dcc, html
import plotly.express as px
import os
import pandas as pd 

os.chdir('C:/Users/cjrodriguezf/Documents/PhD/IATHON/iathon-template')     

# Load the dataset
data = pd.read_csv('jamb_exam_results.csv')


# Create Dash app layout
app = dash.Dash(__name__)

app.layout = html.Div([
    # Title Section
    html.H1("Analyzing Factors Influencing JAMB Scores: A Comprehensive Study of Student Performance in Urban and Rural Public Schools", style={'textAlign': 'center'}),
    html.H4("Author: John Doe"),
    
    # Summary Section
    html.H2("Summary of the data"),
    dcc.Markdown(f'''The provided data contains information about five students, focusing on various educational parameters. Heres a summary of the key points:

1. **JAMB Scores**: The students achieved scores ranging from 182 to 210, indicating a varied performance in the Joint Admissions and Matriculation Board (JAMB) examination.

2. **Study Hours Per Week**: Study hours varied significantly, with one student studying as few as 12 hours per week and another studying up to 29 hours. This suggests differing levels of dedication or external obligations.

3. **Attendance Rate**: Attendance rates are generally high, ranging from 78% to 99%, with all students attending school regularly, which might correlate with their academic performance.

4. **Teacher Quality**: Teacher quality ratings are either 2 or 4 (on an unspecified scale), indicating mixed perceptions of teaching quality across the different students.

5. **Distance to School**: The distance to school varied, with some students living significantly closer (2.6 km) while others are farther away (12.4 km).

6. **School Type and Location**: All students attend public schools, with three located in urban areas and two in rural settings, which may affect access to resources and educational support.

7. **Extra Tutorials and Access to Learning Materials**: There is a mix of access to extra tutorials; three students have attended extra tutorials while all have access to learning materials.

8. **Parental Involvement**: Parental involvement appears high for most students, as indicated by the "High" and "Medium" ratings.

9. **IT Knowledge**: The students exhibit varying levels of IT knowledge, with ratings ranging from Medium to High.

10. **Demographics**: The group includes a mix of ages (15 to 22) and genders (three females and two males). Socioeconomic status varies, with some students coming from low socioeconomic backgrounds, while others are from high-status families.

11. **Parent Education Level**: Parent education levels are predominantly tertiary for most students, which could influence students' academic performance.

12. **Assignments Completed**: The number of completed assignments ranges from 1 to 5, indicating varying levels of engagement with schoolwork.

Overall, the data suggests a diverse group of students with differing academic performances, levels of study commitment, and varying influences from their educational environment and family background.'''),

    # Image Section
    html.Img(src='https://images.unsplash.com/photo-1498036882173-b41c28a8ba34?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2ODkxMzR8MHwxfHNlYXJjaHwxfHxKQU1CJTIwU2NvcmVzJTJDJTIwU3R1ZGVudCUyMFBlcmZvcm1hbmNlJTJDJTIwVXJiYW4lMjBhbmQlMjBSdXJhbCUyMFNjaG9vbHN8ZW58MHx8fHwxNzM2NzgwNDkxfDA&ixlib=rb-4.0.3&q=80&w=1080', style={'maxWidth': '600px', 'height': 'auto'}),
    
    # Stats Report Section
    html.H2("Statistical Report"),
    
    

    html.H1("Statistical Analysis of Student Data"),
    
    html.Div([
        html.H2("Question 1: Is there a significant correlation between Study Hours Per Week and JAMB Score?"),
        dcc.Graph(
            id='study_hours_vs_jamb_score',
            figure={
                'data': [
                    {'x': data['Study_Hours_Per_Week'], 'y': data['JAMB_Score'], 'mode': 'markers', 'name': 'Data Points'},
                ],
                'layout': {
                    'title': 'Study Hours Per Week vs JAMB Score',
                    'xaxis': {'title': 'Study Hours Per Week'},
                    'yaxis': {'title': 'JAMB Score'},
                }
            }
        ),
        html.Button('Perform Correlation Test', id='correlation-button', n_clicks=0),
        html.Div(id='correlation-result')
    ]),

    html.Div([
        html.H2("Question 2: Do Attendance Rate and Teacher Quality have a significant impact on JAMB Score?"),
        dcc.Graph(
            id='attendance_vs_jamb_score',
            figure={
                'data': [
                    {'x': data['Attendance_Rate'], 'y': data['JAMB_Score'], 'mode': 'markers', 'name': 'Attendance vs JAMB Score'},
                    {'x': data['Teacher_Quality'], 'y': data['JAMB_Score'], 'mode': 'markers', 'name': 'Teacher Quality vs JAMB Score'},
                ],
                'layout': {
                    'title': 'Impact of Attendance Rate and Teacher Quality on JAMB Score',
                    'xaxis': {'title': 'Attendance Rate / Teacher Quality'},
                    'yaxis': {'title': 'JAMB Score'},
                }
            }
        ),
        html.Button('Perform Regression Analysis', id='regression-button', n_clicks=0),
        html.Div(id='regression-result')
    ]),

    html.Div([
        html.H2("Question 3: Is there a difference in JAMB Scores based on Age groups?"),
        dcc.Graph(
            id='age_group_jamb_score',
            figure={
                'data': [
                    {'x': data['Age'], 'y': data['JAMB_Score'], 'type': 'box', 'name': 'JAMB Scores by Age'},
                ],
                'layout': {
                    'title': 'JAMB Scores Distribution by Age',
                    'xaxis': {'title': 'Age'},
                    'yaxis': {'title': 'JAMB Score'},
                }
            }
        ),
        html.Button('Perform ANOVA Test', id='anova-button', n_clicks=0),
        html.Div(id='anova-result')
    ]),
])

    
    

# Run the Dash app
app.run_server(debug=True)
    
    