#
#  Import LIBRARIES
from fastapi import FastAPI, UploadFile

#  Import FILES
#

app: FastAPI = FastAPI()


@app.post(path="/uploadFile/")
async def upload_file(file: UploadFile) -> dict[str, str | None]:
    return {"filename": file.filename}
