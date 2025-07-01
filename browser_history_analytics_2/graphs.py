import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np


def create_top_domains_chart(df, top_n=10):
    """Create a bar chart of top visited domains"""
    domain_counts = df['domain'].value_counts().head(top_n)
    
    fig = px.bar(
        x=domain_counts.values,
        y=domain_counts.index,
        orientation='h',
        title=f"Top {top_n} Most Visited Domains",
        labels={'x': 'Number of Visits', 'y': 'Domain'},
        color=domain_counts.values,
        color_continuous_scale='viridis'
    )
    
    fig.update_layout(
        height=400,
        yaxis={'categoryorder': 'total ascending'},
        showlegend=False
    )
    
    return fig

def create_visits_over_time_chart(df):
    """Create a line chart showing visits over time"""
    daily_visits = df.groupby(df['date'].dt.date).size().reset_index()
    daily_visits.columns = ['date', 'visits']
    
    fig = px.line(
        daily_visits,
        x='date',
        y='visits',
        title='Daily Browsing Activity',
        labels={'visits': 'Number of Visits', 'date': 'Date'}
    )
    
    fig.update_traces(line_color='#1f77b4', line_width=2)
    fig.update_layout(height=400)
    
    return fig

def create_hourly_heatmap(df):
    """Create a heatmap showing activity by hour and day of week"""
    # Create pivot table for heatmap
    heatmap_data = df.groupby(['day_of_week', 'hour']).size().reset_index(name='visits')
    heatmap_pivot = heatmap_data.pivot(index='day_of_week', columns='hour', values='visits').fillna(0)
    
    # Reorder days
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heatmap_pivot = heatmap_pivot.reindex(day_order)
    
    fig = px.imshow(
        heatmap_pivot,
        title='Activity Heatmap (Hour vs Day of Week)',
        labels={'x': 'Hour of Day', 'y': 'Day of Week', 'color': 'Visits'},
        color_continuous_scale='viridis'
    )
    
    fig.update_layout(height=400)
    
    return fig

def create_category_pie_chart(df):
    """Create a pie chart showing category distribution"""
    category_counts = df['category'].value_counts()
    
    fig = px.pie(
        values=category_counts.values,
        names=category_counts.index,
        title='Browsing Categories Distribution'
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=400)
    
    return fig

def create_browsing_pattern_chart(df):
    """Create a chart showing browsing patterns by hour"""
    hourly_visits = df.groupby('hour').size().reset_index(name='visits')
    
    fig = px.bar(
        hourly_visits,
        x='hour',
        y='visits',
        title='Browsing Activity by Hour of Day',
        labels={'hour': 'Hour of Day', 'visits': 'Number of Visits'},
        color='visits',
        color_continuous_scale='blues'
    )
    
    fig.update_layout(
        height=400,
        xaxis={'tickmode': 'linear', 'tick0': 0, 'dtick': 1},
        showlegend=False
    )
    
    return fig