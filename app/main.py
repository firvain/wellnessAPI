from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.user_routes import router as user_router
from app.routes.auth_routes import router as auth_router
# Define the list of origins allowed to make cross-origin requests
origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://project-wellness.ece.uowm.gr",
]

app = FastAPI(root_path="/wellness-api")

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
