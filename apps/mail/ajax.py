from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

import json

class MailOptionsNotComplete(Exception):
    pass

@login_required(login_url="/mail/login")
def sendmail(request):
    if request.is_ajax() and request.method == 'POST':
        sendor = "%s%s <%s>" % (request.user.last_name, request.user.first_name, request.user.email)
        recps_email = request.POST.get('emails')
        topic = request.POST.get('topic')
        content = request.POST.get('content')

        if recps_email.strip() == "" or topic.strip() == "" or content.strip() == "" or recps_email.strip() == "":
            raise MailOptionsNotComplete("Mail options haven't been completed.")

        recipients = map( lambda x:x.strip()  , recps_email.split(','))
        

        sendmail_options = {
                'subject': topic,
                'message': content,
                'from_email' : sendor,
                'recipient_list' : recipients
                }


        try:
            send_mail(**sendmail_options)
        except:
            result = { 'status': False , 'msg': 'error while sending mails.' }
            return HttpResponse( json.dumps( result ), mimetype='application/json')
        else:
            result = { 'status': True , 'msg': 'mails sent successfully.' }
            return HttpResponse( json.dumps( result ), mimetype='application/json')

    else:
        raise Http404
