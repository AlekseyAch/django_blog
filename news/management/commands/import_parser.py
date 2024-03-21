from django.core.management.base import BaseCommand, CommandError
from news.parser import enter_page

class Command(BaseCommand):
    help = 'Импортирует данные из другого сайта в новости!'

    def handle(self, *args, **options):
        try:
            enter_page()
            self.stdout.write(self.style.SUCCESS('Успешно импортированы данные из другого сайта'))
        except Exception as e:
            raise CommandError(f'Не удалось импортировать данные: {e}')
