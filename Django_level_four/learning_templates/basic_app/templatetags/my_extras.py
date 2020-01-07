from django import template

register = template.Library()

#@register.filter(name='cutx')
def loope(value,arg):
    """"
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg,'')

#register.filter('custom filter tag name',function itself is called)
register.filter('loope',loope)
