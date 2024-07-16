from fastapi.responses import HTMLResponse#,RedirectResponse
from . import app

@app.get("/html_page", response_class=HTMLResponse) 
async def html_page():
  html_content = """
  <html lang="ko">
    <head>
      <title>crud board_home</title>
    </head>
    <body>
      <h1>Wellcome! crud home</h1>
      <button onclick="location.href='#">to board</button>
      <script src="#"></script>
    </body>
  </html>

  """ 
  
  return html_content
