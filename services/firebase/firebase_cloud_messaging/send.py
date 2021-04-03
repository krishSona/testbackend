from fcm_django.models import FCMDevice
from services.firebase.firebase_cloud_messaging.templates import notification


def send_notification(user_ids, title, template, data, *args):
    message = getattr(notification, template)(args)
    default_data = {
        "click_action": "FLUTTER_NOTIFICATION_CLICK",
        "android": {
            "notification": {
                "channel_id": "high_importance_channel"
            }
        }
    }
    if data:
        default_data.update(data)
    try:
        devices = FCMDevice.objects.filter(user__in=user_ids)
        result = devices.send_message(
            title=title,
            body=message,
            data=default_data,
            sound=True
        )
        return result
    except Exception as e:
        print(e)


