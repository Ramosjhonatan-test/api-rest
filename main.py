from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.post("/convertir")
async def convertir(file: UploadFile = File(...)):
    if not file:
        return JSONResponse(content={"message": "No file uploaded"}, status_code=400)

    # Guarda la imagen en el sistema de archivos
    file_location = f"temp/{file.filename}"  # Asegúrate de crear la carpeta 'temp'
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())
    
    # Aquí debes agregar tu lógica para convertir la imagen en 3D usando Blender
    # Por ahora solo devolveremos un mensaje de éxito
    return JSONResponse(content={"message": "Imagen convertida", "file_location": file_location}, status_code=200)

if __name__ == '__main__':
    import uvicorn
    # Crea la carpeta temp si no existe
    os.makedirs("temp", exist_ok=True)
    uvicorn.run(app, host="0.0.0.0", port=8000)
