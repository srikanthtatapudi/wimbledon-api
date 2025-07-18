# \# Wimbledon API 🎾

# 

# This is a small FastAPI project that provides information about Wimbledon men's singles finals for selected years.

# 

# ---

# 

# \## 📌 Features

# ✅ GET endpoint `/wimbledon` with a `year` query parameter  

# ✅ Validates the year (must be >= 1877)  

# ✅ Returns structured JSON response with:

# \- `champion`

# \- `runner\_up`

# \- `score`

# \- `sets`

# \- `tiebreak` indicator  

# ✅ Proper `404` error if year not found  

# ✅ Fully typed with Pydantic models  

# ✅ Automatic Swagger documentation at `/docs`

# 

# ---

# 

# \## 🚀 How to run locally

# 

# ```bash

# git clone https://github.com/srikanthtatapudi/wimbledon-api.git

# cd wimbledon-api

# python -m venv venv

# venv\\Scripts\\activate

# pip install -r requirements.txt

# uvicorn main:app --reload

# Then open http://127.0.0.1:8000/docs in your browser to use the Swagger UI.

# 

# 🔍 Example usage

# sql

# Copy

# Edit

# GET /wimbledon?year=2021

# Returns:

# 

# json

# Copy

# Edit

# {

# &nbsp; "year": 2021,

# &nbsp; "champion": "Novak Djokovic",

# &nbsp; "runner\_up": "Matteo Berrettini",

# &nbsp; "score": "6–7(4–7), 6–4, 6–4, 6–3",

# &nbsp; "sets": 4,

# &nbsp; "tiebreak": true

# }

# ---

# 

# \## ✍️ Author

# \- \*\*Tatapudi Srikanth\*\*

# \- 📧 Email: tatapudisrikanth2004@gmail.com

# \- 📞 Phone: +91 9705848078

# \- 🔗 \[LinkedIn](https://www.linkedin.com/in/srikanth-tatapudi-294a83262/)

# \- 💻 \[GitHub](https://github.com/srikanthtatapudi)





