from django.db import models
from authentication.models import User


class Bank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ifscode(models.Model):
    code = models.CharField(max_length=11)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)

    def __str__(self):
        return self.code


class Account(models.Model):
    number = models.CharField(max_length=18)
    ifscode = models.ForeignKey(Ifscode, on_delete=models.PROTECT)
    is_verified = models.BooleanField(default=False)
    beneficiary_id = models.CharField(null=True, max_length=20)
    is_beneficiary = models.BooleanField(default=False)

    def __str__(self):
        return self.number


class Designation(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(null=True, max_length=10)
    aadhaar_number = models.CharField(max_length=12)
    total_salary = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    advance_taken = models.IntegerField(default=0)
    account = models.ForeignKey(Account, null=True, on_delete=models.PROTECT)
    designation = models.ForeignKey(Designation, null=True, on_delete=models.PROTECT)
    city = models.ForeignKey(City, null=True, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, null=True, on_delete=models.PROTECT)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    status = models.BooleanField(null=True)
    fcm_registration_token = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.name


class Payment(models.Model):
    title = models.CharField(max_length=150)
    salary_month = models.CharField(max_length=50)
    payment_date = models.DateField(null=True)
    no_of_workers = models.IntegerField()
    total_salary_amount = models.IntegerField()
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)


class Salary(models.Model):
    total_salary = models.IntegerField()
    advance_taken = models.IntegerField()
    net_salary = models.IntegerField()
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)


class Transfer(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.FloatField()
    transfer_id = models.CharField(null=True, max_length=20)
    utr = models.CharField(null=True, max_length=30)
    status = models.CharField(null=True, max_length=20)
    detail = models.CharField(null=True, max_length=150)
    processed_on = models.DateTimeField(null=True)
    payment = models.ForeignKey(Payment, null=True, on_delete=models.PROTECT)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)


class Advance(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.FloatField()
    transfer_id = models.CharField(null=True, max_length=20)
    utr = models.CharField(null=True, max_length=30)
    status = models.CharField(null=True, max_length=20)
    detail = models.CharField(null=True, max_length=150)
    processed_on = models.DateTimeField(null=True)
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT)

    @property
    def account_number(self):
        return self.account.number

    @property
    def ifsc(self):
        return self.account.ifscode.code

    @property
    def bank_name(self):
        return self.account.ifscode.bank.name


class Attendance(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
    punch_at = models.DateTimeField()