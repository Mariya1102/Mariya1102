# Bank Transactions Analyzer

A Streamlit application for analyzing bank transactions.

## Deployment Instructions

1. Create a GitHub repository and push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main
```

2. Deploy to Streamlit Cloud:
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Click "New app"
   - Connect your GitHub repository
   - Select the main branch
   - Set the main file path to `app.py`
   - Click "Deploy"

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app locally:
```bash
streamlit run app.py
```

## Project Structure

- `app.py` - Main application file
- `requirements.txt` - Python dependencies
- `.streamlit/config.toml` - Streamlit configuration 