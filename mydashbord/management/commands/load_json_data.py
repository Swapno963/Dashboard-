import json
from django.core.management.base import BaseCommand
from mydashbord.models import dashbordModel

class Command(BaseCommand):
    help = 'Loading JSON data into the postql Db'
    prbList = []
    def handle(self, *args, **kwargs):
        with open('data.json',encoding='utf-8') as f:
            data = json.load(f)
            # print(data)
            for index,item in enumerate(data):
                # dashbordModel.objects.create(**item)
                try:
                    intensity=item.get('intensity')
                    relevance=item.get('relevance')
                    likelihood=item.get('likelihood')

                    if intensity == "":
                        intensity = None
                        
                    if relevance == "":
                        relevance = None
                        
                    if likelihood == "":
                        likelihood = None
                    

                    dashbordModel.objects.create(
                         end_year=item.get('end_year', ''),
                        intensity=intensity,
                        sector=item.get('sector', ''),
                        topic=item.get('topic', ''),
                        insight=item.get('insight', ''),
                        url=item.get('url', ''),
                        region=item.get('region', ''),
                        start_year=item.get('start_year', ''),
                        impact=item.get('impact', ''),
                        added=item.get('added', ''),
                        published=item.get('published', ''),
                        country=item.get('country', ''),
                        relevance=relevance,
                        pestle=item.get('pestle', ''),
                        source=item.get('source', ''),
                        title=item.get('title', ''),
                        likelihood=likelihood
                    )
                    print(f"Created {index}")

                except Exception as e:
                    # print(f"problem in,{item}")
                    print(f"Exception is,{index}")
                    self.prbList.append(item)
                    
            with open('data3.json', 'w', encoding='utf-8') as f:
                json.dump(self.prbList, f, ensure_ascii=False, indent=4)
                    
                    
                    
                    
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
