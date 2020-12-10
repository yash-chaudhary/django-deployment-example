from django import template

register = template.Library()

def cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    """

    return value.replace(arg,'')

# when registering, first input is what you are calling the string that you call
# the function and cut is the function itself as defined above
register.filter('cut', cut)
