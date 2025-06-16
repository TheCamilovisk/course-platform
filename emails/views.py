from django.contrib import messages
from django.shortcuts import redirect

from emails import services


# Create your views here.
def verify_email_token_view(request, token, *args, **kwargs):
    did_verify, msg, email_obj = services.verify_token(token)
    if not did_verify:
        try:
            del request.session['email_id']
        except:
            pass
        messages.error(request, msg)
        return redirect('/login/')
    messages.success(request, msg)
    request.session['email_id'] = f'{email_obj.id}'
    next_url = request.session.get('next_url') or '/'
    if not next_url.startswith('/'):
        next_url = '/'
    return redirect(next_url)
