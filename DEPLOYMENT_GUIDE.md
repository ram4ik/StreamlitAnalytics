# Deployment Guide 🚀

Complete guide to deploy your iOS Apps Analytics Dashboard to GitHub and Streamlit Cloud.

## Part 1: Push to GitHub

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository:
   - Name: `ios-apps-analytics` (or your preferred name)
   - Description: "Analytics dashboard for tracking iOS app landing pages"
   - **Important**: Make it **Public** (required for free Streamlit Cloud)
   - **Do NOT** initialize with README (we already have files)

### Step 2: Push Your Code

Open Terminal and run these commands:

```bash
# Navigate to your project
cd /Users/ribragimov/Desktop/StreamlitAnalytics

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: iOS Apps Analytics Dashboard"

# Add your GitHub repository as remote
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/ios-apps-analytics.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Important**: Your `.env` file with the token will NOT be pushed (it's in `.gitignore` for security).

## Part 2: Deploy to Streamlit Cloud

### Step 3: Sign Up for Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click "Sign up" or "Continue with GitHub"
3. Authorize Streamlit to access your GitHub repositories

### Step 4: Deploy Your App

1. Click "New app" button
2. Fill in the form:
   - **Repository**: Select `YOUR_USERNAME/ios-apps-analytics`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. Click "Advanced settings" (IMPORTANT!)

### Step 5: Add Secrets (CRITICAL!)

In the Advanced settings, add your GitHub token:

```toml
# Add this in the Secrets section:
GITHUB_TOKEN = "ghp_your_actual_token_here"
```

**How to get your GitHub token:**
1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name: "Streamlit Analytics Dashboard"
4. Select scope: ✅ `public_repo` (or `repo` if you have private repos)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again!)
7. Paste it in Streamlit Cloud secrets

### Step 6: Deploy!

1. Click "Deploy!"
2. Wait 2-3 minutes for installation and deployment
3. Your app will be live at: `https://YOUR_USERNAME-ios-apps-analytics.streamlit.app`

## Automatic Package Installation

**Great news!** Streamlit Cloud automatically:
- ✅ Installs all packages from `requirements.txt`
- ✅ Uses Python 3.9+ environment
- ✅ Handles all dependencies
- ✅ Rebuilds when you push code changes

**You don't need to install anything manually!**

## Part 3: Update Your App

Whenever you want to update the dashboard:

```bash
# Make your changes to the code
# Then:

git add .
git commit -m "Description of your changes"
git push origin main
```

Streamlit Cloud will automatically:
- Detect the push
- Rebuild the app
- Deploy the new version (takes ~2 minutes)

## Part 4: Share Your Dashboard

Once deployed, you can:
- Share the public URL with anyone
- Embed it in your website
- Add it to your GitHub profile README
- Share on social media

## Troubleshooting

### "Could not fetch data" error
- Check that your GITHUB_TOKEN is correctly set in Streamlit Cloud secrets
- Verify the token has `public_repo` or `repo` permissions
- Make sure repositories in WEBPAGES.md are accessible

### "App is down" or build errors
- Check the "Manage app" → "Logs" section in Streamlit Cloud
- Verify all files were pushed to GitHub
- Make sure requirements.txt is in the root directory

### Rate limiting
- GitHub API allows 5,000 requests/hour for authenticated users
- Dashboard caches data for 30 minutes to minimize calls
- If you hit limits, wait an hour or reduce refresh frequency

### Need to update secrets
1. Go to https://share.streamlit.io
2. Find your app → Click "⋮" → "Settings"
3. Update secrets in the Secrets section
4. Click "Save"
5. Reboot the app

## Commands Reference

```bash
# Clone your repo (on a new machine)
git clone https://github.com/YOUR_USERNAME/ios-apps-analytics.git
cd ios-apps-analytics

# Pull latest changes
git pull origin main

# Push changes
git add .
git commit -m "Your message"
git push origin main

# Check git status
git status

# View remote URL
git remote -v
```

## Security Best Practices

✅ **DO:**
- Keep your GitHub token in Streamlit secrets (not in code)
- Use `.gitignore` to exclude `.env` files
- Regenerate tokens periodically
- Use tokens with minimal required permissions

❌ **DON'T:**
- Commit `.env` file to GitHub
- Share your GitHub token publicly
- Use personal access tokens with full permissions
- Hardcode tokens in your code

## Next Steps

1. ✅ Push code to GitHub
2. ✅ Deploy to Streamlit Cloud
3. ✅ Add GitHub token to secrets
4. 🎉 Share your live dashboard!

## Support

- Streamlit Docs: https://docs.streamlit.io
- Streamlit Community: https://discuss.streamlit.io
- GitHub Docs: https://docs.github.com

---

**Ready to deploy?** Follow Steps 1-6 above! 🚀
