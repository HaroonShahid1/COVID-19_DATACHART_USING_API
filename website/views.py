import requests
from django.shortcuts import render
import plotly.express as px
import pandas as pd

def fetch_covid_data_and_display_chart(request):
    api_url = ''  # COVID-19 data API endpoint
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        # Process the data and create a DataFrame
        df = pd.DataFrame(data)

        # Create a chart using Plotly
        fig = px.bar(df, x='country', y='cases', title='COVID-19 Cases by Country')
        chart_div = fig.to_html(full_html=False)

        context = {'chart_div': chart_div}
    else:
        context = {'chart_div': None}  # Handle API request error

    return render(request, 'charting/chart.html', context)
