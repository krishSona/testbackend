from rest_framework import viewsets, permissions
from rest_framework.response import Response

from workers.models import Attendance, Worker


class AttendanceViewSet(viewsets.ModelViewSet):
    swagger_schema = None
    queryset = Attendance.objects.all().order_by('-id')
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        worker_id = request.data.get('workerId')
        _worker = Worker.objects.filter(id=worker_id).first()
        if _worker is not None:
            _balance = _worker.total_salary / 60
            _worker.balance += _balance
            _worker.save()
        punch_at = request.data.get('punch_at')
        attendance = Attendance.objects.create(worker_id=worker_id,punch_at=punch_at)
        if attendance is not None:
            data = {'status': 'success'}
        return Response(data)