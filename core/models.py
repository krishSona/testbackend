import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import Q
from dynamic_validator import ModelFieldRequiredMixin

import utilities
import datetime
import calendar
import math


class Industry(ModelFieldRequiredMixin, models.Model):
    name = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.name)


class EmployeeRange(ModelFieldRequiredMixin, models.Model):
    number = models.CharField(max_length=10)

    REQUIRED_FIELDS = ['number']

    def __str__(self):
        return str(self.number)


class City(ModelFieldRequiredMixin, models.Model):
    name = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.name)


class State(ModelFieldRequiredMixin, models.Model):
    name = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.name)


COMPANY_CATEGORY = [
    (0, 'contractor'),
    (1, 'principal_employer'),
]


class Company(ModelFieldRequiredMixin, models.Model):
    rid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    industry = models.ForeignKey(
        Industry, on_delete=models.PROTECT, null=True, blank=True)
    employee_range = models.ForeignKey(
        EmployeeRange, on_delete=models.PROTECT, null=True, blank=True)
    office_address = models.TextField(null=True, blank=True)
    city = models.ForeignKey(
        City, on_delete=models.PROTECT, null=True, blank=True)
    state = models.ForeignKey(
        State, on_delete=models.PROTECT, null=True, blank=True)
    pincode = models.CharField(max_length=6, null=True, blank=True)
    gstin = models.CharField(
        max_length=15, unique=True, null=True, blank=True)
    average_monthly_salary_payout = models.IntegerField(
        blank=True, null=True)
    monthly_salary_day = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(default=0, choices=COMPANY_CATEGORY)
    code = models.CharField(max_length=6, null=True, blank=True, unique=True)
    domain_name = models.CharField(max_length=250, null=True, blank=True, unique=True)
    tie_up = models.BooleanField(default=False)
    subscription_amount = models.FloatField(default=0)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.name)


class QrCode(models.Model, ModelFieldRequiredMixin):
    qr_id = models.CharField(max_length=23, unique=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    REQUIRED_FIELDS = ['qr_id', 'company']

    def __str__(self):
        return str(self.qr_id)


class Department(ModelFieldRequiredMixin, models.Model):
    name = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.name)


class Designation(ModelFieldRequiredMixin, models.Model):
    name = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.name)


class Bank(ModelFieldRequiredMixin, models.Model):
    name = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.name)


class Ifs(ModelFieldRequiredMixin, models.Model):
    code = models.CharField(max_length=11)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)

    REQUIRED_FIELDS = ['code', 'bank']

    def __str__(self):
        return str(self.code)


class Level(ModelFieldRequiredMixin, models.Model):
    title = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['title']

    def __str__(self):
        return str(self.title)


class Employer(ModelFieldRequiredMixin, models.Model):
    rid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=255)
    user = models.ForeignKey('authentication.User', on_delete=models.PROTECT)
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, null=True, blank=True)
    designation = models.ForeignKey(
        Designation, on_delete=models.PROTECT, null=True, blank=True)
    principal_companies = models.ManyToManyField(Company, related_name='employers', blank=True)

    REQUIRED_FIELDS = ['email', 'name', 'phone', 'company']

    def __str__(self):
        return str(self.email)


