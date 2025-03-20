import requests
import os

# API URL для отримання фотографій ровера Curiosity
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,  # Марсіанський день місії
    'camera': 'fhaz',  # Камера фронтального хазардного уникнення
    'api_key': 'DEMO_KEY'  # API-ключ (можна замінити на власний)
}

# Виконуємо GET-запит до API
response = requests.get(url, params=params)

# Перевіряємо статус-код відповіді
if response.status_code == 200:
    data = response.json()  # Перетворюємо відповідь у JSON
    photos = data.get('photos', [])  # Отримуємо список фото

    if photos:
        # Створюємо папку для збереження, якщо її немає
        os.makedirs("mars_photos", exist_ok=True)

        # Завантажуємо перші дві фотографії
        for i, photo in enumerate(photos[:2], start=1):
            img_url = photo['img_src']
            img_data = requests.get(img_url).content  # Завантажуємо фото

            # Створюємо шлях до файлу
            file_name = f"mars_photos/mars_photo{i}.jpg"
            with open(file_name, 'wb') as file:
                file.write(img_data)

            print(f"Збережено: {file_name}")

    else:
        print("Фото не знайдено за вказаними параметрами.")
else:
    print(f"Помилка запиту: {response.status_code}")


# Базова URL-адреса сервера
BASE_URL = "http://127.0.0.1:8080"

# Файл, який будемо завантажувати
IMAGE_PATH = "mars_photos/mars_photo1.jpg"

# 1️⃣ Завантаження зображення
upload_url = f"{BASE_URL}/upload"
files = {"image": open(IMAGE_PATH, "rb")}

response = requests.post(upload_url, files=files)
if response.status_code == 201:
    image_url = response.json().get("image_url")
    print(f"✅ Зображення успішно завантажено: {image_url}")
else:
    print(f"❌ Помилка при завантаженні: {response.text}")
    exit()

# 2️⃣ Отримання посилання на завантажене зображення
filename = image_url.split("/")[-1]  # Отримуємо ім'я файлу
get_url = f"{BASE_URL}/image/{filename}"

headers_text = {"Content-Type": "text"}
response_text = requests.get(get_url, headers=headers_text)
if response_text.status_code == 200:
    print(f"🔗 Отримано URL зображення: {response_text.json().get('image_url')}")
else:
    print(f"❌ Помилка при отриманні URL: {response_text.text}")

# 3️⃣ Видалення зображення
delete_url = f"{BASE_URL}/delete/{filename}"
response_delete = requests.delete(delete_url)

if response_delete.status_code == 200:
    print(f"🗑 Зображення {filename} видалено успішно.")
else:
    print(f"❌ Помилка при видаленні: {response_delete.text}")
