from z3c.form import interfaces
from zope import schema
from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.leadimagesize')

class ILeadImageSizeSettings(form.Schema):
    """Adds settings to medialog.controlpanel
    """

    form.fieldset(
        'leadimage',
        label=_(u'LeadImage'),
        fields=[
             'leadimagesize',
        ],
     )
    
    leadimagesize = schema.Choice(
        title = _("label_leadimagesize", default=u"Image Size"),
        description = _("help_leadimagesize",
                      default="Choose Default Image Size"),
        vocabulary='medialog.leadimagesize.ImageSizeVocabulary',
        default='mini',
    )



        
alsoProvides(ILeadImageSizeSettings, IMedialogControlpanelSettingsProvider)