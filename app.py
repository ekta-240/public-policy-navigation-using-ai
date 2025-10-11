from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import textwrap
from sklearn.metrics.pairwise import cosine_similarity

# Load Model and Data
vectorizer = joblib.load("policy_vectorizer.pkl")
data = joblib.load("policy_tfidf_matrix.pkl")
tfidf_matrix = data["matrix"]
df = data["df"]

# FastAPI App Setup
app = FastAPI()
templates = Jinja2Templates(directory="templates")

def search_policies(query: str, top_k: int = 3):
    """Search for top K similar policies based on query"""
    query_vec = vectorizer.transform([query.lower()])
    sims = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_idx = sims.argsort()[::-1][:top_k]
    
    results = []
    for idx in top_idx:
        row = df.iloc[idx]
        results.append({
            "title": row["title"],
            "policy_id": row["policy_id"],
            "region": row["region"],
            "year": row["year"],
            "status": row["status"],
            "summary": textwrap.shorten(row["full_text"], width=250, placeholder="..."),
            "score": round(sims[idx], 3)
        })
    return results

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render homepage"""
    return templates.TemplateResponse("index.html", {"request": request, "results": None})

@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, query: str = Form(...)):
    """Handle search query and return results"""
    results = search_policies(query)
    return templates.TemplateResponse("index.html", {"request": request, "results": results, "query": query})
