"""Main Product Initializer
"""

from zope.i18nmessageid import MessageFactory

# Define a Message Factory For When This Product Is Internationalised.
# This Will Be Imported With the Special Name "_" In Most Modules. Strings
# Like _(u"message") Will Then Be Extracted By I18N Tools For Translation.

GLOBALS = globals()

drchenMessageFactory = MessageFactory('drchen.theme')

def initialize(context):
    """Initializer Called When Used As a Zope2 Product.

    This Is Referenced From configure.zcml. Regstrations As a "Zope2 Product"
    Is Necessary For GenericSetup Profiles to Work, For Example.
    """

