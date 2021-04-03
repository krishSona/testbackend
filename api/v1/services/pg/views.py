from rest_framework import views

from rest_framework.exceptions import ValidationError
from core.models import Employee
from django.http.response import JsonResponse


class EmployeeView(views.APIView):

    def patch(self, request, *args, **kwargs):
        employee_rid = request.data.get('employee_rid', None)
        e_nach = request.data.get('e_nach', None)
        if not employee_rid:
            raise ValidationError({"status": "False", "message": "RID required"})
        emp_obj = Employee.objects.filter(rid=employee_rid, deleted_at=None).first()
        if not emp_obj:
            raise ValidationError({
                "status": "False", "message": "Employee Does not Exists"})

        emp_obj.e_nach = e_nach
        emp_obj.save()
        return JsonResponse({"status": "True", "message": "E_nach updated successfully"})
