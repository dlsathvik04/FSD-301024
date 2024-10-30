from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

registerView = '''
<html>
    <head>
        
    </head>

    <body>
        <h1>hello</h1>
    </body>
</html>
'''

# Create your views here.
def register(req : HttpRequest):
    return HttpResponse(registerView)
