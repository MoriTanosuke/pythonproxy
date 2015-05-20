from django.template import Library, Node
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

register = Library()

@register.simple_tag
def active(request, pattern):
    print("Request: " + request.path + " Pattern: " + pattern)
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''
