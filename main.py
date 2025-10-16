#
#  Import LIBRARIES
import os

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


@app.post(path="/uploadFileSave/")
async def upload_file_save(file: UploadFile) -> dict[str, str]:
    upload_directory: str = "./uploads"
    file_location: str = f"./{upload_directory}/{file.filename}"

    os.makedirs(name=upload_directory, exist_ok=True)

    with open(file=file_location, mode="wb") as buffer:
        buffer.write(await file.read())

    return {"message": f"{file.filename} saved at {file_location}"}
