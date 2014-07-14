Installation
------------

To install drchen.theme using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``drchen.theme`` to the list of eggs to install, e.g.::

    [buildout]
    ...
    eggs =
        ...
        drchen.theme

* Re-run buildout, e.g. with::

    $ ./bin/buildout

* Re-start the Zope server::

    $ ./bin/instance restart

Then activate 'DrChen Theme' in Plone (Site Setup -> Add-ons).

