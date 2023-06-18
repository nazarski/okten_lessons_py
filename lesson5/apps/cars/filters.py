from django.http import QueryDict
from django.db.models import QuerySet
from .models import CarModel
from rest_framework.serializers import ValidationError


def car_filter_queryset(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    sort_by = query.get('sort_by')
    sort_order = query.get('sort_order')

    query = query.copy()
    query.pop('sort_by', None)
    query.pop('sort_order', None)

    for k, v in query.items():
        match k:

            # year gt/lt
            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)

            # seats gt/lt
            case 'seats_gt':
                qs = qs.filter(seats__gt=v)
            case 'seats_lt':
                qs = qs.filter(seats__lt=v)

            # volume gt/lt
            case 'volume_gt':
                qs = qs.filter(volume__gt=v)
            case 'volume_lt':
                qs = qs.filter(volume__lt=v)

            # brand startswith, endswith, contains
            case 'brand_startswith':
                qs = qs.filter(brand__startswith=v)
            case 'brand_endswith':
                qs = qs.filter(brand__endswith=v)
            case 'brand_contains':
                qs = qs.filter(brand__contains=v)

            # body_type startswith, endswith, contains
            case 'body_type_startswith':
                qs = qs.filter(body_type__startswith=v)
            case 'body_type_endswith':
                qs = qs.filter(body_type__endswith=v)
            case 'body_type_contains':
                qs = qs.filter(body_type__contains=v)

            # auto_park id
            case 'auto_park':
                qs = qs.filter(auto_park_id=v)

            # default
            case _:
                raise ValidationError({'Detail': f'"{k}" is not allowed'})

    if sort_by:
        match sort_order:
            case 'asc':
                qs = qs.order_by(sort_by)
            case 'desc':
                qs = qs.order_by(f'-{sort_by}')
    return qs
