
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
    html.H1("Factors Influencing Academic Performance: A Comprehensive Analysis of JAMB Scores and Educational Contexts", style={'textAlign': 'center'}),
    html.H4("Author: John Doe"),
    
    # Summary Section
    html.H2("Summary of the data"),
    dcc.Markdown(f'''The provided data consists of information about five students, capturing various academic and demographic variables that may influence their educational performance. Here's a summary of the key points:

1. **JAMB Scores**: Scores range from 182 to 210, with an average of approximately 198.4. The highest score recorded is 210, while the lowest is 182.

2. **Study Hours Per Week**: Students dedicate between 12 to 29 hours per week to studying. The student with the highest study hours (29) scored 182, while the one with the lowest study hours (12) scored 199.

3. **Attendance Rates**: Attendance rates vary from 78% to 99%. The student with the highest attendance (99%) scored 210, while the one with the lowest attendance (78%) scored 192.

4. **Teacher Quality**: Teacher quality is rated on a scale of 1 to 4. Most students have a teacher quality rating of 2 or 4, suggesting a mix of lower and higher quality teaching.

5. **Distance to School**: Distance to school varies significantly, with values ranging from 2.6 km to 12.4 km. 

6. **School Type**: All students attend public schools.

7. **School Location**: Students are from both urban (3 students) and rural (2 students) locations.

8. **Extra Tutorials**: Two students attend extra tutorials, while three do not.

9. **Access to Learning Materials**: All students have access to learning materials.

10. **Parent Involvement**: Parental involvement is classified as high for three students and medium for two.

11. **IT Knowledge**: IT knowledge is rated as medium for three students and high for two.

12. **Demographics**: The students include 3 females and 2 males, with ages ranging from 15 to 22 years. Socioeconomic status varies, with two students from a low status and three from a high or medium status.

13. **Parent Education Level**: Parent education levels range from tertiary to unspecified, with one student lacking specified data.

14. **Assignments Completed**: Assignment completion varies between 1 and 2, with no student completing more than 2 assignments.

In summary, the data reflects a diverse group of students in terms of academic performance, study habits, and demographic backgrounds, with various factors potentially impacting their educational outcomes.'''),

    # Image Section
    html.Img(src='https://images.unsplash.com/photo-1486591978090-58e619d37fe7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2ODkxMzR8MHwxfHNlYXJjaHwxfHxBY2FkZW1pYyUyMFBlcmZvcm1hbmNlJTJDJTIwSkFNQiUyMFNjb3JlcyUyQyUyMEVkdWNhdGlvbmFsJTIwQ29udGV4dHN8ZW58MHx8fHwxNzM2NzgzODY2fDA&ixlib=rb-4.0.3&q=80&w=1080', style={'maxWidth': '600px', 'height': 'auto'}),
    
    # Stats Report Section
    html.H2("Statistical Report"),
    
    

    dcc.Graph(
        id='scatter-jamb-study-hours',
        figure={
            'data': [
                {'x': data['Study_Hours_Per_Week'], 'y': data['JAMB_Score'], 'mode': 'markers', 'name': 'Scores vs Study Hours'},
            ],
            'layout': {
                'title': 'JAMB Score vs Study Hours Per Week',
                'xaxis': {'title': 'Study Hours Per Week'},
                'yaxis': {'title': 'JAMB Score'},
            }
        }
    ),
    dcc.Graph(
        id='boxplot-attendance-teacher-quality',
        figure={
            'data': [
                {
                    'y': data['Attendance_Rate'],
                    'type': 'box',
                    'name': 'Attendance Rate'
                },
                {
                    'y': data['Teacher_Quality'],
                    'type': 'box',
                    'name': 'Teacher Quality'
                }
            ],
            'layout': {
                'title': 'Boxplot of Attendance Rate and Teacher Quality',
                'yaxis': {'title': 'Rate / Quality'},
            }
        }
    ),
    dcc.Graph(
        id='histogram-age',
        figure={
            'data': [
                {'x': data['Age'], 'type': 'histogram', 'name': 'Age Distribution'},
            ],
            'layout': {
                'title': 'Histogram of Student Age',
                'xaxis': {'title': 'Age'},
                'yaxis': {'title': 'Number of Students'},
            }
        }
    ),
])

    
    

# Run the Dash app
app.run_server(debug=True)
    
    