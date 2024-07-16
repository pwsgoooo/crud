from fastapi import FastAPI,Depends
from fastapi.responses import HTMLResponse,RedirectResponse
from sqlalchemy.orm import Session
from typing import Any,List
from fastapi.templating import Jinja2Templates
from fastapi import Request
import json
from db.models.conn import CURSOR,SESSON,create_tables #,start_ctable
from db.models.members import Members


app = FastAPI(debug=True)

def get_db():
    db = SESSON
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup_event():
    # start_ctable()
    create_tables()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "World"})




@app.get("/write_board",response_class=HTMLResponse)
async def write_board(request: Request):
    return templates.TemplateResponse("write_board.html",{"request":request})

# @app.get('/board') #,response_model=list[Members]
# async def get_board(db:Session = Depends(get_db))->List:
#     CURSOR.execute('select * from board.members')
#     lists = CURSOR.fetchall()
#     if len(lists) >= 0:
#         print("table not exist content ")

# @app.get('/board/{id}',response_model=list[Members])
# async def get_board(id:str, db:Session = Depends(get_db)):
#     listonlyuser = db.query(Members).filter(db.id == id)
#     return listonlyuser
