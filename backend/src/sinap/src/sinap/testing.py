from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import sinap


class SINAPLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=sinap)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "sinap:default")
        applyProfile(portal, "sinap:initial")


SINAP_FIXTURE = SINAPLayer()


SINAP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAP_FIXTURE,),
    name="SINAPLayer:IntegrationTesting",
)


SINAP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAP_FIXTURE, WSGI_SERVER_FIXTURE),
    name="SINAPLayer:FunctionalTesting",
)


SINAPACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="SINAPLayer:AcceptanceTesting",
)
