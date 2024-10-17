from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "¡Hola, mundo! Este es un servidor FastAPI."}

@app.get("/convert")
async def convert_image():
    return {"message": "Aquí es donde convertirías tu imagen a 3D."}
