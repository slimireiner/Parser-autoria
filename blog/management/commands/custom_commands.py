from django.core.management.base import BaseCommand
import requests

from blog.models import Car, Try


class Command(BaseCommand):
    help = 'Парсинг авториа'

    def handle(self, *args, **options):
        a = 0

        def get_html():
            response = requests.get(
                f"https://auto.ria.com/api/search/auto?indexName=auto%2Corder_auto%2Cnewauto_search&technicalCondition=1&category_id=1&originExclude=1&brandOrigin%5B%5D=158&brandOrigin%5B%5D=643&brandOrigin%5B%5D=804&abroad=2&custom=1&damage=1&auto_repairs=2&page={a}&countpage=20&with_feedback_form=1&with_last_id=1")
            try:
                b = response.json()
            except:
                return False
            return b

        def get_content():
            global link_page, item
            car_ids = get_html()['result']['search_result']['ids']
            for card_id in car_ids:
                link = 'https://auto.ria.com/demo/bu/searchPage/v2/view/auto/2746/274622/' + card_id + '?lang_id=2'
                link_page = f'https://auto.ria.com/auto_gabela_{card_id}.html'

                try:
                    item = requests.get(link).json()
                except:
                    continue
                try:
                    car = Car(
                        id=item['autoData']['autoId'],
                        title=item['title'],
                        current_usd=item['USD'],
                        current_eur=item['EUR'],
                        current_grn=item['UAH'],
                        city=item['locationCityName'],
                        link=link_page,
                        race=int(item['autoData']['race'].split(' ')[0]),
                        year=item['autoData']['year'],
                        type_fuel=item['autoData']['fuelName'],
                        type_of_drive=item['autoData']['gearboxName'],
                        body_type=item['autoData']['subCategoryNameEng'],
                        drive_unit=item['autoData']['driveName']

                    ).save()
                except:
                    car = Car.objects.get(id=item['autoData']['autoId'])
                    car.title = item['title']
                    car.current_usd = item['USD']
                    car.current_eur = item['EUR']
                    car.current_grn = item['UAH']
                    car.city = item['locationCityName']
                    car.link = link_page
                    car.race = int(item['autoData']['race'].split(' ')[0])
                    car.year = item['autoData']['year']
                    car.type_fuel = item['autoData']['fuelName']
                    car.type_of_drive = item['autoData']['gearboxName']
                    car.body_type = item['autoData']['subCategoryNameEng']
                    car.drive_unit = item['autoData']['driveName']
                    continue

            return True if len(car_ids) else False

        result = True
        while result:
            try:
                print(f'{a = }')
                result = get_content()
                a += 1
            except:
                print('Ошибка')