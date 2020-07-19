from admin import send_notification

# token_web = 'dgtKyE3PzDgtJz_NxaSP5A:APA91bGYm8jkmLt-k3ZWquUsQy_zwOPigaK_iO-TYgYNJHO29L3P42jFGBb7XWLXApXErtNU18-yZucN37fA2AG35lB4d23YsI3pXns6l7s5BzEadWcqsM_qZdYFHtPmAZwXO2ZcHomE'
token_mobile = 'cK09jkhyF1I:APA91bH9jNwcvzH_TZDTveVkO4fiJwzbTSNZHNtQYacGYhTUJ5fcB9SRBLtikio5C4CVgRYOaN8lOOlEUjqRy8R5y3ZM9EneiAXbVw3pNwWIeAgfBkZpaOcE4slOUvE3WaDKShN-bw8e'

# print('Informe o título:')
# title = input()

# print('Informe o corpo:')
# message = input()

send_notification(
    'Gooex',
    'Cansado dessa porra!!',
    to=[token_mobile]
)