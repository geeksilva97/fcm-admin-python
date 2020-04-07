import firebase_admin
from firebase_admin import credentials, messaging
import datetime

cred = credentials.Certificate('config/gooexapp-firebase-adminsdk-xkhb9-2f4864d8c7.json')
firebase_admin.initialize_app(cred)

def send_notification(title, message, to=[]):
    # registration_tokens = [
    #     'dgtKyE3PzDgtJz_NxaSP5A:APA91bGYm8jkmLt-k3ZWquUsQy_zwOPigaK_iO-TYgYNJHO29L3P42jFGBb7XWLXApXErtNU18-yZucN37fA2AG35lB4d23YsI3pXns6l7s5BzEadWcqsM_qZdYFHtPmAZwXO2ZcHomE'
    # ]
    registration_tokens = to

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
        data={'score': '850', 'time': '2:45'},
        tokens=registration_tokens,
    )
    response = messaging.send_multicast(message)
    # See the BatchResponse reference documentation
    # for the contents of response.
    print('{0} messages were sent successfully'.format(response.success_count))


