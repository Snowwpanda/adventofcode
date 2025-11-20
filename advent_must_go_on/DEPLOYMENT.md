# Deployment Guide

## Option 1: Run Locally (Easiest)

Perfect for testing or competing with friends on the same network.

1. **Install Python** (3.8 or higher)

2. **Install dependencies:**
   ```bash
   cd advent_must_go_on
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

4. **Access:** Open browser to `http://localhost:8501`

## Option 2: Share on Local Network

Allow friends on the same WiFi/network to access your app.

1. **Find your local IP:**
   
   **Windows:**
   ```bash
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., 192.168.1.100)
   
   **Mac/Linux:**
   ```bash
   ifconfig
   ```

2. **Run with network access:**
   ```bash
   streamlit run app.py --server.address 0.0.0.0 --server.port 8501
   ```

3. **Share with friends:**
   - Give them your IP: `http://192.168.1.100:8501`
   - They must be on the same network

## Option 3: Deploy to Streamlit Cloud (Free)

Host publicly on the internet for free!

### Prerequisites
- GitHub account
- Your code pushed to a GitHub repository

### Steps

1. **Push code to GitHub:**
   ```bash
   cd advent_must_go_on
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/advent-must-go-on.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository
   - Set main file: `app.py`
   - Click "Deploy"

3. **Share your URL:**
   - You'll get a URL like: `https://yourapp.streamlit.app`
   - Share with anyone!

### Notes for Streamlit Cloud
- Free tier: 1 app, limited resources
- Automatic updates when you push to GitHub
- Data persists using JSON files
- Public by default (anyone can access)

## Option 4: Deploy to Heroku

More control and custom domain options.

1. **Install Heroku CLI:**
   - Download from [heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

2. **Create Procfile:**
   ```bash
   echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile
   ```

3. **Create runtime.txt:**
   ```bash
   echo "python-3.11.0" > runtime.txt
   ```

4. **Deploy:**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   heroku open
   ```

## Option 5: Deploy with Docker

Portable and works anywhere Docker runs.

1. **Create Dockerfile:**
   ```dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build image:**
   ```bash
   docker build -t advent-must-go-on .
   ```

3. **Run container:**
   ```bash
   docker run -p 8501:8501 advent-must-go-on
   ```

4. **Access:** `http://localhost:8501`

### Deploy Docker to Cloud

**AWS ECS, Google Cloud Run, Azure Container Instances:**
- Push image to container registry
- Deploy to cloud container service
- Configure domain and SSL

## Data Persistence

### Local/Network Deployment
- Data stored in `data/` folder
- Automatically persists across restarts
- Backup `data/` folder regularly

### Streamlit Cloud
- Uses GitHub for storage
- Data persists in `data/` folder
- Changes saved to JSON files
- Consider GitHub for backups

### Database Option (Advanced)

For many users or better reliability, use a database:

1. **Replace JSON with SQLite:**
   ```python
   # In scoring.py, replace JSON with SQLite
   import sqlite3
   ```

2. **Or use PostgreSQL/MySQL:**
   - Better for 100+ concurrent users
   - More setup required
   - Deploy database separately

## Security Considerations

### Public Deployment
- No authentication by default
- Anyone can submit as any username
- Consider adding login system
- Use Streamlit's authentication options

### Add Basic Authentication

Install streamlit-authenticator:
```bash
pip install streamlit-authenticator
```

Update app.py:
```python
import streamlit_authenticator as stauth

# Add authentication config
# See: https://github.com/mkhorasani/Streamlit-Authenticator
```

### Rate Limiting

Add to prevent spam:
```python
import time
from functools import lru_cache

# Add rate limiting logic
```

## Performance Optimization

### For Many Users

1. **Use caching:**
   - Already implemented with `@st.cache_resource`
   - Prevents reloading problems on every interaction

2. **Optimize problem loading:**
   - Load problems once at startup
   - Cache solutions

3. **Database for scores:**
   - SQLite for <100 users
   - PostgreSQL for 100+ users

### For Large Problems

1. **Limit input size:**
   ```python
   max_input_size = 10000  # characters
   ```

2. **Add timeout:**
   ```python
   import signal
   # Add execution timeout
   ```

## Monitoring

### View Logs

**Streamlit Cloud:**
- Check "Logs" tab in dashboard

**Heroku:**
```bash
heroku logs --tail
```

**Docker:**
```bash
docker logs container_id
```

### Analytics

Add Google Analytics or similar:
```python
# In app.py
import streamlit.components.v1 as components

components.html("""
<!-- Google Analytics code -->
""")
```

## Backup Strategy

### Automatic Backups

**Option 1: Git commits**
```bash
# Cron job to backup data
0 0 * * * cd /path/to/app && git add data/ && git commit -m "Daily backup" && git push
```

**Option 2: Cloud storage**
```python
# Backup to S3/Google Cloud Storage
import boto3
# Upload data/ folder
```

## Troubleshooting

### App Won't Start
- Check Python version (3.8+)
- Verify requirements installed: `pip list`
- Check for syntax errors: `python -m py_compile app.py`

### Can't Access from Network
- Check firewall settings
- Ensure using `0.0.0.0` as address
- Verify IP address is correct

### Scores Not Saving
- Check `data/` folder exists
- Verify write permissions
- Look for errors in console

### Slow Performance
- Too many problems? Optimize loading
- Too many users? Consider database
- Check server resources

## Cost Estimates

### Free Options
- **Streamlit Cloud:** Free (1 app)
- **Local:** $0 (your hardware)
- **Heroku:** $0 (limited hours)

### Paid Options
- **Heroku Hobby:** $7/month
- **AWS ECS:** ~$10-30/month
- **Digital Ocean:** $5-10/month
- **Custom Domain:** ~$10/year

## Next Steps

1. Choose deployment method based on your needs
2. Test thoroughly before sharing
3. Set up backups
4. Monitor performance
5. Share with friends and enjoy! 🎉

## Support

For issues or questions:
- Check README.md
- Review problem validation
- Test locally first
- Check Streamlit docs: https://docs.streamlit.io
