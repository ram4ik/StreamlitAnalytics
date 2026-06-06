# iOS Apps Analytics Dashboard 📱

A beautiful, auto-updating analytics dashboard for monitoring all your iOS app landing pages on GitHub.

🌐 **Live Demo**: https://ram4ik.github.io/StreamlitAnalytics/

## Two Versions Available

### 🌟 Static Website (GitHub Pages) - **Recommended**
- ✅ Auto-updates every 6 hours via GitHub Actions
- ✅ Shows stars, forks, views, and traffic data
- ✅ No rate limits, works for everyone
- ✅ Super fast loading
- ✅ Mobile responsive

### 🐍 Streamlit App (Alternative)
- ✅ Real-time interactive dashboard
- ✅ Advanced charts and visualizations
- ✅ Detailed analytics
- ✅ Live at: https://ram4ik.streamlit.app/

---

## 🚀 Quick Start (GitHub Pages)

A comprehensive Streamlit dashboard for monitoring and analyzing GitHub traffic across all your iOS app landing pages.

## Features

### 🌍 Global Overview
- **Total Views & Unique Visitors**: Aggregate statistics across all your apps
- **Stars & Forks Tracking**: Monitor repository engagement
- **Real-time Updates**: Auto-refresh every 30 minutes

### 📈 Traffic Trends
- **Daily Traffic Charts**: Visualize views and unique visitors over time
- **Historical Analysis**: Track trends up to 90 days back
- **Combined Insights**: See aggregate performance across all apps

### 🏆 Performance Analytics
- **Top Performing Apps**: Ranked by views and engagement
- **Engagement Score**: Custom metric combining views and stars
- **Comparative Analysis**: See which apps resonate most with users

### 🔗 Traffic Sources
- **Referrer Tracking**: Discover where your traffic comes from
- **Source Analysis**: Identify most effective marketing channels
- **Geographic Insights**: Understand your global reach

### 📱 Individual App Details
- **Per-App Analytics**: Deep dive into specific app performance
- **Popular Content**: See which pages get the most visits
- **Trend Analysis**: Track individual app growth over time

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- GitHub account with repository access
- GitHub Personal Access Token

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd StreamlitAnalytics
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure GitHub Token

#### Option A: Using .env file (Local Development)

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Get your GitHub token:
   - Go to https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Select scopes: `repo` (for private repos) or `public_repo` (for public only)
   - Copy the generated token

3. Edit `.env` and add your token:
```
GITHUB_TOKEN=your_actual_token_here
```

#### Option B: Using Streamlit Secrets (Production/Cloud)

Create `.streamlit/secrets.toml`:
```bash
mkdir -p .streamlit
```

Add your token:
```toml
GITHUB_TOKEN = "your_actual_token_here"
```

### 4. Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

## Deploying to Streamlit Cloud

1. Push your code to GitHub (ensure `.env` is in `.gitignore`)
2. Go to https://share.streamlit.io
3. Deploy your repository
4. Add secrets in Streamlit Cloud dashboard:
   - Go to App settings → Secrets
   - Add: `GITHUB_TOKEN = "your_token"`

## Usage

### Dashboard Navigation

- **Sidebar**: Control refresh rate and date ranges
- **Overview Section**: Quick glance at total performance
- **Trends Section**: Analyze traffic patterns over time
- **Top Apps Section**: Identify your best performers
- **Sources Section**: Understand traffic origins
- **Individual Apps**: Deep dive into specific app metrics

### Updating Web Pages List

Edit `WEBPAGES.md` to add or remove app pages:
```
https://github.com/username/AppNamePage
https://github.com/username/AnotherAppPage
```

The dashboard will automatically pick up changes on next refresh.

## Features You Can Add in the Future

### 📊 Advanced Analytics
- Conversion tracking (stars → forks)
- Growth rate calculations
- Predictive analytics using ML

### 🔔 Alerts & Notifications
- Email alerts for traffic spikes
- Slack integration for daily summaries
- Anomaly detection

### 📤 Export & Reporting
- PDF report generation
- CSV data export
- Automated weekly/monthly reports

### 🎯 SEO & Marketing
- Keyword tracking
- Competitor analysis
- Social media integration

### 📱 App Store Integration
- App Store Connect API integration
- Download statistics
- Revenue tracking (if applicable)

### 🗺️ Geographic Analysis
- Visitor location mapping
- Regional performance insights
- Timezone-based traffic patterns

### 🔄 CI/CD Integration
- Automated deployment tracking
- Release correlation analysis
- A/B testing results

## Troubleshooting

### "GitHub token not found"
- Ensure your `.env` file exists and contains `GITHUB_TOKEN`
- For Streamlit Cloud, check secrets are properly configured

### "Could not fetch data"
- Verify your token has correct permissions (`repo` or `public_repo`)
- Check if repositories are accessible with your token
- Ensure repository names in WEBPAGES.md are correct

### Rate Limiting
- GitHub API has rate limits (5,000 requests/hour for authenticated users)
- Dashboard caches data for 30 minutes to minimize API calls
- If you hit limits, wait or reduce refresh frequency

## Project Structure

```
StreamlitAnalytics/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── WEBPAGES.md           # List of GitHub pages to track
├── .env                  # Environment variables (local)
├── .env.example          # Example environment file
├── .gitignore            # Git ignore file
├── README.md             # This file
└── .streamlit/
    └── secrets.toml      # Streamlit secrets (production)
```

## Technologies Used

- **Streamlit**: Web framework for data apps
- **Plotly**: Interactive visualizations
- **PyGithub**: GitHub API integration
- **Pandas**: Data manipulation
- **Python-dotenv**: Environment management

## Contributing

Feel free to open issues or submit pull requests to improve the dashboard!

## License

MIT License - Feel free to use and modify as needed.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review Streamlit documentation: https://docs.streamlit.io
3. Check GitHub API docs: https://docs.github.com/en/rest

---

**Built with ❤️ to help you track your iOS apps' global reach!**
