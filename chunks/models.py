from django.db import models
from django.utils.translation import ugettext_lazy as _


class Chunk(models.Model):
    """
    A Chunk is a piece of content associated
    with a unique key that can be inserted into
    any template with the use of a special template
    tag
    """
    key = models.CharField(_('key'), help_text=_('A unique name for this chunk of content'), primary_key=True, max_length=255)
    content = models.TextField(_('content'), blank=True)

    class Meta:
        ordering = ('key',)
        verbose_name = _('chunk')
        verbose_name_plural = _('chunks')
    
    def __unicode__(self):
        return u'%s' % (self.key,)

