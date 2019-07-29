from django.shortcuts import render,redirect,get_object_or_404
from ..models import ProtocolRequest
from ..approvalManager import ApproveProtocol
from django.contrib.auth.decorators import login_required


@login_required
def reject_request(request, id):
    ap = ApproveProtocol()
    protocol_request = get_object_or_404(ProtocolRequest, pk=id)  # get current request object
    if request.method == 'POST':
        ap.reject(protocol_request)
        redirect('request_list')

    return render(request, 'protocol/detail.html', {'request': protocol_request})