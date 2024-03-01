from django.core.management.base import BaseCommand, CommandError
from news.import_from_wordpress import import_wordpress_data

class Command(BaseCommand):
    help = 'Импортирует данные из XML-файла WordPress'

    def handle(self, *args, **options):
        file_path = input('Введите путь к файлу WordPress XML: ').strip()  # Удаление лишних пробелов
        try:
            import_wordpress_data(file_path)
            self.stdout.write(self.style.SUCCESS('Успешно импортированы данные из XML-файла WordPress'))
        except Exception as e:
            raise CommandError(f'Не удалось импортировать данные: {e}')
