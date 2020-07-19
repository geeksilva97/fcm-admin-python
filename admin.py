import firebase_admin
from firebase_admin import credentials, messaging
import datetime
import json

cred = credentials.Certificate('config/firebase-admin.json')
firebase_admin.initialize_app(cred)

def send_notification(title, message, to=[], data={}):
    # registration_tokens = [
    #     'dgtKyE3PzDgtJz_NxaSP5A:APA91bGYm8jkmLt-k3ZWquUsQy_zwOPigaK_iO-TYgYNJHO29L3P42jFGBb7XWLXApXErtNU18-yZucN37fA2AG35lB4d23YsI3pXns6l7s5BzEadWcqsM_qZdYFHtPmAZwXO2ZcHomE'
    # ]
    # data['click_action'] = 'FLUTTER_NOTIFICATION_CLICK'
    # data['title'] = 'MY TITLE'
    # data['body'] = 'MY BODY'
    data.update({
        "body": message,
        "title": title,
        'type': 'confimar_embarque', # aqui vai a informacao sobre o tipo da notificacao
        'email': 'eutransportador@gmail.com', # aqui vai o email do usuário
        "click_action": "FLUTTER_NOTIFICATION_CLICK",
        "id": "1",
        "status": "done",
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
            #     title=title,
            # b   body=message,
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
    # See the BatchResponse reference documentation
    # for the contents of response.
    print('data: {}\n'.format(data))
    print('{0} messages were sent successfully'.format(response.success_count))


