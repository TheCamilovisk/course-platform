from django.http import HttpResponse

from emails import services


# Create your views here.
def verify_email_token_view(request, token, *args, **kwargs):
    did_verify, msg = services.verify_token(token)
    if not did_verify:
        return HttpResponse(msg)
    return HttpResponse(token)
