from fastapi import FastAPI,Depends
from fastapi.responses import HTMLResponse,RedirectResponse
from sqlalchemy.orm import Session
from typing import Any,List
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


@app.get('/',response_class=HTMLResponse)
async def get_root() -> HTMLResponse:
    return RedirectResponse(url="/html_page") # return RedirectResponse(url='../client/home.html')




@app.get('/board') #,response_model=list[Members]
async def get_board(db:Session = Depends(get_db))->List:
    CURSOR.execute('select * from board.members')
    lists = CURSOR.fetchall()
    # lists = db.query(Members).all()
    if len(lists) >= 0:
        print("table not exist content ")

# @app.get('/board/{id}',response_model=list[Members])
# async def get_board(id:str, db:Session = Depends(get_db)):
#     listonlyuser = db.query(Members).filter(db.id == id)
#     return listonlyuser
