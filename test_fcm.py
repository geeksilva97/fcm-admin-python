from admin import send_notification

token_web = 'dgtKyE3PzDgtJz_NxaSP5A:APA91bGYm8jkmLt-k3ZWquUsQy_zwOPigaK_iO-TYgYNJHO29L3P42jFGBb7XWLXApXErtNU18-yZucN37fA2AG35lB4d23YsI3pXns6l7s5BzEadWcqsM_qZdYFHtPmAZwXO2ZcHomE'
token_mobile = 'enZBYzC-MJg:APA91bEQnFjawk4A4trokV5MUTmDbs6uKZKE2lfNVgs668Vw0ySzbG2xjI-3qLOob_IVAeos3tgZQ0T2AxYnlPnrqD-t_4CKLlEH-CgUctlMh8xjcOxMMwjKgX9JYmxTPr1bcptvEG_L'

print('Informe o título:')
title = input()

print('Informe o corpo:')
message = input()

send_notification(
    title,
    message,
    to=[token_mobile, token_web]
)