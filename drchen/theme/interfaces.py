from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IThemeSpecific(IDefaultPloneLayer):
    """Zope Browser Layer Marker Interface.
    """

class ICustomTheme(Interface):
    """Zope Browser Layer Marker Interface.
    """

class IDrChenView(Interface):
    """Marker Interface
    """
    def getColumnsClass():
        """Returns CSS Class for Column Content Based on Columns Presence.
        """

    def getColumnsClasses():
        """Returns All CSS Classes Based on Columns Presence.
        """

