#
#  Import LIBRARIES
from fastapi import FastAPI, UploadFile

#  Import FILES
#

app: FastAPI = FastAPI()


@app.post(path="/uploadFile/")
async def upload_file(file: UploadFile) -> dict[str, str | None]:
    return {"filename": file.filename}


@app.post(path="/uploadFiles/")
async def upload_files(files: list[UploadFile]) -> dict[str, list[str | None]]:
    return {"filenames": [file.filename for file in files]}
