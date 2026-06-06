import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from github import Github, GithubException
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="iOS Apps Analytics Dashboard",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("📱 iOS Apps Analytics Dashboard")
st.markdown("### Monitoring Your Apps' Global Reach")

# Initialize GitHub client
@st.cache_resource
def get_github_client():
    """Initialize and cache GitHub client"""
    token = os.getenv('GITHUB_TOKEN') or st.secrets.get('GITHUB_TOKEN')
    if not token:
        st.error("⚠️ GitHub token not found. Please set GITHUB_TOKEN in .env file or Streamlit secrets.")
        st.info("Create a token at: https://github.com/settings/tokens")
        st.stop()
    return Github(token)

@st.cache_data(ttl=3600)
def load_webpages():
    """Load web pages from WEBPAGES.md"""
    try:
        with open('WEBPAGES.md', 'r') as f:
            lines = f.readlines()

        repos = []
        for line in lines:
            line = line.strip()
            if line.startswith('https://github.com/'):
                # Extract owner and repo name from URL
                parts = line.replace('https://github.com/', '').split('/')
                if len(parts) >= 2:
                    repos.append({
                        'url': line,
                        'owner': parts[0],
                        'repo': parts[1],
                        'app_name': parts[1].replace('Page', '')
                    })
        return repos
    except FileNotFoundError:
        st.error("WEBPAGES.md file not found!")
        return []

@st.cache_data(ttl=1800)
def fetch_repo_traffic(github_client, owner, repo_name):
    """Fetch traffic data for a single repository"""
    try:
        repo = github_client.get_repo(f"{owner}/{repo_name}")

        # Get views
        views = repo.get_views_traffic(per="week")

        # Get clones
        clones = repo.get_clones_traffic(per="week")

        # Get referrers
        referrers = repo.get_top_referrers()

        # Get popular content
        paths = repo.get_top_paths()

        # Get repo info
        repo_info = {
            'name': repo.name,
            'description': repo.description,
            'stars': repo.stargazers_count,
            'forks': repo.forks_count,
            'watchers': repo.watchers_count,
            'open_issues': repo.open_issues_count,
            'created_at': repo.created_at,
            'updated_at': repo.updated_at,
            'size': repo.size,
            'language': repo.language,
        }

        return {
            'views': views,
            'clones': clones,
            'referrers': referrers,
            'paths': paths,
            'info': repo_info
        }
    except GithubException as e:
        st.warning(f"Could not fetch data for {repo_name}: {str(e)}")
        return None

def create_traffic_dataframe(traffic_data):
    """Convert traffic data to DataFrame"""
    if not traffic_data:
        return pd.DataFrame()

    views_data = []
    for view in traffic_data['views']['views']:
        views_data.append({
            'date': view.timestamp,
            'views': view.count,
            'unique_visitors': view.uniques
        })

    return pd.DataFrame(views_data)

