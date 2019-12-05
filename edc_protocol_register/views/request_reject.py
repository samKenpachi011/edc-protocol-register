from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render,redirect,get_object_or_404

from ..approvalManager import ApproveProtocol
from ..models import ProtocolRequest


@login_required
@permission_required('can_reject_request')
def reject_request(request, id_):
    ap = ApproveProtocol()
    protocol_request = get_object_or_404(ProtocolRequest, pk=id_)
    if request.method == 'POST':
        if request.user.has_perm('edc_protocol_register.can_reject_request'):
            # get reason from post data
            data = request.POST.get('reason')
            ap.reject(protocol_request=protocol_request, reason=data)
        return redirect('request_list')

    return render(request, 'edc_protocol_register/fail.html')