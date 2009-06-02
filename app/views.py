from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django import template
from tabnu.app.models import Tab

def index(request):
	try:
		tabs_list = Tab.objects.filter(parent=None).order_by('order_value')
	except Tab.DoesNotExist:
		output = _('No root tabs exist')
		return render_to_response('app/error.html', {'error_message': output})

	# update children (according to parents)
	for tab in tabs_list:
		tab.children = tab.child_set.all()
	debug = ''
	return render_to_response('app/index.html', {'tabs': tabs_list, 'title': 'Shahar Livne - TabNU', 'debug': debug },
		context_instance=template.RequestContext(request))

def tab(request, tab_name):
	try:
		tab = Tab.objects.get(name=tab_name)
	except Tab.DoesNotExist:
		output = _('Tab %(tab_name)s does not exist') % {'tab_name': tab_name}
		return render_to_response('app/error.html', {'error_message': output})
	# update children
	tab.children = tab.child_set.all()
	debug = ''
	return render_to_response('app/tab.html', {'tab': tab, 'title': 'Shahar Livne - TabNU', 'debug': debug },
		context_instance=template.RequestContext(request))
