from django import template


register = template.Library()


@register.filter()
def censor(value):
   low = value.lower()
   censor_list = ['some', 'tit']
   for i in censor_list:
      if i.find(low):
         low = value.replace(i, '*' * len(i))
   return f'{low} '
