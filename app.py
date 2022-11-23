from fastapi import FastAPI, File, UploadFile
import uvicorn
import time
import numpy as np
import pandas as pd

from users import user
from scan import scan

app = FastAPI()

the_list = user.from_file('users.csv')
the_scans = scan.from_file('scans.csv')

@app.get('/users')
def get_users():
    return str(*the_list)

@app.post('/users')
def add_user(nome: str, prenom:str, poids:float, taille:int):
    u = user(nome, prenom, poids, taille)
    the_list.append(u)
    return f"{{ 'id': {u.id} }}"

@app.delete('/users/{id}')
def delete_user(id: int):
    for u in the_list:
        if u.id == id:
            the_list.remove(u)
            return " { success: true } "
    return " { success: false } "

@app.put('/save')
def save():
    # save users
    df = pd.DataFrame([u.__dict__ for u in the_list])
    df.to_csv('users.csv', index=False)
    # save scans
    df = pd.DataFrame([s.__dict__ for s in the_scans])
    df.to_csv('scans.csv', index=False)
    return " { success: true } "


@app.get('/scans')
def get_scans():
    return str(*the_scans)

@app.get('/upload_scans')
def upload_scan():
    # serve the upload page
    with open('./assets/upload_scans.html', 'r') as f:
        # send the html file
        return bytes(f.read().encode('utf-8'))

@app.post('/upload_scans')
def upload_scans(id:int,nature:str,file: UploadFile):
    print(file)
    # save the file
    with open(f'./uploaded_files/{file.filename}', 'wb') as f:
        f.write(file.file.read())
    # create a scan object
    s = scan(id, nature, f'./uploaded_files/{file.filename}')
    the_scans.append(s)
    return {"filename": file.filename}


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
