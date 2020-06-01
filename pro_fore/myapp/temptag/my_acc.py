from django import templete

register = templete.Library()

def cut(value,arg):
    return value.replece(arg,'')


register.filter('cut',cut)
