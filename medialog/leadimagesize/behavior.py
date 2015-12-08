from zope import schema
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from plone import api
from medialog.leadimagesize.interfaces import ILeadImageSizeSettings


   
_ = MessageFactory('medialog.leadimagesizes')
 
class ICustomSize(form.Schema):
    """ A field where you can set the size for lead image"""
    
    def defaultleadsize():
        """Returns default settings"""
        return 'mini'
        # (api.portal.get_registry_record('medialog.leadimagesize.interfaces.ILeadImageSizeSettings.leadsize'))
            
    leadsize = schema.Choice(
        title = _("label_leadimagesize", default=u"Image Size"),
        description = _("help_leadimagesize",
                      default="Choose Size"),
        vocabulary='medialog.leadimagesize.LeadImageSizeVocabulary',
        default='defaultleadsize',
    )

alsoProvides(ICustomSize, IFormFieldProvider)

