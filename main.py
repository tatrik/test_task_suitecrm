import uvicorn
import os
from fastapi import FastAPI

from app.api import router


app = FastAPI(title="suitecrm")
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=8000,
        host=os.environ["SERVER_HOST"],
        reload=True,
    )
