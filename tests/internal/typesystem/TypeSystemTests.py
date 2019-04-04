from tests.base import BaseTest
from pht.internal.typesystem.TypeSystem import TypeSystem


class TypeSystemTests(BaseTest):

    def setUp(self):
        self.type_system = TypeSystem("pythonclass", "1.0")

    def test_name_1(self):
        self.checkExpect(
            expect='pythonclass',
            actual=self.type_system.name)

    def test_version_1(self):
        self.checkExpect(
            expect='1.0',
            actual=self.type_system.version)

    def test_copy_1(self):
        self.assertCopiesAreEqualOf(self.type_system)

    def test_eq_1(self):
        self.assertIsEqual(self.type_system, TypeSystem("pythonclass", "1.0"))

    def test_as_simple_dict(self):
        self.checkMapping(
            expect={
                'name': 'pythonclass',
                'version': '1.0'
            },
            actual=self.type_system.as_simple_mapping())
