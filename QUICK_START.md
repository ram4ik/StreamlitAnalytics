# Quick Start Guide ⚡

## Option 1: Automated Setup (Easiest)

```bash
cd /Users/ribragimov/Desktop/StreamlitAnalytics
./setup_local.sh
```

This script will:
- Install all required packages
- Create .env file
- Guide you through token setup
- Optionally start the app

## Option 2: Manual Setup

### 1️⃣ Install Packages

```bash
cd /Users/ribragimov/Desktop/StreamlitAnalytics
pip install -r requirements.txt
```

### 2️⃣ Setup GitHub Token

```bash
# Copy template
cp .env.example .env

# Edit .env and add your token
# Get token from: https://github.com/settings/tokens
nano .env  # or use your preferred editor
```

Add this line to .env:
```
GITHUB_TOKEN=ghp_your_actual_token_here
```

### 3️⃣ Run Dashboard

```bash
streamlit run app.py
```

## Deploy to GitHub & Streamlit Cloud

### Step 1: Create GitHub Repo
1. Go to https://github.com/new
2. Name: `ios-apps-analytics`
3. Make it **Public**
4. Don't initialize with README

### Step 2: Push Code

```bash
cd /Users/ribragimov/Desktop/StreamlitAnalytics

# Initialize git
git init
git add .
git commit -m "Initial commit: iOS Apps Analytics Dashboard"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ios-apps-analytics.git

# Push
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `ios-apps-analytics`
5. Main file: `app.py`
6. Click "Advanced settings"
7. Add secret:
   ```toml
   GITHUB_TOKEN = "your_token_here"
   ```
8. Click "Deploy!"

**Done!** Your app will be live in 2-3 minutes at:
`https://YOUR_USERNAME-ios-apps-analytics.streamlit.app`

## Package Installation on Streamlit Cloud

**Streamlit Cloud automatically installs packages!**

When you deploy:
- ✅ Reads `requirements.txt`
- ✅ Installs all packages automatically
- ✅ Uses Python 3.9+ environment
- ✅ No manual installation needed!

## Update Deployed App

```bash
# Make changes to code
git add .
git commit -m "Updated analytics features"
git push origin main
```

Streamlit Cloud auto-detects and redeploys in ~2 minutes!

## Troubleshooting

**Issue**: `pip install` fails
**Solution**: Try `pip3 install -r requirements.txt`

**Issue**: `streamlit: command not found`
**Solution**: Make sure packages installed successfully, try `python -m streamlit run app.py`

**Issue**: Can't access GitHub data
**Solution**: Check your token has `public_repo` permission

**Issue**: Build fails on Streamlit Cloud
**Solution**: Check logs in Streamlit Cloud dashboard → Your app → Manage → Logs

## Need Help?

- 📖 Full guide: `DEPLOYMENT_GUIDE.md`
- 📚 README: `README.md`
- 💬 Streamlit Community: https://discuss.streamlit.io

---

**Ready?** Run `./setup_local.sh` to get started! 🚀
