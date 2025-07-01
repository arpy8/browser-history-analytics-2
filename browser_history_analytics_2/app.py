import streamlit as st

try:
    from browser_history_analytics_2.utils import (
        generate_df,
        get_summary_stats
    )
    from browser_history_analytics_2.graphs import (
        create_top_domains_chart,
        create_visits_over_time_chart,
        create_hourly_heatmap,
        create_category_pie_chart,
        create_browsing_pattern_chart
    )
    from browser_history import get_history
except ImportError as e:
    st.error(f"Missing required dependencies: {e}")
    st.error("Please install all required packages using: pip install -r requirements.txt")
    st.stop()


st.set_page_config(
    page_title="Browser History Analytics 2",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    try:
        outputs = get_history()
        data = outputs.histories
        return generate_df(data)
    except Exception as e:
        st.error(f"Error loading browser history: {e}")
        return None
        
try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading browser history data: {e}")
    df = None

if df is not None and not df.empty:
    st.sidebar.header("Filters")
    
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['date'].min().date(), df['date'].max().date()),
        min_value=df['date'].min().date(),
        max_value=df['date'].max().date()
    )
    
    categories = df['category'].unique()
    selected_categories = st.sidebar.multiselect(
        "Select Categories",
        options=categories,
        default=categories
    )
    
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = df[
            (df['date'].dt.date >= start_date) & 
            (df['date'].dt.date <= end_date) &
            (df['category'].isin(selected_categories))
        ]
    else:
        filtered_df = df[df['category'].isin(selected_categories)]
    
    tab1, tab2, tab3 = st.tabs(["Home", "Raw Data", "Additional Info"])

    
    with tab1:
        st.header("Summary Statistics")

        if not filtered_df.empty:
            stats = get_summary_stats(filtered_df)
            
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1: st.metric("Total Visits", stats['total_visits'])
            with col2: st.metric("Unique Domains", stats['unique_domains'])
            with col3: st.metric("Date Range", len(filtered_df['date'].dt.date.unique()), delta="days")
            with col4: st.metric("Most Active Day", stats['most_active_day'])
            with col5: st.metric("Peak Hour", stats['most_active_hour'])
            
            st.header("Visualizations")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("Most Visited Domains")
                fig_domains = create_top_domains_chart(filtered_df)
                st.plotly_chart(fig_domains, use_container_width=True)
            
            with col2:
                st.subheader("Visits Over Time")
                fig_timeline = create_visits_over_time_chart(filtered_df)
                st.plotly_chart(fig_timeline, use_container_width=True)
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("Activity Heatmap")
                fig_heatmap = create_hourly_heatmap(filtered_df)
                st.plotly_chart(fig_heatmap, use_container_width=True)
            
            with col2:
                st.subheader("Category Distribution")
                fig_pie = create_category_pie_chart(filtered_df)
                st.plotly_chart(fig_pie, use_container_width=True)
            
            st.subheader("Browsing Patterns by Hour")
            fig_hourly = create_browsing_pattern_chart(filtered_df)
            st.plotly_chart(fig_hourly, use_container_width=True)
            
        with tab2:
            st.header("Raw Data")
            
            search_term = st.text_input("🔍 Search in URLs or titles:", placeholder="Enter search term...")
            
            if search_term:
                search_df = filtered_df[
                    filtered_df['url'].str.contains(search_term, case=False, na=False) |
                    filtered_df['title'].str.contains(search_term, case=False, na=False) |
                    filtered_df['domain'].str.contains(search_term, case=False, na=False)
                ]
            else:
                search_df = filtered_df
            
            col1, col2, col3 = st.columns([1,0.2,0.2])
            with col1:
                show_columns = st.multiselect(
                    "Select columns to display:",
                    options=['date', 'domain', 'url', 'title', 'category', 'hour', 'day_of_week'],
                    default=['date', 'domain', 'title', 'category'],
                )
            
            with col2:
                rows_to_show = st.selectbox("Rows to display:", [10, 25, 50, 100, "All"])
            
            with col3:
                st.write("<br>"*2, unsafe_allow_html=True)  
                display_df = search_df[show_columns].copy()
                
                if rows_to_show != "All":
                    display_df = display_df.head(rows_to_show)
                
                csv = display_df.to_csv(index=False)
                
                st.download_button(
                    label="📥",
                    data=csv,
                    file_name="browser_history_filtered.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            
            if show_columns:
                st.dataframe(display_df, use_container_width=True, height=300)
                
        
        with tab3:
            st.header("Additional Info")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("Top Domains by Category")
                for category in filtered_df['category'].unique():
                    if category != 'Unknown':
                        cat_domains = filtered_df[filtered_df['category'] == category]['domain'].value_counts().head(3)
                        st.write(f"**{category}:**")
                        for domain, count in cat_domains.items():
                            st.write(f"  • {domain}: {count} visits")
            
            with col2:
                st.subheader("Browsing Habits")
                avg_daily_visits = len(filtered_df) / len(filtered_df['date'].dt.date.unique())
                most_active_category = filtered_df['category'].value_counts().index[0]
                
                st.write(f"**Average daily visits:** {avg_daily_visits:.1f}")
                st.write(f"**Most browsed category:** {most_active_category}")
                st.write(f"**Peak browsing time:** {stats['most_active_hour']} on {stats['most_active_day']}s")
                
                weekend_visits = len(filtered_df[filtered_df['day_num'].isin([5, 6])])
                weekday_visits = len(filtered_df[~filtered_df['day_num'].isin([5, 6])])
                
                if weekday_visits > 0:
                    weekend_ratio = weekend_visits / weekday_visits
                    st.write(f"**Weekend/Weekday ratio:** {weekend_ratio:.2f}")
    
else:
    st.error("Unable to load browser history data. Please ensure the CSV file exists and is properly formatted.")