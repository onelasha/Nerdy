# 🚀 Deployment Guide - Streamlit Cloud

## Prerequisites

✅ GitHub repository: `https://github.com/onelasha/Nerdy`  
✅ Streamlit Cloud account (free): `https://share.streamlit.io`

## Step-by-Step Deployment

### 1. Sign Up / Log In to Streamlit Cloud

1. Go to **https://share.streamlit.io**
2. Click **"Sign up"** or **"Sign in"**
3. Authenticate with your **GitHub account** (onelasha)

### 2. Deploy Your App

1. Click **"New app"** button
2. Fill in the deployment form:
   - **Repository:** `onelasha/Nerdy`
   - **Branch:** `main`
   - **Main file path:** `dashboard.py`
   - **App URL:** Choose a custom URL (e.g., `nerdy-student-risk-dashboard`)

3. Click **"Deploy!"**

### 3. Configure Secrets (Optional - For AI Features)

If you want AI-powered explanations and recommendations:

1. After deployment, click **"⚙️ Settings"** in your app
2. Go to **"Secrets"** section
3. Add your Anthropic API key:

```toml
ANTHROPIC_API_KEY = "your-anthropic-api-key-here"
```

4. Click **"Save"**
5. App will automatically restart with AI features enabled

**Note:** The app works perfectly without the API key using rule-based analysis!

### 4. Your App is Live! 🎉

Your dashboard will be available at:
```
https://[your-custom-url].streamlit.app
```

Example: `https://nerdy-student-risk-dashboard.streamlit.app`

## What Happens During Deployment

1. **Streamlit Cloud clones your repo** from GitHub
2. **Installs dependencies** from `requirements.txt`
3. **Runs `dashboard.py`** automatically
4. **Auto-generates data** on first run (thanks to our auto-generation feature!)
5. **Serves the app** publicly

## Deployment Files

Your repo already has everything needed:

- ✅ `requirements.txt` - Python dependencies
- ✅ `dashboard.py` - Main application
- ✅ `generate_data.py` - Auto-generates data if missing
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ `packages.txt` - System dependencies (empty, but ready)

## Managing Your Deployment

### Update Your App

Just push changes to GitHub:
```bash
git add .
git commit -m "Update dashboard"
git push origin main
```

Streamlit Cloud will **automatically redeploy** within seconds!

### View Logs

1. Go to your app on Streamlit Cloud
2. Click **"⋮"** menu (top right)
3. Select **"Logs"** to see console output

### Reboot App

If needed:
1. Click **"⋮"** menu
2. Select **"Reboot app"**

### Delete App

1. Go to **https://share.streamlit.io**
2. Find your app in the dashboard
3. Click **"⋮"** → **"Delete app"**

## Troubleshooting

### "Module not found" errors
- Check `requirements.txt` has all dependencies
- Verify package names and versions

### App won't start
- Check logs for errors
- Ensure `dashboard.py` is in the root directory
- Verify GitHub repo is public or Streamlit has access

### Data not loading
- The app auto-generates data on first run
- Check logs to see if generation succeeded
- Data generation happens automatically via `load_data()` function

### AI features not working
- Add `ANTHROPIC_API_KEY` to Secrets (optional)
- App works without it using rule-based analysis

## Performance Considerations

### Free Tier Limits
- **1 GB RAM** per app
- **1 CPU core**
- Apps sleep after **7 days** of inactivity
- **Unlimited public apps**

### Optimization Tips
- Data is cached with `@st.cache_data`
- 75 students runs smoothly on free tier
- For 1000+ students, consider upgrading

## Custom Domain (Optional)

Streamlit Cloud provides:
- Default: `your-app.streamlit.app`
- Custom domains available on paid plans

## Sharing Your App

Share the URL with:
- **Varsity Tutors team** for case study review
- **Stakeholders** for demo
- **Portfolio** to showcase your work

### Example Share Message

```
🎉 Student Risk Dashboard is live!

Check it out: https://[your-url].streamlit.app

Features:
✅ AI-powered risk analysis
✅ Interactive visualizations
✅ Personalized recommendations
✅ Real-time filtering

Built for the Varsity Tutors Director of Engineering case study.
```

## Security Notes

### What's Public
- ✅ Source code (GitHub repo)
- ✅ Dashboard UI
- ✅ Sample data (generated, not real students)

### What's Private
- 🔒 API keys (stored in Streamlit Secrets)
- 🔒 Environment variables
- 🔒 `.streamlit/secrets.toml` (gitignored)

### Best Practices
- Never commit API keys to Git
- Use Streamlit Secrets for sensitive data
- Sample data only (no real student PII)

## Monitoring

### Analytics
Streamlit Cloud provides:
- **View count**
- **Active users**
- **Resource usage**
- **Error rates**

Access via app dashboard on Streamlit Cloud.

## Next Steps After Deployment

1. ✅ Test the live app thoroughly
2. ✅ Share URL with Varsity Tutors
3. ✅ Add to your portfolio/resume
4. ✅ Monitor usage and feedback
5. ✅ Iterate based on feedback

## Support

- **Streamlit Docs:** https://docs.streamlit.io
- **Community Forum:** https://discuss.streamlit.io
- **GitHub Issues:** For app-specific issues

---

## Quick Deployment Checklist

- [ ] GitHub repo is up to date (`git push`)
- [ ] All files committed (especially `.streamlit/config.toml`)
- [ ] Signed up for Streamlit Cloud
- [ ] Connected GitHub account
- [ ] Deployed app with correct settings
- [ ] (Optional) Added ANTHROPIC_API_KEY to Secrets
- [ ] Tested live app
- [ ] Shared URL

**Estimated deployment time:** 5-10 minutes

---

**Your app is ready to deploy!** 🚀

Just follow the steps above and you'll have a live, shareable dashboard in minutes.
