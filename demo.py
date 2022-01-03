import uvicorn
import os

os.environ["MODIN_ENGINE"] = "ray" 

import modin.pandas as pd
import numpy as np

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():

    frame_data = np.random.randint(0, 100, size=(2**10, 2**8))
    df = pd.DataFrame(frame_data)
    return {"Hello": df}

if __name__ == "__main__":

    uvicorn.run("demo:app", host='0.0.0.0')