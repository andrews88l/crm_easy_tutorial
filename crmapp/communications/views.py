from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from .forms import CommunicationForm

from .models import Communication
from crmapp.accounts.models import Account

# Create your views here.

@login_required()
def comm_detail(request, uuid):

	comm = Communication.objects.get(uuid=uuid)
	if comm.owner != request.user:
		return HttpResponseForbidden()

	return render(request, 'communications/comm_detail.html', {'comm' : comm})

@login_required()
def comm_cru(request, uuid=None, account=None):

	if uuid:
		comm = get_object_or_404(Communication, uuid=uuid)
		if comm.owner != request.user:
			return HttpResponseForbidden()
	else:
		comm = Communication(owner=request.user)

	if request.POST:
		form = CommunicationForm(request.POST, instance=comm)
		if form.is_valid():
			# make sure the user owns the account
			account = form.cleaned_data['account']
			if account.owner != request.user:
				return HttpResponseForbidden()
			# save the data
			form.save()
			# return the user to the account detail view
			if request.is_ajax():
				return render(request, 'communicationis/comm_item_view.html', {'comm' : comm, 'account' : account})
			else:
				reverse_url = reverse('crmapp.acounts.views.account_detail', args=(account.uuid,))
				return HttpResponseRedirect(reverse_url)
		else:
			# if the form isn't valid, still fetch the account so it can be passed to the template
			account = form.cleaned_data['account']
	else:
		form = CommunicationForm(instance=comm)

	variables = {
		'form' : form,
		'comm' : comm,
		'account' : account,
	}

	if request.is_ajax():
		template = 'communications/comm_item_form.html'
	else:
		template = 'communications/comm_cru.html'

	return render(request, template, variables)