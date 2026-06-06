# GitHub Pages Setup Guide 🚀

Deploy your analytics dashboard to GitHub Pages in 3 minutes!

## Quick Setup (3 Steps)

### Step 1: Push Code to GitHub

```bash
cd /Users/ribragimov/Desktop/StreamlitAnalytics

git add index.html GITHUB_PAGES_SETUP.md
git commit -m "Add static HTML dashboard for GitHub Pages"
git push origin main
```

### Step 2: Enable GitHub Pages

1. Go to your repository: https://github.com/ram4ik/StreamlitAnalytics
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under "Source":
   - Select branch: **main**
   - Select folder: **/ (root)**
5. Click **Save**

### Step 3: Visit Your Site

Your dashboard will be live at:
```
https://ram4ik.github.io/StreamlitAnalytics/
```

⏱️ **Takes 2-3 minutes** for first deployment.

---

## ✨ Features of Static Dashboard

### 🎯 What Works
- ✅ Real-time data fetching from GitHub API
- ✅ Auto-updates every 5 minutes
- ✅ Shows all 23 iOS apps
- ✅ Displays stars, forks, watchers
- ✅ Mobile responsive design
- ✅ Beautiful gradient UI
- ✅ No server needed
- ✅ Free hosting on GitHub Pages

### 📊 Statistics Shown
- Total apps count
- Total stars across all apps
- Total forks
- Total watchers
- Individual app stats
- Last update timestamp
- App descriptions
- Programming languages

### 🔒 GitHub Token (Optional)
- **Without token**: 60 API requests per hour (fine for most users)
- **With token**: 5,000 requests per hour
- Token stored locally in browser (secure)
- Can view analytics without token

---

## 🎨 Customization

### Change Colors

Edit `index.html` line 15-16:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Try these gradients:
- Blue to Purple: `#667eea 0%, #764ba2 100%`
- Ocean: `#2E3192 0%, #1BFFFF 100%`
- Sunset: `#FF512F 0%, #F09819 100%`
- Forest: `#134E5E 0%, #71B280 100%`

### Change Title

Edit line 66:
```html
<h1>📱 iOS Apps Analytics Dashboard</h1>
```

### Add More Repositories

Edit `index.html` around line 227, add to the array:
```javascript
const repoUrls = [
    'https://github.com/ram4ik/DocksidePage',
    'https://github.com/ram4ik/YourNewApp',  // Add here
    // ... rest
];
```

---

## 🌐 Custom Domain (Optional)

Want to use your own domain like `analytics.yourdomain.com`?

### Step 1: Add CNAME file

```bash
echo "analytics.yourdomain.com" > CNAME
git add CNAME
git commit -m "Add custom domain"
git push origin main
```

### Step 2: Configure DNS

In your domain provider (GoDaddy, Namecheap, etc):

Add CNAME record:
```
Type: CNAME
Name: analytics
Value: ram4ik.github.io
```

### Step 3: Enable in GitHub Settings

1. Go to Settings → Pages
2. Enter your custom domain: `analytics.yourdomain.com`
3. Check "Enforce HTTPS"
4. Save

Done! Your dashboard will be at your custom domain.

---

## 📱 Embedding in Another Website

Want to embed this in your portfolio? Use an iframe:

```html
<iframe 
    src="https://ram4ik.github.io/StreamlitAnalytics/" 
    width="100%" 
    height="800px" 
    frameborder="0">
</iframe>
```

---

## 🔄 Updating Data

### Automatic Updates
Dashboard fetches fresh data:
- Every time page loads
- Every 5 minutes while page is open
- When "Refresh Data" button clicked

### Manual Updates
Just refresh the browser page (F5 or Cmd+R)

---

## 🆚 Comparison: GitHub Pages vs Streamlit Cloud

| Feature | GitHub Pages (Static) | Streamlit Cloud (Dynamic) |
|---------|----------------------|---------------------------|
| **Hosting** | Free, Fast | Free, Fast |
| **Setup** | 3 steps | 3 steps |
| **Tech** | HTML/CSS/JS | Python |
| **Data** | Real-time API calls | Server-side processing |
| **Traffic Data** | ❌ No (API limitation) | ✅ Yes (views, clones) |
| **Interactivity** | Basic | Advanced |
| **Charts** | Basic stats | Interactive Plotly |
| **Custom Domain** | ✅ Yes | ✅ Yes |
| **Best For** | Simple stats, portfolios | Full analytics, dashboards |

**Recommendation**: Use **both**!
- GitHub Pages: Quick stats page
- Streamlit Cloud: Full analytics dashboard

---

## 🐛 Troubleshooting

### "404 Page Not Found"
- Wait 3-5 minutes after enabling Pages
- Check Settings → Pages shows green checkmark
- Verify branch is `main` and folder is `/ (root)`

### "API Rate Limit Exceeded"
- Add GitHub token in settings panel
- Token gives 5,000 requests/hour vs 60 without
- Get token: https://github.com/settings/tokens

### "No Data Showing"
- Check browser console (F12)
- Verify internet connection
- Try with GitHub token
- Check repository URLs are correct

### "Styles Not Loading"
- Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Clear browser cache
- Wait for GitHub Pages to fully deploy

---

## 📈 Analytics for Your GitHub Pages

Want to track visitors to your dashboard?

### Option 1: GitHub built-in (Settings → Insights → Traffic)

### Option 2: Google Analytics

Add before `</head>` in `index.html`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Option 3: Simple Analytics (Privacy-friendly)

Add before `</body>`:
```html
<script async defer src="https://scripts.simpleanalyticscdn.com/latest.js"></script>
```

---

## 🚀 Advanced: Automated Updates with GitHub Actions

Want to cache data and update hourly? Create `.github/workflows/update-data.yml`:

```yaml
name: Update Analytics Data
on:
  schedule:
    - cron: '0 * * * *'  # Every hour
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Fetch and cache data
        run: |
          # Your script to fetch and save data to JSON
          # Then commit and push
```

---

## 📋 Checklist

Before going live:

- [ ] Pushed `index.html` to main branch
- [ ] Enabled GitHub Pages in Settings
- [ ] Verified site loads at `username.github.io/repo`
- [ ] Tested on mobile device
- [ ] Optionally added GitHub token for higher limits
- [ ] Shared your dashboard URL! 🎉

---

## 🌟 Next Steps

1. **Share your dashboard**: Add link to README.md
2. **Add to portfolio**: Show off your analytics site
3. **Monitor performance**: Check GitHub Insights
4. **Keep updating**: Push new features anytime

---

## 📞 Support

- **GitHub Pages Docs**: https://docs.github.com/pages
- **GitHub API Docs**: https://docs.github.com/rest
- **Issues**: Create issue in your repository

---

**Your dashboard is now live! 🎉**

Share it: `https://ram4ik.github.io/StreamlitAnalytics/`
