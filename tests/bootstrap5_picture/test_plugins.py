from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap5.contrib.bootstrap5_picture.cms_plugins import (
    Bootstrap5PicturePlugin,
)

from ..fixtures import B5TestFixture
from ..helpers import get_filer_image


class B5PicturePluginTestCase(B5TestFixture, CMSTestCase):

    def setUp(self):
        super().setUp()
        self.image = get_filer_image()

    def tearDown(self):
        super().tearDown()
        self.image.delete()

    def test_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap5PicturePlugin.__name__,
            language=self.language,
            picture=self.image,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'class="img-fluid"')

        # test picture_fluid, picture_rounded and picture_thumbnail options
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap5PicturePlugin.__name__,
            language=self.language,
            picture=self.image,
            picture_fluid=False,
            picture_rounded=True,
            picture_thumbnail=True,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'class="rounded img-thumbnail"')