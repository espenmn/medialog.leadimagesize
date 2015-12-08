from zope import schema
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.leadimagesizes')
 
class ICustomSize(form.Schema):
    """ A field where you can set the size for lead image"""
    leadsize = schema.Choice(
        title = _("label_leadimagesize", default=u"Image Size"),
        description = _("help_leadimagesize",
                      default="Choose Size"),
        vocabulary='medialog.leadimagesize.LeadImageSizeVocabulary',
        default='mini',
    )

alsoProvides(ICustomSize, IFormFieldProvider)

