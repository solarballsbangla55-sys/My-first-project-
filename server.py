from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>Server working!</h1>"

@app.post("/upload-video")
async def upload_video(file: UploadFile = File(...)):
    # For now, we only test upload works
    return {"filename": file.filename, "status": "video uploaded successfully"}
    
    

  
