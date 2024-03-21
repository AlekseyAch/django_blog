import requests
import os
from bs4 import BeautifulSoup
from django.core.exceptions import ObjectDoesNotExist
from news.models import News, Category
from django.utils.text import slugify
from transliterate import translit
from django.core.files import File
from urllib.parse import urlparse
from datetime import datetime
from django.utils import timezone

def enter_page():
    base_url = 'https://alekseyblog.wordpress.com/'
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Ошибка при загрузке страницы товара {response}: {response.status_code}")
        return None

    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    news = soup.find_all('header', class_="entry-header")

    urls = []
    for article in news:
        h2_tag = article.find("h2")
        url_tag = h2_tag.find("a")
        if url_tag is not None:
            # Извлекаем ссылку из атрибута href
            url = url_tag.get("href")
            urls.append(url)
        else:
            print("Ссылка не найдена")

    return urls


def download_and_save_image(img_url):
    # Извлекаем только путь к файлу из URL
    parsed_url = urlparse(img_url)
    filename = os.path.basename(parsed_url.path)

    # Путь для сохранения изображения на сервере Django
    image_dir = 'news_images/'
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Путь к сохраненному файлу
    image_path = os.path.join(image_dir, filename)

    # Проверяем, существует ли файл с таким именем
    if os.path.exists(image_path):
        print(f"Изображение {filename} уже существует. Пропускаем скачивание.")
        return image_path

    # Скачиваем изображение
    response = requests.get(img_url)
    if response.status_code == 200:
        # Сохраняем изображение
        with open(image_path, 'wb') as f:
            f.write(response.content)

        return image_path

    return None

def book(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    news = soup.find_all('article', class_="post")

    for article in news:
        title = article.find("h2", class_="entry-title").text.strip()
        img_element = article.find("img", class_="wp-post-image")
        img_url = img_element["src"] if img_element else None

        formatted_datetime_str = None  # Устанавливаем значение по умолчанию

        time_element = article.find("time", class_="entry-date published updated")
        if time_element:
            datetime_str = time_element["datetime"]
            datetime_object = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
            formatted_datetime_str = datetime_object.replace(tzinfo=None)

        categories = []
        category_span = article.find("span", class_="cat-links")
        if category_span:
            category_soup = BeautifulSoup(str(category_span), 'lxml')
            for a in category_soup.find_all("a"):
                category_name = a.text.strip()
                category, created = Category.objects.get_or_create(title=category_name)
                categories.append(category)

        content_divs = article.find_all("div", class_="entry-content")
        content = "\n".join(div.text.strip() for div in content_divs)

        title_lower = title.lower()
        slug_title = translit(title_lower, 'bg', reversed=True).replace(' ', '-')
        slug = slugify(slug_title)

        try:
            news = News.objects.get(title=title)
            news.category = category
            news.text_blocks = content

            if img_url:
                image_path = download_and_save_image(img_url)
                if image_path:
                    news.text_img.save(os.path.basename(image_path), File(open(image_path, 'rb')))

            news.slug = slug
            news.date = formatted_datetime_str
            news.excerpt = content
            if formatted_datetime_str is not None:
                news.save()
            else:
                # Если дата не определена, устанавливаем текущее время
                news.date = timezone.now()
                news.save()

            news.tags.clear()
        except ObjectDoesNotExist:
            news_entry = News(title=title, text_blocks=content, excerpt=content, slug=slug)

            if img_url:
                image_path = download_and_save_image(img_url)
                if image_path:
                    news_entry.text_img.save(os.path.basename(image_path), File(open(image_path, 'rb')))

            if categories:
                news_entry.category = categories[0]
            else:
                news_entry.category = None

            if formatted_datetime_str is None:
                news_entry.date = timezone.now()
            else:
                # Если дата не определена, устанавливаем текущее время
                news_entry.date = timezone.now()

            news_entry.save()

urls = enter_page()
for url in urls:
    book(url)
