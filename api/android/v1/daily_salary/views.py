import json

from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from api.android.v1.daily_salary.serializers import WorkerSerializer
from workers.models import Worker, Advance


# def session(request):
#     phone_number = request.GET.get('phone_number')
#     if phone_number is not None:
#         _worker = Worker.objects.filter(phone=phone_number).first()
#         data = {"status": 200, "id": _worker.id}
#     else:
#         data = {"status": 400, "message": "आपका खाता पंजीकृत नहीं है। कृपया अपने ठेकेदार से संपर्क करें।"}
#     return JsonResponse(data)


# def worker(request):
#     worker_id = request.GET.get('worker_id')
#     if worker_id is not None:
#         _worker = Worker.objects.filter(id=worker_id).first()
#         data = {"balance": "₹" + str(_worker.balance)}
#     else:
#         data = {"status": 400, "message": "आपका खाता पंजीकृत नहीं है। कृपया अपने ठेकेदार से संपर्क करें।"}
#     return JsonResponse(data)


def transfer_to_bank(request):
    worker_id = request.GET.get('worker_id')
    if worker_id is not None:
        _worker = Worker.objects.filter(id=worker_id).first()
        _balance = _worker.balance
        _worker.balance = 0
        _worker.save()
        _advance = Advance.objects.create(worker_id=_worker.id, account_id=_worker.account_id, amount=_balance,
                                          utr="AXPS7170EHAG23G")
        data = {"Bank Name:": _advance.account.ifscode.bank.name, "Bank A/C:": _advance.account.number,
                "IFSC:": _advance.account.ifscode.code, "Deposited:": _advance.amount, "Txn. No.:": _advance.utr}
    else:
        data = {"status": 400, "message": "आपका खाता पंजीकृत नहीं है। कृपया अपने ठेकेदार से संपर्क करें।"}
    return JsonResponse(data)


class WorkerViewSet(viewsets.ModelViewSet):
    swagger_schema = None
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Worker.objects.all().order_by('-id')
    serializer_class = WorkerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Worker.objects.all().order_by('-id')
        phone = self.request.query_params.get('phoneNumber', None)
        if phone is not None:
            queryset = queryset.filter(phone=phone)
        return queryset


class AdvanceViewSet(viewsets.ModelViewSet):
    swagger_schema = None
    queryset = Advance.objects.all().order_by('-id')
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        worker_id = request.data.get('workerId')
        _advance = Advance()
        # if worker_id is not None:
        _worker = Worker.objects.filter(id=worker_id).first()
        if _worker is not None:
            _balance = _worker.balance
            _worker.balance = 0
            _worker.save()
            _advance = Advance.objects.create(worker_id=_worker.id, account_id=_worker.account_id, amount=_balance,
                                              utr="AXPS7170EHAG23G")
            data = {'Bank Name: ': _advance.bank_name, 'Bank A/C: ': _advance.account_number, 'Deposited: ': _advance.amount, 'IFSC: ': _advance.ifsc, 'Txn. No.: ': _advance.utr}
        return Response(data)
