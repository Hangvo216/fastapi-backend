from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://nextjs-frontend.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/image')
def get_image():
    image_url = 'https://i.imgur.com/TNzYa7Q.jpg'  # Replace with your own image URL
    return {'url': image_url}