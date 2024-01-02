from fastapi import FastAPI
from routes.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
