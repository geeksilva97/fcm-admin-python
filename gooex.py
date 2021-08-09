import firebase_admin
from firebase_admin import credentials, messaging
import datetime
import json

cred = credentials.Certificate('./gooexapp-firebase-certificate.json')
firebase_admin.initialize_app(cred)


def send_notification(title, message, tokens=[], data={}):
  message = messaging.MulticastMessage(
      notification=messaging.Notification(
      title=title,
      body=message,
    ),
    android=messaging.AndroidConfig(
      ttl=datetime.timedelta(seconds=3600),
      priority='normal',

      notification=messaging.AndroidNotification(
        icon='stock_ticker_update',
        color='#f45342',
        sound='default',
      ),
    ),
    data=data,
    tokens=tokens,
  )

  response = messaging.send_multicast(message)
  print('{0} messages were sent successfully'.format(response.success_count))


send_notification(
  title='testando',
  message='Isso é apenas um teste',
  tokens=['eT4JWKnn8to:APA91bEXfq_bNa7Jo9m5YgTaiMTASPbzXBxDOWY1Tz-sBRXN-6Fd4tghzDIi0F9yLxZk5OaTIXQDCBZ4M8EAt5OzJbL4nqy30VMlvhrH14rTqPcMcnoM6rVX6ipj_UojW17FnimQm_uU']
)