from ert_gui.ide.keywords.definitions import ProperNameFormatArgument
from tests import ResTest


class ProperNameFormatArgumentTest(ResTest):

    def test_proper_name_format_argument(self):

        argument = ProperNameFormatArgument()

        self.assertTrue(argument.validate("NAME%d"))
        self.assertTrue(argument.validate("__NA%dME__"))
        self.assertTrue(argument.validate("<NAME>%d"))
        self.assertTrue(argument.validate("%d-NAME-"))

        self.assertFalse(argument.validate("-%dNA ME-"))
        self.assertFalse(argument.validate("NAME*%d"))