def get_default_work_days():
    return {"days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]}


class Employee(models.Model):
    rid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=True,
        blank=True
    )
    mail_verified = models.BooleanField(null=True, blank=True)
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, blank=True, null=True)
    company_verified = models.BooleanField(null=True, blank=True)
    net_monthly_salary = models.IntegerField()
    verified_salary = models.IntegerField(null=True, blank=True)
    due_day = models.IntegerField(null=True, blank=True)
    kyc = models.BooleanField(null=True, blank=True)
    e_nach = models.BooleanField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    employee_id = models.CharField(max_length=50, null=True, blank=True)
    extra_data = JSONField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    salary_day = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)
    permanent_city = models.CharField(max_length=50, blank=True, null=True)
    permanent_state = models.CharField(max_length=50, blank=True, null=True)
    permanent_pincode = models.IntegerField(null=True, blank=True)
    current_address = models.TextField(null=True, blank=True)
    current_city = models.CharField(max_length=50, blank=True, null=True)
    current_state = models.CharField(max_length=50, blank=True, null=True)
    current_pincode = models.IntegerField(null=True, blank=True)
    service_status = models.IntegerField(default=0)
    credit_limit = models.FloatField(default=50)
    bank_account_number = models.CharField(max_length=18, null=True, blank=True)
    ifs = models.ForeignKey(Ifs, on_delete=models.PROTECT, null=True, blank=True)
    level = models.ForeignKey(
        Level, on_delete=models.PROTECT, null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    user = models.ForeignKey('authentication.User', on_delete=models.PROTECT)
    salary_type = models.CharField(max_length=50, default="net")
    agreed_with_terms_and_conditions = models.BooleanField(default=False)
    daily_salary = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    credited = models.FloatField(default=0)
    debited = models.FloatField(default=0)
    withdraw = models.FloatField(default=0)
    fees = models.FloatField(default=0)
    gst = models.FloatField(default=0)
    work_days = JSONField(default=get_default_work_days)
    work_timings = models.CharField(max_length=17, default="09:00 AM-06:00 PM")
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, null=True, blank=True)
    designation = models.ForeignKey(
        Designation, on_delete=models.PROTECT, null=True, blank=True)
    employer = models.ForeignKey(
        Employer, on_delete=models.PROTECT, blank=True, null=True)
    beneficiary_id = models.CharField(null=True, blank=True, max_length=20)
    is_beneficiary = models.BooleanField(default=False)
    check_location = models.BooleanField(default=True)
    wish_listing = models.BooleanField(default=False)
    mail_enabled = models.BooleanField(default=True, null=False)
    mail_bounced = models.IntegerField(default=0)
    mail_token = models.CharField(max_length=40, null=True, blank=True)
    unsubscribe_token = models.CharField(max_length=40, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    digital_time_stamp = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['net_monthly_salary', 'user', 'company', 'employer']

    def save(self, *args, **kwargs):
        if not self.pk:
            # create mail_token and unsubscribe_token of employee
            self.mail_token = utilities.get_random_time_based_token()
            self.unsubscribe_token = utilities.get_random_time_based_token()
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.phone)

    def get_daily_salary(self):
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        num_days_in_current_month = calendar.monthrange(year, month)[1]

        work_days_in_current_month = [
            datetime.date(year, month, day).weekday() for day in range(1, num_days_in_current_month + 1)
            if datetime.date(year, month, day).strftime('%a') in self.work_days.get('days')
        ]
        num_work_days_in_current_month = len(work_days_in_current_month)
        daily_salary = self.net_monthly_salary / num_work_days_in_current_month
        daily_salary = (math.floor(daily_salary / 50)) * 50
        return daily_salary

    # TODO: optimize (make a model field)
    def get_available_balance(self):
        attendance_queryset = Attendance.objects.filter(
            employee=self.pk,
            date__month=datetime.datetime.now().month,
            date__year=datetime.datetime.now().year
        )
        total_verified_salary = sum([attendance.verified_salary for attendance in attendance_queryset])
        transfer_up_to = (total_verified_salary * self.credit_limit) / 100
        transfer_up_to = transfer_up_to - self.withdraw
        return float(round(transfer_up_to))

    def calculate_work_day(self, num_days):
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        work_days = [
            datetime.date(year, month, day).weekday() for day in range(1, num_days + 1)
            if datetime.date(year, month, day).strftime('%a') in self.work_days.get('days')
        ]
        return len(work_days)


DURATION_CHOICES = [
    ("full_day", "full_day"),
    ("half_day", "half_day"),
]
WORK_LOCATION_CHOICES = [
    ("office", "office"),
    ("home", "home"),
    ("other", "other"),
]


class Attendance(ModelFieldRequiredMixin, models.Model):
    date = models.DateField(db_index=True, default=datetime.datetime.now)
    status = models.CharField(
        max_length=30, null=True, db_index=True)
    duration = models.CharField(
        max_length=10, null=True, blank=True, db_index=True, choices=DURATION_CHOICES)
    start_at = models.TimeField(null=True, blank=True)
    end_at = models.TimeField(null=True, blank=True)
    work_location = models.CharField(
        max_length=10, null=True, blank=True, choices=WORK_LOCATION_CHOICES)
    qr_code_scanned = models.BooleanField(null=True, blank=True)
    face_detected = models.BooleanField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    salary = models.FloatField(default=0)
    verified_salary = models.FloatField(default=0)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/attendance/', null=True, blank=True)

    REQUIRED_FIELDS = ['status', 'employee', 'company']

    def __str__(self):
        return str(self.date)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'employee', 'company'],
                name='make_unique_date_employee_company'
            ),
        ]


