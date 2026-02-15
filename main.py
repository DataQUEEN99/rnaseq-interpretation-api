from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RNA-seq Interpretation API is running 🚀"}
