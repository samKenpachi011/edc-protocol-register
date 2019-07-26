from django.core.mail import send_mail

req_subject = "bhp protocol request "
req_body = "your protocol request has been submited successfully"

res_subject_approved="request approved"
res_subject_rejected="request rejected"
res_body_approved="your request has been approved"
res_body_rejected="your request has been rejected"
sender = "postmaster@sandboxceec9532622a40f297ed91245b14cb8c.mailgun.org"


def send_email(email, response=False,approved=False, reason=""):
    if approved and response:
        send_mail(
            res_subject_approved,
            res_body_approved,
            sender,
            [email,],
            fail_silently=False
        )
    elif approved is False and response:
        send_mail(
            res_subject_rejected,
            reason,
            sender,
            [email, ],
            fail_silently=False
            )
    elif approved and response is False:
        send_mail(
            req_subject,
            req_body,
            sender,
            [email, ],
            fail_silently=False
        )
        

        

