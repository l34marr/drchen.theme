from Products.Five import BrowserView
from zope.component import getMultiAdapter
from zope.interface import implements

from drchen.theme.interfaces import IDrChenView

_marker = []


class DrChenView(BrowserView):
    implements(IDrChenView)

    # Utility methods

    def getColumnsClasses(self, view=None):
        """Determine Whether a Column Should Be Shown.
           Their Names Are Called plone.leftcolumn and plone.rightcolumn.
        """

        plone_view = getMultiAdapter(
            (self.context, self.request), name=u'plone')
        portal_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state')

        sl = plone_view.have_portlets('plone.leftcolumn', view=view);
        sr = plone_view.have_portlets('plone.rightcolumn', view=view);

        isRTL = portal_state.is_rtl()

        # pre-fill dictionary
        columns = dict(one="", content="", two="")

        if not sl and not sr:
            # we don't have columns, thus conten takes the whole width
            columns['content'] = "width-full position-0"

        elif sl and sr:
            # In case we have both columns, content takes 50% of the whole
            # width and the rest 50% is spread between the columns
            columns['one'] = "width-1:4 position-0"
            columns['content'] = "width-1:2 position-1:4"
            columns['two'] = "width-1:4 position-3:4"

        elif (sr and not sl) and isRTL:
            # We have right column and we are in RTL language
            columns['content'] = "width-3:4 position-1:4"
            columns['two'] = "width-1:4 position-0"

        elif (sr and not sl) and not isRTL:
            # We have right column and we are NOT in RTL language
            columns['content'] = "width-3:4 position-0"
            columns['two'] = "width-1:4 position-3:4"

        elif (sl and not sr) and isRTL:
            # We have left column and we are in RTL language
            columns['one'] = "width-1:4 position-3:4"
            columns['content'] = "width-3:4 position-0"

        elif (sl and not sr) and not isRTL:
            # We have left column and we are in NOT RTL language
            columns['one'] = "width-1:4 position-0"
            columns['content'] = "width-3:4 position-1:4"

        # append cell to each css-string
        for key, value in columns.items():
            columns[key] = "cell " + value

        return columns

    def getColumnsClass(self, view=None):
        """XXX: Keep Old Customized main_templates Working,
           This Should Be Marked as Deprecated in Future.
        """

        return self.getColumnsClasses(view).get('content')

