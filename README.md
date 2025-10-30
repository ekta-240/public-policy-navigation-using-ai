# 🔎 Public Policy Navigation System using AI

## Overview
An AI-powered web application for searching and navigating education policies using Natural Language Processing (NLP) and TF-IDF vectorization.

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/ekta-240/public-policy-navigation-using-ai.git
cd public-policy-navigation-using-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
uvicorn app:app --reload --port 5000

# 4. Open in browser
# Visit: http://localhost:5000
```

## Features
- 🔍 **Semantic Search**: Find relevant education policies using natural language queries
- 📊 **TF-IDF Vectorization**: Uses trained model for accurate similarity matching
- 🎨 **Modern UI**: Clean, responsive interface with card-based results
- ⚡ **Fast API**: Built with FastAPI for high performance
- 📈 **Relevance Scoring**: Shows similarity scores for each result

## Technology Stack
- **Backend**: FastAPI
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **ML/NLP**: scikit-learn (TF-IDF Vectorizer)
- **Data Processing**: pandas, numpy
- **Server**: Uvicorn (ASGI server)

## Project Structure
```
public-policy-navigation-using-ai/
├── app.py                      # FastAPI application (main server)
├── templates/
│   └── index.html             # Frontend template with search UI
├── static/                     # Static assets (CSS, JS, images)
├── education_policies.csv      # Full dataset (500 policies)
├── train_policies.csv         # Training data (400 policies)
├── test_policies.csv          # Test data (100 policies)
├── policy_vectorizer.pkl      # Trained TF-IDF vectorizer
├── policy_tfidf_matrix.pkl    # Pre-computed TF-IDF matrix
├── infosys_nlp.ipynb          # Jupyter notebook for model training
├── policy/                     # Additional policy modules
│   ├── main.py                # Standalone FastAPI example
│   ├── code.ipynb             # Experimentation notebook
│   └── *.pkl                  # Additional trained models
└── README.md                   # This file
```

## Installation & Setup

### Prerequisites
- Python 3.8+ (Python 3.13+ recommended)
- pip or conda package manager

### 1. Clone the Repository
```bash
git clone https://github.com/ekta-240/public-policy-navigation-using-ai.git
cd public-policy-navigation-using-ai
```

### 2. Install Dependencies

**Using pip:**
```bash
pip install fastapi uvicorn jinja2 joblib pandas scikit-learn numpy
```

**Using conda:**
```bash
conda install -y fastapi uvicorn jinja2 joblib pandas scikit-learn numpy
```

### 3. Verify Model Files
Ensure these trained model files exist in the root directory:
- `policy_vectorizer.pkl`
- `policy_tfidf_matrix.pkl`

If missing, run `infosys_nlp.ipynb` to generate them.


## Dataset Information

The synthetic education policy dataset includes:
- **500 policies** covering various education sectors
- **Sectors**: Primary, Secondary, Higher Education, Vocational, Early Childhood
- **Regions**: 10 Indian states (Karnataka, Maharashtra, Tamil Nadu, etc.)
- **Years**: 2015-2025
- **Fields**: 
  - Policy ID, Title, Sector, Region, Year
  - Target Group, Status, Funding
  - Stakeholders, Impact Score
  - Summary, Goals, Full Text

## Model Details

- **Algorithm**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Features**: 5000 max features, bigrams (1-2 word combinations)
- **Similarity Metric**: Cosine Similarity
- **Training Data**: 400 policies
- **Test Data**: 100 policies

## API Endpoints

### GET `/`
- Returns the homepage with search interface
- Response: HTML page

### POST `/search`
- Accepts form data with `query` parameter
- Returns search results rendered in HTML
- Parameters:
  - `query` (string): Search query text

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This is an educational project for demonstrating NLP and web application development.

## Author
**Ekta** - [ekta-240](https://github.com/ekta-240)

## Acknowledgments
- Built as part of the Infosys Springboard learning program
- Uses scikit-learn for NLP and machine learning
- FastAPI framework for high-performance web services


<img width="1920" height="1080" alt="Screenshot (2980)" src="https://github.com/user-attachments/assets/adcda552-5f60-437e-aa90-d925c09197e4" />
<img width="1920" height="1080" alt="Screenshot (2982)" src="https://github.com/user-attachments/assets/be199383-aefc-4163-8c8d-d9b732ad641f" />

