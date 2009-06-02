from django.db import models
from django.utils.translation import ugettext_lazy as _
#from django.core import validators

# this version should change on each database change for backwards 
# compatibility
CURRENT_TAB_FORMAT_VERSION="0"

EFFECT_CHOICES = (
    ('NONE', 'None'),
    ('FADE', 'Fade'),
    ('SLID', 'Slide'),
    ('SLFD', 'Slide and Fade'),
)

class Tab(models.Model):
	name = models.CharField(_('Name'), unique=True, max_length=255)
	title = models.CharField(_('Title'), max_length=255)
	remark = models.CharField(_('Remark'), max_length=255)
	url = models.URLField(_('URL'), blank=True, max_length=1023)
	order_value = models.FloatField(_('Order value'), default=0.0)
	parent = models.ForeignKey('self', blank=True, null=True, related_name='child_set')
	updated = models.DateTimeField(_('Updated'), auto_now=True)
	active = models.BooleanField(_('Active'), default=True, help_text="Check this to activate the tab")
	effect = models.CharField(max_length=4, choices=EFFECT_CHOICES, default='FADE')
	version = models.CharField(_('Version'), max_length=32, editable=False, default=CURRENT_TAB_FORMAT_VERSION)

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		verbose_name = _('Tab')
		verbose_name_plural = _('Tabs')

	class Admin:
		list_display = ('name', 'title', 'remark', 'active', 'updated',)
		list_filter = ['active',]
		search_fields = ['name', 'title', 'remark', 'url',]
		fields = (
			(None, {
				'fields': ('name', 'title', 'remark', 'url', 'order_value', 'parent', 'updated', 'active', 'effect',)
			}),
		)

	def save(self):
		super(Tab, self).save()
