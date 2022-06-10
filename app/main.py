from fastapi import FastAPI,Form
from app.handler import json_input
from starlette.responses import RedirectResponse


app = FastAPI()

@app.get("/")
def raiz():
        return RedirectResponse(url="/docs/")

@app.post("/traer_data/")
async def traer_data(
            fuente: str = Form(), 
            region: str = Form(),
            canal: str = Form(),
            categoria: str = Form(),
            marca: str = Form()):
    
    file_input = './json/json_ejercicio/json_' + region + '_' + canal + '_' + marca + '_' + categoria + '_' + fuente.lower() + '_pronostico.json'
    file_input = file_input.replace('  ', ' ')
    data = json_input(file_input)
    return data

@app.post("/traer_data_opt/")
async def traer_data_opt(
            fuente: str = Form(), 
            region: str = Form(),
            canal: str = Form(),
            categoria: str = Form(),
            marca: str = Form(),
            tipo_meta: str = Form()):

    file_input = "./json/json_ejercicio/opt/json_" + region + '_' + canal + '_' + marca + '_' + categoria + '_' + tipo_meta + '_' + fuente.lower() + '_optimizacion_tem.json'        
    data = json_input(file_input)
    return data
