from fastapi import FastAPI,Depends,Form,HTTPException,Request
from fastapi.responses import HTMLResponse,RedirectResponse
from sqlalchemy.orm import Session
from typing import Any,List
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
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


@app.get("/board",response_class=HTMLResponse)
async def get_board(request: Request, db:Session=Depends(get_db)):
    boards = db.query(Members).all()
    return templates.TemplateResponse("board.html",{"request":request, "boards":boards})

class AddMembers(BaseModel):
    id : str
    name: str
    content: str

@app.post("/board",response_class=HTMLResponse)
async def write_board(request: Request, id:str = Form(...),name:str=Form(...),content:str=Form(...),db:Session=Depends(get_db)):
    new_data = AddMembers(id=id, name=name, content=content)
    new_row = Members(id=new_data.id, name= new_data.name, content=new_data.content)
    db.add(new_row)
    db.commit()
    db.refresh(new_row)    
    boards = db.query(Members).all()
    return templates.TemplateResponse("board.html",{"request":request, "boards":boards})


@app.get("/board/edit/{row_id}")
async def edit_data_view(row_id:str, request: Request, db:Session=Depends(get_db)):
    edit_row = db.query(Members).filter(Members.id==row_id).first()
    boards = db.query(Members).all()
    if edit_row:
        return templates.TemplateResponse("board_edit.html",{"request":request, "edit_row":edit_row,"boards":boards})
    else:
        raise HTTPException(status_code=404,detail="editing row enable")


class EditMember(BaseModel):
    name: str
    content: str

@app.put("/board/edit/{row_id}")
async def edit_complete_view(request: Request,row_id:str,edit:EditMember, db:Session=Depends(get_db)):
    edit_row= db.query(Members).filter(Members.id==row_id).first()
    if edit_row:
        # db.delete(edit_row)
        edit_row.name = edit.name
        edit_row.content = edit.content
        db.commit()
        db.refresh(edit_row)

        boards = db.query(Members).all()
        return templates.TemplateResponse("board.html",{"request":request,"boards":boards})
    else:
        raise HTTPException(status_code=404,detail="not not")

    

@app.post("/board/delete/{row_id}")
async def delete_data(row_id:str, db:Session=Depends(get_db)):
    delete_row = db.query(Members).filter(Members.id==row_id).first()
    if delete_row:
        db.delete(delete_row)
        db.commit()
    else:
        raise HTTPException(status_code=404,detail="not not")
    
    return HTMLResponse(status_code=302, headers={"Location":"/board"})