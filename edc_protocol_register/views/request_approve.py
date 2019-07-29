from django.shortcuts import render,redirect,get_object_or_404
from ..models import ProtocolRequest, ProtocolResponse, Protocol
from ..approvalManager import ApproveProtocol
from django.contrib.auth.decorators import login_required


@login_required
def approve_request(request, id):
    ap =ApproveProtocol()
    protocol_request = get_object_or_404(ProtocolRequest,pk=id)
    if request.method == 'POST':
        ap.approve(protocol_request=protocol_request)
        return redirect('request_list')
    return render(request, 'protocol/detail.html', {'protocol': protocol_request})