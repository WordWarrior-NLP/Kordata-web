from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
# from routers import news

#  RUN ::
#  uvicorn main:app --reload

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",    # 또는 "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"message": "Let's start!"}


# app.include_router(news.router)


