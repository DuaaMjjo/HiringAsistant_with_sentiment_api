import uvicorn

if __name__ =="__main__":
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    uvicorn.run("app:app",host="0.0.0.0", port=10000, reload=True)

