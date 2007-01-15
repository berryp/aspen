"""Define some handlers that always return a single HTTP Response.
"""

def HTTP403(environ, start_response):
    start_response('403 Forbidden', [])
    return ['This directory has no index.']

def HTTP404(environ, start_response):
    start_response('404 Not Found', [])
    return ['Resource not found.']
