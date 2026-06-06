# GitHub Actions Setup 🤖

Your dashboard now uses **GitHub Actions** to automatically fetch and update analytics data!

## ✨ How It Works

1. **GitHub Actions runs** a Python script every 6 hours
2. **Fetches ALL data** from GitHub API (stars, forks, views, traffic)
3. **Saves to** `data/stats.json` file
4. **Your website reads** from this JSON file (no API calls needed!)
5. **Result**: Always shows data, no rate limits, works for all visitors!

---

## 🚀 Enable GitHub Actions (One-Time Setup)

### Step 1: Enable Actions

Your repository might have Actions disabled. To enable:

1. Go to: https://github.com/ram4ik/StreamlitAnalytics/settings/actions
2. Under "Actions permissions":
   - Select: ✅ **"Allow all actions and reusable workflows"**
3. Click **Save**

### Step 2: Manually Trigger First Run

Since the workflow is set to run every 6 hours, let's trigger it now:

1. Go to: https://github.com/ram4ik/StreamlitAnalytics/actions
2. Click on **"Update Analytics Data"** workflow (left sidebar)
3. Click **"Run workflow"** button (right side)
4. Select branch: **main**
5. Click green **"Run workflow"** button

### Step 3: Wait 1-2 Minutes

Watch the workflow run:
- Yellow circle 🟡 = Running
- Green checkmark ✅ = Success
- Red X ❌ = Failed (check logs)

### Step 4: Check Results

After success, you'll see:
- New file created: `data/stats.json`
- Commit message: "🤖 Update analytics data [skip ci]"
- Your website now has data!

---

## 🔍 How to Verify It's Working

### Method 1: Check the JSON file

Visit: https://github.com/ram4ik/StreamlitAnalytics/blob/main/data/stats.json

You should see all your analytics data!

### Method 2: Check your website

Visit: https://ram4ik.github.io/StreamlitAnalytics/

Now you'll see real data with stars, forks, views!

### Method 3: Check workflow runs

Visit: https://github.com/ram4ik/StreamlitAnalytics/actions

You'll see successful workflow runs.

---

## ⚙️ Configuration

### Change Update Frequency

Edit `.github/workflows/update-stats.yml` line 6:

```yaml
# Every 6 hours (current)
- cron: '0 */6 * * *'

# Every 3 hours
- cron: '0 */3 * * *'

# Every hour
- cron: '0 * * * *'

# Every day at midnight
- cron: '0 0 * * *'

# Twice a day (6am and 6pm UTC)
- cron: '0 6,18 * * *'
```

### Add More Repositories

Edit `scripts/fetch_stats.py` line 11, add to the `REPO_URLS` list:

```python
REPO_URLS = [
    'https://github.com/ram4ik/DocksidePage',
    'https://github.com/ram4ik/YourNewApp',  # Add here
    # ... rest
]
```

---

## 🎯 Benefits of This Approach

### ✅ Advantages
- **No rate limits** for visitors
- **Fast loading** (reads from file)
- **Historical data** preserved
- **Works without login** or token
- **Auto-updates** every 6 hours
- **GitHub traffic data** included (views, clones, referrers)
- **Free hosting** on GitHub

### 📊 Data Includes
- ⭐ Stars, forks, watchers
- 👁️ Views (last 14 days)
- 👥 Unique visitors
- 📥 Clone statistics
- 🔗 Traffic sources (referrers)
- 📄 Popular pages
- 🕐 Last update time

---

## 🐛 Troubleshooting

### Workflow not running?

**Check 1:** Actions enabled?
- Go to Settings → Actions → General
- Ensure "Allow all actions" is selected

**Check 2:** Workflow file syntax?
```bash
# Test locally
cd /Users/ribragimov/Desktop/StreamlitAnalytics
python scripts/fetch_stats.py
```

**Check 3:** GitHub token permissions?
- Default `GITHUB_TOKEN` should work
- Has read access to public repos

### No data showing?

**Cause 1:** Actions hasn't run yet
- **Solution:** Manually trigger (see Step 2 above)

**Cause 2:** `data/stats.json` missing
- **Solution:** Check workflow logs for errors

**Cause 3:** CORS issues
- **Solution:** None! Static files on GitHub Pages don't have CORS issues

### Workflow failing?

**Check logs:**
1. Go to Actions tab
2. Click failed workflow
3. Click the job
4. Read error messages

**Common issues:**
- Missing dependencies → Check `update-stats.yml`
- API rate limit → Shouldn't happen with Actions
- Permission denied → Check repository settings

---

## 📈 Manual Data Update

Want to update data immediately? Two ways:

### Method 1: GitHub UI (Easy)
1. Go to Actions tab
2. Click "Update Analytics Data"
3. Click "Run workflow"

### Method 2: Command Line
```bash
# Trigger via GitHub API
curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/repos/ram4ik/StreamlitAnalytics/actions/workflows/update-stats.yml/dispatches \
  -d '{"ref":"main"}'
```

---

## 🔐 Security Notes

### GitHub Token
- Workflow uses `secrets.GITHUB_TOKEN`
- Automatically provided by GitHub
- Expires after each run
- No setup needed!

### Data Privacy
- Only fetches **public** repository data
- No personal information collected
- Safe to share publicly

---

## 📊 Data Structure

The `data/stats.json` file contains:

```json
{
  "last_updated": "2026-06-05T23:00:00Z",
  "total_stats": {
    "total_apps": 23,
    "total_stars": 150,
    "total_forks": 45,
    "total_watchers": 200,
    "total_views_14d": 1250,
    "total_unique_visitors_14d": 450,
    "total_clones_14d": 30
  },
  "apps": {
    "Dockside": {
      "info": { /* repo details */ },
      "views": { /* view statistics */ },
      "clones": { /* clone statistics */ },
      "referrers": [ /* traffic sources */ ],
      "paths": [ /* popular pages */ ]
    },
    // ... more apps
  }
}
```

---

## 🎨 Customization

### Display More Stats

Edit `index.html` around line 450 to show additional fields:

```javascript
// Add to app card
<div class="app-stat">
    <span class="label">📥 Clones</span>
    <span class="value">${(app.clones.count || 0).toLocaleString()}</span>
</div>
```

### Add Charts

Use Chart.js or similar library to visualize trends over time.

### Export Data

The JSON file can be:
- Downloaded directly
- Parsed by other tools
- Used in other dashboards
- Imported to spreadsheets

---

## ✅ Checklist

After setup, verify:

- [ ] GitHub Actions is enabled in repository settings
- [ ] Workflow has run at least once successfully
- [ ] `data/stats.json` file exists in repository
- [ ] Website shows real data (not zeros)
- [ ] Workflow is scheduled to run every 6 hours
- [ ] Manual trigger works from Actions tab

---

## 🚀 Next Steps

1. **Enable GitHub Pages** (if not already):
   - Settings → Pages → Source: main branch, / (root)

2. **Wait for first workflow run** (or trigger manually)

3. **Visit your dashboard**: https://ram4ik.github.io/StreamlitAnalytics/

4. **Share your analytics** with the world! 🎉

---

## 📞 Support

- **Workflow Logs**: Check Actions tab for errors
- **GitHub Actions Docs**: https://docs.github.com/actions
- **Cron Schedule**: https://crontab.guru

---

**Your dashboard will now auto-update every 6 hours with fresh data!** 🎉
