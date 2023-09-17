import uvicorn

if __name__ =="__main__":
    uvicorn.run("app:app", port=8000, reload=True)

#Run the API with uvicorn ,will run on local host
