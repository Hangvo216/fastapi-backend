from fastapi import FastAPI

app = FastAPI()

@app.get('/image')
def get_image():
    image_url = 'https://i.imgur.com/TNzYa7Q.jpg'  # Replace with your own image URL
    return {'url': image_url}