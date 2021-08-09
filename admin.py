import firebase_admin
from firebase_admin import credentials, messaging
import datetime
import json

cred = credentials.Certificate('config/firebase-admin.json')
firebase_admin.initialize_app(cred)

def send_notification(title, message, to=[], data={}):
    data.update({
        "body": message,
        "title": title,
        'type': 'confimar_embarque', # aqui vai a informacao sobre o tipo da notificacao
        'email': 'eutransportador@gmail.com', # aqui vai o email do usuário
        "click_action": "FLUTTER_NOTIFICATION_CLICK",
        'data': json.dumps({'email': 'eutransportador@gmail.com'})
    })
    registration_tokens = to

    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=message,
        ),
        android=messaging.AndroidConfig(
            ttl=datetime.timedelta(seconds=5*60),
            priority='high',
            
            notification=messaging.AndroidNotification(
                icon='stock_ticker_update',
                color='#f45342',
                sound='default',
                # click_action='FLUTTER_NOTIFICATION_CLICK',
            ),
        ),
        data=data,
        tokens=registration_tokens,
    )
    response = messaging.send_multicast(message)
    print('data: {}\n'.format(data))
    print('{0} messages were sent successfully'.format(response.success_count))