def main():
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")

        # Refresh button
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.cache_data.clear()
            st.rerun()

        st.divider()

        # Date range filter
        st.subheader("📅 Date Range")
        days_back = st.slider("Days to analyze", 7, 90, 30)

        st.divider()

        # Info
        st.info("💡 Data refreshes every 30 minutes automatically")
        st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    # Load GitHub client
    github_client = get_github_client()

    # Load repositories
    repos = load_webpages()

    if not repos:
        st.error("No repositories found in WEBPAGES.md")
        return

    st.success(f"📊 Tracking {len(repos)} iOS app landing pages")

    # Fetch data for all repos
    with st.spinner("Fetching analytics data from GitHub..."):
        all_traffic_data = {}
        progress_bar = st.progress(0)

        for idx, repo_info in enumerate(repos):
            traffic = fetch_repo_traffic(github_client, repo_info['owner'], repo_info['repo'])
            if traffic:
                all_traffic_data[repo_info['app_name']] = traffic
            progress_bar.progress((idx + 1) / len(repos))

        progress_bar.empty()

    if not all_traffic_data:
        st.error("Could not fetch any traffic data. Please check your GitHub token permissions.")
        return

    # Calculate aggregate metrics
    total_views = 0
    total_unique_visitors = 0
    total_stars = 0
    total_forks = 0

    for app_name, data in all_traffic_data.items():
        if data and data['views']:
            total_views += data['views']['count']
            total_unique_visitors += data['views']['uniques']
        if data and data['info']:
            total_stars += data['info']['stars']
            total_forks += data['info']['forks']

    # Overview metrics
    st.header("🌍 Global Overview")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Views (14 days)", f"{total_views:,}", help="Total page views across all apps")
    with col2:
        st.metric("Unique Visitors", f"{total_unique_visitors:,}", help="Unique visitors in last 14 days")
    with col3:
        st.metric("Total Stars ⭐", f"{total_stars:,}", help="GitHub stars across all repositories")
    with col4:
        st.metric("Total Forks", f"{total_forks:,}", help="Total repository forks")

    st.divider()

    # Traffic trends
    st.header("📈 Traffic Trends")

    # Combine all views data
    all_views_df = []
    for app_name, data in all_traffic_data.items():
        df = create_traffic_dataframe(data)
        if not df.empty:
            df['app'] = app_name
            all_views_df.append(df)

    if all_views_df:
        combined_df = pd.concat(all_views_df, ignore_index=True)

        # Aggregate by date
        daily_traffic = combined_df.groupby('date').agg({
            'views': 'sum',
            'unique_visitors': 'sum'
        }).reset_index()

        # Create line chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=daily_traffic['date'],
            y=daily_traffic['views'],
            mode='lines+markers',
            name='Total Views',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8)
        ))
        fig.add_trace(go.Scatter(
            x=daily_traffic['date'],
            y=daily_traffic['unique_visitors'],
            mode='lines+markers',
            name='Unique Visitors',
            line=dict(color='#ff7f0e', width=3),
            marker=dict(size=8)
        ))

        fig.update_layout(
            title="Daily Traffic Across All Apps",
            xaxis_title="Date",
            yaxis_title="Count",
            hovermode='x unified',
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Top performing apps
    st.header("🏆 Top Performing Apps")

    # Create performance DataFrame
    performance_data = []
    for app_name, data in all_traffic_data.items():
        if data and data['views'] and data['info']:
            performance_data.append({
                'App Name': app_name,
                'Views (14d)': data['views']['count'],
                'Unique Visitors': data['views']['uniques'],
                'Stars': data['info']['stars'],
                'Forks': data['info']['forks'],
                'Engagement Score': data['views']['count'] + (data['info']['stars'] * 10)
            })

    perf_df = pd.DataFrame(performance_data)
    perf_df = perf_df.sort_values('Engagement Score', ascending=False)

    col1, col2 = st.columns(2)

    with col1:
        # Top apps by views
        fig_views = px.bar(
            perf_df.head(10),
            x='Views (14d)',
            y='App Name',
            orientation='h',
            title='Top 10 Apps by Views',
            color='Views (14d)',
            color_continuous_scale='Blues'
        )
        fig_views.update_layout(height=500, showlegend=False)
        st.plotly_chart(fig_views, use_container_width=True)

    with col2:
        # Top apps by stars
        fig_stars = px.bar(
            perf_df.head(10),
            x='Stars',
            y='App Name',
            orientation='h',
            title='Top 10 Apps by Stars',
            color='Stars',
            color_continuous_scale='Oranges'
        )
        fig_stars.update_layout(height=500, showlegend=False)
        st.plotly_chart(fig_stars, use_container_width=True)

    st.divider()

    # Traffic sources
    st.header("🔗 Traffic Sources")

    all_referrers = []
    for app_name, data in all_traffic_data.items():
        if data and data['referrers']:
            for ref in data['referrers']:
                all_referrers.append({
                    'referrer': ref.referrer,
                    'views': ref.count,
                    'unique_visitors': ref.uniques
                })

    if all_referrers:
        referrers_df = pd.DataFrame(all_referrers)
        referrers_agg = referrers_df.groupby('referrer').agg({
            'views': 'sum',
            'unique_visitors': 'sum'
        }).reset_index().sort_values('views', ascending=False).head(15)

        fig_referrers = px.bar(
            referrers_agg,
            x='views',
            y='referrer',
            orientation='h',
            title='Top Traffic Referrers',
            color='views',
            color_continuous_scale='Greens',
            labels={'views': 'Total Views', 'referrer': 'Source'}
        )
        fig_referrers.update_layout(height=500)
        st.plotly_chart(fig_referrers, use_container_width=True)

    st.divider()

    # Individual app details
    st.header("📱 Individual App Analytics")

    app_names = sorted(all_traffic_data.keys())
    selected_app = st.selectbox("Select an app to view details:", app_names)

    if selected_app and selected_app in all_traffic_data:
        data = all_traffic_data[selected_app]

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Views", f"{data['views']['count']:,}")
        with col2:
            st.metric("Unique Visitors", f"{data['views']['uniques']:,}")
        with col3:
            st.metric("Stars", f"{data['info']['stars']:,}")
        with col4:
            st.metric("Forks", f"{data['info']['forks']:,}")

        # App description
        if data['info']['description']:
            st.info(f"📝 {data['info']['description']}")

        # Traffic chart for selected app
        app_df = create_traffic_dataframe(data)
        if not app_df.empty:
            fig_app = px.line(
                app_df,
                x='date',
                y=['views', 'unique_visitors'],
                title=f"Traffic Trend for {selected_app}",
                labels={'value': 'Count', 'date': 'Date', 'variable': 'Metric'}
            )
            st.plotly_chart(fig_app, use_container_width=True)

        # Popular paths
        if data['paths']:
            st.subheader("Most Visited Pages")
            paths_data = [{
                'Path': path.path,
                'Views': path.count,
                'Unique Visitors': path.uniques
            } for path in data['paths']]
            st.dataframe(pd.DataFrame(paths_data), use_container_width=True, hide_index=True)

    # Footer
    st.divider()
    st.caption("Built with ❤️ using Streamlit | Data from GitHub API | Updates every 30 minutes")

if __name__ == "__main__":
    main()
