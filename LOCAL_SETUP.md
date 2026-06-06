# Local Development Setup 💻

Quick guide to run the dashboard on your local machine.

## First Time Setup

### Option 1: Automated Setup (Recommended)
```bash
cd /Users/ribragimov/Desktop/StreamlitAnalytics
./setup_local.sh
```

This will:
- Install all required packages
- Create `.env` file
- Guide you through adding your GitHub token
- Optionally start the app

### Option 2: Manual Setup

1. **Install dependencies**:
```bash
cd /Users/ribragimov/Desktop/StreamlitAnalytics
pip install -r requirements.txt
```

2. **Set up GitHub token**:
```bash
cp .env.example .env
nano .env  # or use any text editor
```

Add your token:
```
GITHUB_TOKEN=ghp_your_token_here
```

Get token at: https://github.com/settings/tokens (need `public_repo` scope)

## Running the Dashboard

### Option 1: Simple Start
```bash
streamlit run app.py
```

### Option 2: Using the helper script
```bash
./run.sh
```

### Option 3: Custom port
```bash
# If port 8501 is busy
streamlit run app.py --server.port=8502

# Or with helper script
./run.sh 8502
```

### Option 4: With custom options
```bash
# Open in browser automatically
streamlit run app.py --server.headless=false

# Don't watch for file changes
streamlit run app.py --server.fileWatcherType=none

# Combine options
streamlit run app.py --server.port=8502 --server.headless=false
```

## Accessing the Dashboard

Once started, open your browser to:
- **Default**: http://localhost:8501
- **Custom port**: http://localhost:YOUR_PORT

Or just wait - Streamlit usually opens browser automatically!

## Stopping the Dashboard

Press `Ctrl+C` in the terminal

## Common Issues

### "Port 8501 is not available"

**Cause**: Another Streamlit app or process is using that port.

**Solutions**:

1. **Use a different port**:
```bash
streamlit run app.py --server.port=8502
```

2. **Kill the existing process** (macOS/Linux):
```bash
lsof -ti:8501 | xargs kill -9
```

3. **Kill the existing process** (Windows):
```bash
netstat -ano | findstr :8501
taskkill /PID <PID_NUMBER> /F
```

### "GITHUB_TOKEN not found"

**Cause**: `.env` file missing or token not set.

**Solution**:
```bash
cp .env.example .env
nano .env  # Add your token
```

### "Module not found"

**Cause**: Dependencies not installed.

**Solution**:
```bash
pip install -r requirements.txt
```

### "WEBPAGES.md not found"

**Cause**: Running from wrong directory.

**Solution**:
```bash
cd /Users/ribragimov/Desktop/StreamlitAnalytics
streamlit run app.py
```

### Config warnings about CORS/XSRF

These warnings are harmless and can be ignored. The `.streamlit/config.toml` has been configured to minimize warnings.

## Development Tips

### Auto-reload on changes

Streamlit watches for file changes automatically. When you edit `app.py`:
1. Save the file
2. Click "Rerun" in the browser (or press `R`)

### Clear cache

If data seems stale:
1. Click "🔄 Refresh Data" in the sidebar
2. Or press `C` in the browser to clear cache and rerun

### View in network

To access from other devices on your network:
```bash
streamlit run app.py --server.address=0.0.0.0
```

Then access at: `http://YOUR_LOCAL_IP:8501`

### Debug mode

For more verbose output:
```bash
streamlit run app.py --logger.level=debug
```

## Virtual Environment (Recommended)

Using a virtual environment keeps dependencies isolated:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# When done, deactivate
deactivate
```

## File Watching

If auto-reload isn't working:
```bash
# Disable file watcher
streamlit run app.py --server.fileWatcherType=none

# Use polling instead of native watcher
streamlit run app.py --server.fileWatcherType=poll
```

## Environment Variables

Alternative to `.env` file - set directly in terminal:

**macOS/Linux**:
```bash
export GITHUB_TOKEN=ghp_your_token_here
streamlit run app.py
```

**Windows**:
```bash
set GITHUB_TOKEN=ghp_your_token_here
streamlit run app.py
```

## Testing Changes Before Deployment

1. Edit code locally
2. Test with `streamlit run app.py`
3. Verify everything works
4. Commit and push:
```bash
git add .
git commit -m "Description of changes"
git push origin main
```

Streamlit Cloud will auto-deploy your changes!

## Useful Streamlit Commands

```bash
# Check Streamlit version
streamlit version

# View config options
streamlit config show

# Create new Streamlit app
streamlit hello

# Get help
streamlit --help
```

## Project Structure

```
StreamlitAnalytics/
├── app.py              # Main application
├── WEBPAGES.md         # List of GitHub repos
├── requirements.txt    # Python dependencies
├── .env               # Your GitHub token (local only)
├── .streamlit/
│   └── config.toml    # Streamlit configuration
└── run.sh            # Helper script to start app
```

## Performance Tips

### Speed up local development:

1. **Reduce cache TTL** for faster refreshes during development:
```python
@st.cache_data(ttl=300)  # 5 minutes instead of 30
```

2. **Comment out expensive operations** you're not working on

3. **Test with fewer repos** temporarily:
   - Edit `WEBPAGES.md` and comment out most URLs (add `#` at start)
   - Uncomment when done testing

## Keyboard Shortcuts

In the browser when dashboard is open:

- `R` - Rerun the app
- `C` - Clear cache and rerun
- `S` - Take a screenshot
- `/` - Focus search (in sidebar)
- `?` - Show keyboard shortcuts

## Next Steps

Once everything works locally:

1. **Push to GitHub**:
```bash
git add .
git commit -m "Local development working"
git push origin main
```

2. **Deploy to Streamlit Cloud** (see `DEPLOYMENT_GUIDE.md`)

3. **Share your live dashboard** with the world! 🌍

---

**Need help?** Check `TROUBLESHOOTING.md` or `README.md`
