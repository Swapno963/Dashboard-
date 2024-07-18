import json
from django.core.management.base import BaseCommand
from mydashbord.models import dashbordModel

class Command(BaseCommand):
    help = 'Loading JSON data into the postql Db'

    def handle(self, *args, **kwargs):
        with open('data.json',encoding='utf-8') as f:
            data = json.load(f)
            print(data)
            # for item in data:
            #     print(item)
                # dashbordModel.objects.create(**item)
        # self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
