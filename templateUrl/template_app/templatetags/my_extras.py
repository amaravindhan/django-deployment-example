from django import template

register = template.Library()

# Custom filters

def cut(value, arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg, '')

# registering Filter
register.filter('cut', cut)
# OR
@register.filter(name = 'mul')
def multiply(value, times):
    """
    This multipies value for times
    """
    return value*int(times)