STATEMENT_STATUS_CHOICES = [
    ("initialized", "initialized"),
    ("pending", "pending"),
    ("waiting", "waiting"),
    ("rejected", "rejected"),
    ("approved", "approved"),
    ("cancelled", "cancelled"),
    ("completed", "completed"),
]


class Statement(ModelFieldRequiredMixin, models.Model):
    rid = models.UUIDField(default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add=True, db_index=True)
    status = models.CharField(max_length=15, choices=STATEMENT_STATUS_CHOICES, default="initialized")
    description = models.CharField(max_length=255)
    credit = models.FloatField(null=True)
    debit = models.FloatField(null=True)
    withdraw = models.FloatField(null=True, blank=True)
    fees = models.FloatField(null=True, blank=True)
    gst = models.FloatField(null=True, blank=True)
    balance = models.FloatField(null=True, blank=True)
    current_due = models.FloatField(null=True, blank=True)
    previous_due = models.FloatField(null=True, blank=True)
    interest = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_valid_till = models.DateTimeField(null=True, blank=True)
    digital_time_stamp = models.TextField(null=True, blank=True)

    REQUIRED_FIELDS = ['description', 'balance', 'employee', 'company']

    def __str__(self):
        return str(self.date)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(debit__isnull=False) | Q(credit__isnull=False),
                name='not_both_null'
            )
        ]


BOOKING_STATUS_CHOICES = [
    (0, 'open'),
    (1, 'pending'),
    (2, 'closed'),
]

CATEGORY_CHOICE = [
    (1, 'employee'),
    (2, 'employer'),
]


class Booking(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=255, null=True, blank=True)
    category = models.IntegerField(null=True, blank=True, choices=CATEGORY_CHOICE)
    status = models.IntegerField(default=0, db_index=True, choices=BOOKING_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.name)


class Setting(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.CharField(max_length=255)

    def __str__(self):
        return str(self.key)


class Pricing(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    min_price = models.IntegerField(null=True, blank=True)
    max_price = models.IntegerField()
    fee = models.IntegerField()

    def __str__(self):
        return str(self.fee)

    @staticmethod
    def calculate_fees(amount, company_obj):
        if amount is None or amount < 0:
            return None
        if company_obj.tie_up is False and amount == 0:
            return None
        if company_obj.tie_up is True and amount == 0:
            price_obj = Pricing.objects.filter(
                Q(company=company_obj) & Q(min_price=None) & Q(max_price=0)
            ).first()
            fee = float(price_obj.fee) if price_obj else None
        else:
            price_obj = Pricing.objects.filter(
                Q(company=company_obj) & Q(min_price__lt=amount) & Q(max_price__gte=amount)
            ).first()
            fee = float(price_obj.fee) if price_obj else None
        if fee and fee > 0:
            gst = (fee * 18) / 100
            fee = fee + gst
        return fee


class Verifier(models.Model):
    employee = models.ManyToManyField(Employee)
    email = models.EmailField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return str(self.email)


DOMAIN_CHOICE = [
    (0, 'generic'),
    (1, 'company')
]


class Domain(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)
    category = models.IntegerField(null=True, blank=True, choices=DOMAIN_CHOICE)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Application(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    company_email = models.CharField(max_length=255, null=True, blank=True)
    employee_id = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    net_monthly_salary = models.CharField(max_length=255, null=True, blank=True)
    salary_day = models.CharField(max_length=255, null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    bank_account_name = models.CharField(max_length=255, null=True, blank=True)
    bank_account_number1 = models.CharField(max_length=255, null=True, blank=True)
    bank_account_number2 = models.CharField(max_length=255, null=True, blank=True)
    ifsc = models.CharField(max_length=255, null=True, blank=True)
    utm_source = models.CharField(max_length=255, null=True, blank=True)
    utm_medium = models.CharField(max_length=255, null=True, blank=True)
    utm_campaign = models.CharField(max_length=255, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)
