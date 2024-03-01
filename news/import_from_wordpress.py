import xml.etree.ElementTree as ET
from .models import News, Category, Tag
from django.utils.text import slugify
from transliterate import translit

def import_wordpress_data(file_path):
    print(f"Importing data from WordPress XML file: {file_path}")

    tree = ET.parse(file_path)
    root = tree.getroot()

    total_imported = 0

    for item in root.findall('.//item'):
        title = item.find('title').text
        category_title = item.find('category').text
        tags = [tag.text for tag in item.findall('.//category[@domain="post_tag"]') if tag.text]
        content = item.find('.//{http://purl.org/rss/1.0/modules/content/}encoded').text

        # Преобразуем заголовок к нижнему регистру
        title_lower = title.lower()
        # Транслитерация в латиницу без пробелов
        slug_title = translit(title_lower, 'bg', reversed=True).replace(' ', '-')
        # Генерация slug
        slug = slugify(slug_title)

        print(f"Импортируется этот пост: {title}")

        category, _ = Category.objects.get_or_create(title=category_title)

        # Пытаемся найти существующую запись по заголовку
        try:
            news = News.objects.get(title=title)
            # Обновляем данные существующей записи
            news.category = category
            news.text_blocks = content
            news.slug = slug  # Обновляем slug
            news.save()
            # Обновляем теги
            news.tags.clear()

            for tag_title in tags:
                tag, _ = Tag.objects.get_or_create(title=tag_title)
                news.tags.add(tag)
        except News.DoesNotExist:
            # Создаем новую запись
            news = News(title=title, category=category, text_blocks=content, slug=slug)
            news.save()

            # Добавляем теги
            for tag_title in tags:
                tag, _ = Tag.objects.get_or_create(title=tag_title)
                news.tags.add(tag)

        total_imported += 1

    print(f"Data imported successfully. Total imported: {total_imported}")
