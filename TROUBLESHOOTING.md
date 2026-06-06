# Troubleshooting Guide 🔧

Common issues and solutions for the iOS Apps Analytics Dashboard.

## Deployment Issues

### ❌ "Failed to build pillow" during deployment

**Problem**: Pillow can't compile due to missing system libraries.

**Solution**: Make sure these files exist in your repo:
- `packages.txt` - Contains system dependencies
- `.python-version` - Specifies Python 3.11
- `runtime.txt` - Alternative Python version specification

If still failing:
1. Check Streamlit Cloud logs for specific missing library
2. Add missing library to `packages.txt`
3. Push changes: `git push origin main`

### ❌ "Python 3.14 compatibility issues"

**Problem**: Bleeding-edge Python version lacks pre-built wheels.

**Solution**: Files `.python-version` and `runtime.txt` pin to Python 3.11.

If you need to change Python version:
```bash
echo "3.11" > .python-version
echo "python-3.11" > runtime.txt
git add .python-version runtime.txt
git commit -m "Pin Python version"
git push origin main
```

## Runtime Errors

### ❌ "Cannot hash argument 'github_client'"

**Problem**: Streamlit can't cache functions with unhashable parameters.

**Solution**: Add underscore prefix to parameter name:
```python
@st.cache_data(ttl=1800)
def fetch_repo_traffic(_github_client, owner, repo_name):  # Note the underscore
    repo = _github_client.get_repo(f"{owner}/{repo_name}")
```

### ❌ "GitHub token not found"

**Problem**: Missing or incorrect GitHub token configuration.

**Solution for local development**:
1. Copy `.env.example` to `.env`
2. Add your token: `GITHUB_TOKEN=ghp_your_token_here`

**Solution for Streamlit Cloud**:
1. Go to https://share.streamlit.io
2. Click your app → Settings → Secrets
3. Add:
   ```toml
   GITHUB_TOKEN = "ghp_your_token_here"
   ```
4. Reboot app

### ❌ "Could not fetch data for [repo]"

**Problem**: GitHub API access issues.

**Possible causes**:
1. **Token lacks permissions**
   - Solution: Generate new token with `public_repo` or `repo` scope
   
2. **Rate limiting**
   - GitHub allows 5,000 requests/hour for authenticated users
   - Solution: Wait an hour or reduce refresh frequency
   
3. **Private repository**
   - Solution: Use token with `repo` scope (not just `public_repo`)
   
4. **Repository doesn't exist**
   - Solution: Check repository name in `WEBPAGES.md`

### ❌ "WEBPAGES.md file not found"

**Problem**: File missing or in wrong location.

**Solution**: 
1. Ensure `WEBPAGES.md` is in root directory
2. Check it's committed to git:
   ```bash
   git add WEBPAGES.md
   git commit -m "Add WEBPAGES.md"
   git push origin main
   ```

## Data Issues

### ⚠️ "No traffic data showing"

**Problem**: Fresh repositories or no visitors yet.

**Why**: GitHub only provides traffic data for the last 14 days, and only if there are visitors.

**Solution**: 
- Wait for visitors to access your pages
- Share your repository links to generate traffic
- Check back in a few days

### ⚠️ "Data seems outdated"

**Problem**: Cache hasn't refreshed.

**Solution**:
1. Click "🔄 Refresh Data" button in sidebar
2. Or wait 30 minutes for automatic refresh
3. Or adjust cache TTL in code:
   ```python
   @st.cache_data(ttl=900)  # 15 minutes instead of 30
   ```

### ⚠️ "Missing some repositories"

**Problem**: Repository URLs incorrect in WEBPAGES.md.

**Solution**: Check format in `WEBPAGES.md`:
```
https://github.com/username/RepoName
https://github.com/username/AnotherRepo
```

Each URL should be:
- On its own line
- Complete GitHub URL
- Accessible with your token

## Performance Issues

### 🐌 "Dashboard loads slowly"

**Problem**: Fetching data for many repositories takes time.

**Solutions**:
1. **Increase cache time** (fetch less often):
   ```python
   @st.cache_data(ttl=3600)  # 1 hour
   ```

