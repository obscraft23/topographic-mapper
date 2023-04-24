import io
import base64

from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse,JSONResponse
from starlette.middleware.cors import CORSMiddleware
import altmap
import time

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   
    allow_methods=["*"],      
    allow_headers=["*"]
)


@app.get("/api/mapper", response_class=JSONResponse)
def mapper(lat0: float, lat1: float, lon0: float, lon1: float, magnetic_north_line: bool):
    #stime = time.time()
    fig = altmap.createTopographic(lat0, lon0, lat1, lon1, magnetic_north_line, max_length=4000)
    if fig == None:
        return JSONResponse({"datab64":"too large"})
    png_output = io.BytesIO()
    fig.savefig(png_output, format='png')
    png_data = png_output.getvalue()
    base64_data = base64.b64encode(png_data).decode()

    #print(time.time() - stime)
    return JSONResponse(content={"datab64" :base64_data})

@app.get("/healthz")
def health_check():
    return Response(content="OK\n")
