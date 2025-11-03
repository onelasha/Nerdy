# 🔒 Security Guide - API Key Management

## ⚠️ NEVER Commit API Keys to Git

API keys should **NEVER** be:
- Hardcoded in source code
- Committed to Git repositories
- Shared in chat/email/Slack
- Posted publicly anywhere

## ✅ How to Store API Keys Securely

### For Streamlit Cloud (Production)

1. **Go to:** https://share.streamlit.io
2. **Open your app** → Click **⚙️ Settings**
3. **Go to Secrets** tab
4. **Add your key:**

```toml
ANTHROPIC_API_KEY = "sk-ant-api03-..."
```

5. **Click Save**
6. App restarts automatically with the key available

### For Local Development

1. **Create** `.streamlit/secrets.toml` (already gitignored)
2. **Add your key:**

```toml
# .streamlit/secrets.toml
ANTHROPIC_API_KEY = "sk-ant-api03-..."
```

3. **Never commit this file** (it's in `.gitignore`)

### Alternative: Environment Variables

```bash
# In your terminal (temporary, current session only)
export ANTHROPIC_API_KEY="sk-ant-api03-..."

# Then run your app
streamlit run dashboard.py
```

Or add to your shell profile (`~/.zshrc` or `~/.bashrc`):
```bash
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```

## 🔄 How the App Reads the Key

The dashboard automatically checks for the key in this order:

1. **Streamlit Secrets** (`st.secrets.ANTHROPIC_API_KEY`)
2. **Environment Variable** (`os.environ.get("ANTHROPIC_API_KEY")`)
3. **Fallback** to rule-based analysis if not found

## 🚨 If You Accidentally Exposed a Key

### Immediate Actions:

1. **Revoke the key immediately:**
   - Go to https://console.anthropic.com/settings/keys
   - Find the exposed key
   - Click **Delete** or **Revoke**

2. **Generate a new key:**
   - Click **Create Key**
   - Copy the new key
   - Store it securely (see above)

3. **Update your deployments:**
   - **Streamlit Cloud:** Update in Settings → Secrets
   - **Local:** Update `.streamlit/secrets.toml`

### Prevention:

- ✅ Use `.gitignore` (already configured)
- ✅ Use Streamlit Secrets for production
- ✅ Use environment variables for local dev
- ✅ Never paste keys in chat/email
- ✅ Review commits before pushing

## 📁 Files That Are Safe (Gitignored)

These files are **automatically ignored** by Git:

```
.streamlit/secrets.toml  ← API keys go here
.env                     ← Alternative for env vars
tutoring_data.csv        ← Generated data
```

## 📁 Files That Are Public (In Git)

These files are **committed to Git** and public:

```
.streamlit/config.toml   ← UI configuration only (no secrets)
dashboard.py             ← Source code (no hardcoded keys)
requirements.txt         ← Package list
README.md                ← Documentation
```

## ✅ Security Checklist

Before deploying or sharing:

- [ ] No API keys in source code
- [ ] `.streamlit/secrets.toml` is gitignored
- [ ] API key added to Streamlit Cloud Secrets
- [ ] No sensitive data in sample CSV
- [ ] `.gitignore` includes secrets files
- [ ] Reviewed recent commits for exposed keys

## 🔐 Best Practices

### DO:
- ✅ Use Streamlit Secrets for production
- ✅ Use `.streamlit/secrets.toml` for local dev
- ✅ Rotate keys periodically
- ✅ Use different keys for dev/prod
- ✅ Monitor API usage for anomalies

### DON'T:
- ❌ Hardcode keys in source code
- ❌ Commit secrets to Git
- ❌ Share keys via chat/email
- ❌ Use production keys in development
- ❌ Leave keys in public places

## 📊 Monitoring API Usage

Check your Anthropic dashboard regularly:
- https://console.anthropic.com/settings/usage

Watch for:
- Unexpected spikes in usage
- Requests from unknown IPs
- Unusual patterns

## 🆘 Support

If you suspect your key was compromised:
1. **Revoke immediately**
2. **Generate new key**
3. **Contact Anthropic support** if needed
4. **Review recent API usage**

---

## Quick Reference

### Get a New Key
https://console.anthropic.com/settings/keys

### Add to Streamlit Cloud
App Settings → Secrets → Add `ANTHROPIC_API_KEY`

### Add Locally
Create `.streamlit/secrets.toml` with your key

### Check if Working
Dashboard will show AI-generated explanations and recommendations

---

**Remember:** The app works perfectly without an API key using rule-based analysis. AI features are optional but enhance the insights!
