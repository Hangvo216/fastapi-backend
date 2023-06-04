from fastapi import FastAPI

app = FastAPI()

@app.get('/image')
def get_image():
    image_url = 'https://example.com/path/to/image.jpg'  # Replace with your own image URL
    return {'url': image_url}