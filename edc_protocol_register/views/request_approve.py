from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render,redirect,get_object_or_404

from ..models import ProtocolRequest
from ..approve_protocol import ApproveProtocol


@login_required
@permission_required('can_approve_request')
def approve_request(request, id):
    ap = ApproveProtocol()
    protocol_request = get_object_or_404(ProtocolRequest, pk=id)
    if request.method == 'POST':
        if request.user.has_perm('edc_protocol_register.can_approve_request'):
            ap.approve(protocol_request=protocol_request)
            return redirect('request_list')

    return render(request, 'edc_protocol_register/fail.html')