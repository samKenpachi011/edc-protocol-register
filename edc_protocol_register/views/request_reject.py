from django.shortcuts import render,redirect,get_object_or_404
from ..models import ProtocolRequest
from ..approvalManager import ApproveProtocol
from django.contrib.auth.decorators import login_required,permission_required
from ..forms import RejectForm
import json


@login_required
@permission_required('can_reject_request')
def reject_request(request, id):
    ap = ApproveProtocol()
    protocol_request = get_object_or_404(ProtocolRequest, pk=id)
    if request.method == 'POST':
        data = request.POST.get('reason')
        print(data)
        ap.reject(protocol_request=protocol_request, reason=data)
        return redirect('request_list')

    return render(request, 'edc_protocol_register/fail.html')