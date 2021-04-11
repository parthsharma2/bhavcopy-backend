import redis
from django.http import JsonResponse, HttpResponseNotAllowed
from django.conf import settings


def get_equity(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    redis_instance = redis.StrictRedis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
    )

    response_data = []
    q = request.GET.get('q', '').upper()

    for key in redis_instance.keys(f'*{q}*'):
        value = redis_instance.hgetall(key)

        # redis returns values as byte strings that need to
        # be decoded into a unicode string to return as a response
        response_data.append(
            {k.decode(): v.decode() for k, v in value.items()}
        )

    return JsonResponse(response_data, safe=False)
