# Mars Rover “Curiosity” photos
import requests
import os

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
photos = data.get('photos', [])

if photos:
    if not os.path.exists('mars_photos'):
        os.makedirs('mars_photos')

    for idx, photo in enumerate(photos):

        img_url = photo['img_src']
        img_name = f'mars_photos/mars_photo{idx + 1}.jpg'

        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            with open(img_name, 'wb') as f:
                f.write(img_response.content)
            print(f"Photos are saved as: {img_name}")
        else:
            print(f"Impossible to download the photo {img_url}")
    else:
        print("There are no photos for these parameters.")
else:
    print(f"Status error: {response.status_code}")

# POST/GET/DELETE
import requests

def upload_image(image_path):
    url = 'http://127.0.0.1:8080/upload'
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        response = requests.post(url, files=files)
        if response.status_code == 201:
            image_url = response.json()['image_url']
            return image_url

def get_image_url(filename):
    url = f'http://127.0.0.1:8080/image/{filename}'
    response = requests.get(url, headers={'Content-Type': 'text'})
    if response.status_code == 200:
        print(response.json()['image_url'])

def delete_image(filename):
    url = f'http://127.0.0.1:8080/delete/{filename}'
    response = requests.delete(url)
    if response.status_code == 200:
        print(response.json()['image_url'])


if __name__ == '__main__':
    image_url = upload_image('path_to_your_image.jpg')
    get_image_url('example.jpg')
    delete_image('example.jpg')

