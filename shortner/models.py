from django.db import models
from django.core.urlresolvers import reverse
from hashids import Hashids
hashids = Hashids()
# Create your models here.
class Link(models.Model):
	# Using this field is actually a Charfield but with a URL validator. AWESOME!
	url = models.URLField()

	def get_absolute_url(self):
		return reverse("link_show", kwargs={"pk": self.pk})

	def __str__(self):
		return self.url

	# ENCODES URL TO A HASH VALUE
	@staticmethod
	def shorten(link):
		l, _ = Link.objects.get_or_create(url=link.url)
		return str(hashids.encrypt(l.pk))

	# DECODES THE ENCODED HASH VALUE TO URL LINK
	@staticmethod
	def expand(slug):
		dirty_str = str(hashids.decrypt(slug))
		print(dirty_str)
		clean_id = dirty_str.strip("(,)")
		print(clean_id)
		link_id = int(clean_id)
		l = Link.objects.get(pk=link_id)
		return l.url

	def short_url(self):
		return reverse("redirect_short_url",
                   kwargs={"short_url": Link.shorten(self)})