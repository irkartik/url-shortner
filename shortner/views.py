
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.base import RedirectView
from django.conf import settings
from .models import Link
from django.shortcuts import redirect, render

# Create your views here.
class LinkCreate(CreateView):
	model = Link
	fields = ["url"]

	def form_valid(self, form):
		prev = Link.objects.filter(url=form.instance.url)
		if prev:
			return redirect("link_show", pk=prev[0].pk)
		return super(LinkCreate, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(LinkCreate, self).get_context_data(**kwargs)
		# Passing link_list to display original and short_url in link_form.html
		context['link_list'] = Link.objects.all().order_by('-id')[:10]
		# Passing site_url to display domain base
		context['site_url'] = settings.SITE_URL
		return context

# class LinkShow(DetailView):
# 	model = Link
# 	def get_context_data(self, **kwargs):
# 		context = super(LinkShow, self).get_context_data(**kwargs)
# 		context['site_url'] = settings.SITE_URL
# 		return context

def LinkShow(request, pk):
	context = {
		'site_url' : settings.SITE_URL,
		'object' : Link.objects.get(id=pk),
	}
	return render(request, 'shortner/link_detail.html', context)

def RedirectToLongURL(request, short_url):
	print(Link.expand(short_url))
	return redirect(Link.expand(short_url))