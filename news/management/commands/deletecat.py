from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Удаление постов в категории'
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument('name_of_category', type=str)
    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["name_of_category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name_of_category=options['name_of_category'])
            Post.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category.name_of_category}')) # в случае неправильного подтверждения говорим, что в доступе отказано
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR('Could not find this category '))