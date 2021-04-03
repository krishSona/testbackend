from django.http import JsonResponse
from workers.models import Worker


def registration(request):
    _id = request.GET.get('id')
    token = request.GET.get('token')
    if token is not None:
        worker = Worker.objects.filter(id=_id).first()
        worker.fcm_registration_token = token
        worker.save()
        data = {"status": 200, "message": "OK"}
    else:
        data = {"status": 400, "message": "टोकन पंजीकरण विफल।"}
    return JsonResponse(data)