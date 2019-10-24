import hashlib
from django import template

register = template.Library()

@register.filter
def makemd5(email):
    return hashlib.md5(request.user.email.strip().lower().encode('utf-8')).hexdigest()