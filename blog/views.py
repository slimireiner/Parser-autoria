from django.shortcuts import render

from .models import *


def index(request):
    cars = Car.objects.all()

    if request.GET.get('kuzov', None) and request.GET.get('kuzov', None) != 'all':
        cars = cars.filter(body_type=request.GET.get('kuzov'))

    if request.GET.get('year', None) and request.GET.get('year', None) != 'all':
        cars = cars.filter(year__gte=request.GET.get('year'))

    if request.GET.get('usd', None) and request.GET.get('usd', None) != 'all':
        cars = cars.filter(current_usd__gte=request.GET.get('usd'))

    if request.GET.get('year_do', None) and request.GET.get('year_do', None) != 'all':
        cars = cars.filter(year__lte=request.GET.get('year_do'))

    if request.GET.get('usd_do', None) and request.GET.get('usd_do', None) != 'all':
        cars = cars.filter(current_usd__lte=request.GET.get('usd_do'))

    if request.GET.get('race', None) and request.GET.get('race', None) != 'all':
        cars = cars.filter(race__gte=request.GET.get('race'))

    if request.GET.get('race_do', None) and request.GET.get('race_do', None) != 'all':
        cars = cars.filter(race__lte=request.GET.get('race_do', None))

    if request.GET.get('fuel', None) and request.GET.get('fuel', None) != 'all':
        cars = cars.filter(type_fuel=request.GET.get('fuel'))

    if request.GET.get('privod', None) and request.GET.get('privod', None) != 'all':
        cars = cars.filter(drive_unit=request.GET.get('privod'))

    if request.GET.get('transmission', None) and request.GET.get('transmission', None) != 'all':
        cars = cars.filter(type_of_drive=request.GET.get('transmission'))

    if request.GET.get('city', None) and request.GET.get('city', None) != 'all':
        cars = cars.filter(city=request.GET.get('city'))

    kuzova = []
    years = []
    usds = []
    usd_dos = []
    year_dos = []
    races = []
    race_dos = []
    fuels = []
    privods = []
    transmissions = []
    citys = []

    for car in Car.objects.all():
        if car.body_type not in kuzova:
            kuzova.append(
                car.body_type
            )
        if car.year not in years:
            years.append(
                car.year
            )
        if car.current_usd not in usds:
            usds.append(
                car.current_usd
            )
        if car.current_usd not in usd_dos:
            usd_dos.append(
                car.current_usd
            )
        if car.year not in year_dos:
            year_dos.append(
                car.year
            )
        if car.race not in races:
            races.append(
                car.race
            )
        if car.race not in race_dos:
            race_dos.append(
                car.race
            )
        if car.type_fuel not in fuels:
            fuels.append(
                car.type_fuel
            )
        if car.drive_unit not in privods:
            privods.append(
                car.drive_unit
            )
        if car.type_of_drive not in transmissions:
            transmissions.append(
                car.type_of_drive
            )
        if car.city not in citys:
            citys.append(
                car.city
            )

    kuzova = sorted(kuzova)
    years = sorted(years)
    usds = sorted(usds)
    usd_dos = sorted(usd_dos)
    races = sorted(races)
    race_dos = sorted(race_dos)
    year_dos = sorted(year_dos)
    fuels = sorted(fuels)
    privods = sorted(privods)
    transmissions = sorted(transmissions)
    citys = sorted(citys)

    return render(request, 'blog/index.html',
                  context={'cars': cars, 'kuzova': kuzova, 'years': years, 'usds': usds, 'usd_dos': usd_dos,
                           'year_dos': year_dos, 'races': races, 'race_dos': race_dos, 'fuels': fuels,
                           'privods': privods,
                           'transmissions': transmissions, 'citys': citys})

# r = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