2. **Reduce number of repos** (temporarily for testing):
   - Comment out some lines in `WEBPAGES.md`

3. **Use pagination**: Modify code to load repos in batches

### 🐌 "Timeout errors"

**Problem**: GitHub API calls taking too long.

**Solution**: Add timeout and retry logic:
```python
from github import Github
import time

github_client = Github(token, timeout=30)
```

## Local Development Issues

### ❌ "streamlit: command not found"

**Problem**: Streamlit not installed or not in PATH.

**Solution**:
```bash
pip install -r requirements.txt
# Or
python -m streamlit run app.py
```

### ❌ "Module not found" errors

**Problem**: Dependencies not installed.

**Solution**:
```bash
# Install all dependencies
pip install -r requirements.txt

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### ❌ "Permission denied: .env"

**Problem**: File permissions issue.

**Solution**:
```bash
chmod 600 .env
```

## Streamlit Cloud Specific

### ❌ "App stuck in 'Deploying' state"

**Problem**: Build process hanging.

**Solutions**:
1. Check logs in Streamlit Cloud dashboard
2. Reboot app from settings
3. If still stuck, delete and recreate app

### ❌ "Secrets not loading"

**Problem**: Secrets configuration incorrect.

**Solution**:
1. Go to App settings → Secrets
2. Use TOML format (not JSON):
   ```toml
   GITHUB_TOKEN = "value_here"
   ```
3. No commas, no trailing spaces
4. Reboot app after saving

### ❌ "App keeps rebooting"

**Problem**: Code error causing crashes.

**Solution**:
1. Check logs for Python errors
2. Test locally first:
   ```bash
   streamlit run app.py
   ```
3. Fix errors and push:
   ```bash
   git add .
   git commit -m "Fix error"
   git push origin main
   ```

## GitHub API Limits

### ⚠️ "API rate limit exceeded"

**Problem**: Too many requests to GitHub API.

**Current limits**:
- Authenticated: 5,000 requests/hour
- Unauthenticated: 60 requests/hour

**Solutions**:
1. **Ensure token is being used** (check logs)
2. **Increase cache TTL**:
   ```python
   @st.cache_data(ttl=3600)  # Cache for 1 hour
   ```
3. **Reduce refresh frequency**
4. **Wait for rate limit to reset** (shown in error message)

**Check your rate limit**:
```bash
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/rate_limit
```

## Getting Help

If you can't resolve an issue:

1. **Check logs**:
   - Local: Terminal output
   - Cloud: Streamlit dashboard → Manage app → Logs

2. **Verify configuration**:
   - Is token valid and has correct permissions?
   - Are all files pushed to GitHub?
   - Is Python version correct?

3. **Test locally first**:
   ```bash
   cd /path/to/StreamlitAnalytics
   streamlit run app.py
   ```

4. **Community support**:
   - Streamlit Community: https://discuss.streamlit.io
   - GitHub Issues: Create issue in your repo

## Quick Fixes Reference

```bash
# Refresh deployment
git add .
git commit -m "Fix: description"
git push origin main

# Clear local cache
rm -rf ~/.streamlit/cache

# Reinstall dependencies
pip install -r requirements.txt --upgrade --force-reinstall

# Check Python version
python --version

# Check git status
git status

# View recent commits
git log --oneline -5

# Revert last commit (if needed)
git revert HEAD
git push origin main
```

## Preventive Maintenance

### Regular checks:
- ✅ Verify GitHub token hasn't expired
- ✅ Check for outdated dependencies
- ✅ Monitor API usage
- ✅ Review error logs weekly
- ✅ Test locally before pushing major changes

### Updates:
```bash
# Update dependencies (periodically)
pip list --outdated
pip install -r requirements.txt --upgrade

# Update requirements.txt
pip freeze > requirements.txt

# Commit and push
git add requirements.txt
git commit -m "Update dependencies"
git push origin main
```

---

**Still having issues?** Create an issue in your GitHub repository with:
- Error message (full stack trace)
- What you were trying to do
- Steps to reproduce
- Environment (local/cloud, Python version, etc.)
