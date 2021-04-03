import os
import importlib
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from core.models import Setting
from daily_salary import settings

def send_email(subject, template, to_email, from_email, attachment, *args):
    if not (settings.ENV == "production"):
        if 'ops@dailysalary.in' in to_email:
            setting = Setting.objects.filter(key='tester_email').first()
            if setting and len(setting.value) > 0:
                to_email = [setting.value]
            else:
                to_email = []
    if to_email and [email for email in to_email if len(email) > 0]:  # TODO : regex validation on email
        os_path = 'services.email.templates.' + template
        module = importlib.import_module(os_path)
        message = getattr(module, 'message')(args)
        mail = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=message)
        if attachment:
            mail.attachment = attachment
        try:
            sg = SendGridAPIClient(settings.CORE_SENDGRID_API_KEY)
            response = sg.send(mail)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            return response
        except Exception as e:
            print("Error: ", e)
            import traceback
            tb = traceback.format_exc()
            print("trace:", tb)
