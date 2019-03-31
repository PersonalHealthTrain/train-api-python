from tests.base import BaseTest
from types import MappingProxyType
from pht.internal.util.typetest import is_primitive, is_list, is_mapping, is_str, is_hashable
from pht.internal.protocol.SimpleMappingRepresentable import SimpleMappingRepresentable


class TypetestTests(BaseTest):

    def _assertIsSimpleMapping(self, x):
        return self.assertThat(SimpleMappingRepresentable.is_simple_mapping(x))

    def _assertIsNotSimpleMapping(self, x):
        return self.assertThatNot(SimpleMappingRepresentable.is_simple_mapping(x))

    ######################################################
    # is_primitive
    ######################################################
    def test_is_primitive_1(self):
        self.assertThat(is_primitive(1))

    def test_is_primitive_2(self):
        self.assertThat(is_primitive(True))

    def test_is_primitive_3(self):
        self.assertThat(is_primitive(False))

    def test_is_primitive_4(self):
        self.assertThat(is_primitive(0))

    def test_is_primitive_5(self):
        self.assertThat(is_primitive(0.0))

    def test_is_primitive_6(self):
        self.assertThat(is_primitive(''))

    def test_is_primitive_7(self):
        self.assertThat(is_primitive(None))

    def test_is_primitive_8(self):
        self.assertThat(is_primitive('foo'))

    def test_is_primitive_9(self):
        self.assertThat(is_primitive(42))

    def test_is_primitive_10(self):
        self.assertThat(is_primitive(-42))

    def test_is_primitive_11(self):
        self.assertThat(is_primitive(42.42))

    def test_is_primitive_12(self):
        self.assertThat(is_primitive(-13.12))

    def test_is_not_primitive_1(self):
        self.assertThatNot(is_primitive([]))

    def test_is_not_primitive_2(self):
        self.assertThatNot(is_primitive({}))

    def test_is_not_primitive_3(self):
        self.assertThatNot(is_primitive(range(6)))

    ######################################################
    # is_list
    ######################################################
    def test_is_list_1(self):
        self.assertThat(is_list([]))

    def test_is_list_2(self):
        self.assertThat([1, 2])

    def test_is_list_3(self):
        self.assertThat([1])

    def test_is_list_4(self):
        self.assertThat(list(range(3)))

    def test_is_not_list_1(self):
        self.assertThatNot(is_list(range(3)))

    def test_is_not_list_2(self):
        self.assertThatNot(is_list('foo'))

    def test_is_not_list_3(self):
        self.assertThatNot(is_list(''))

    ######################################################
    # isMapping
    ######################################################
    def test_is_mapping_1(self):
        self.assertThat(is_mapping({}))

    def test_is_mapping_2(self):
        self.assertThat(is_mapping({'foo': 'bar'}))

    def test_is_mapping_3(self):
        self.assertThat(is_mapping(MappingProxyType({'foo': 'bar'})))

    ######################################################
    # is str
    ######################################################
    def test_is_str_1(self):
        self.assertThat(is_str(''))

    def test_is_str_2(self):
        self.assertThat(is_str('foo'))

    def test_is_str_3(self):
        self.assertThatNot(is_str(['f', 'o', 'o']))

    ######################################################
    # is Hashable
    ######################################################
    def test_is_hashable_1(self):
        self.assertThat(is_hashable(''))

    def test_is_hashable_2(self):
        self.assertThat(is_hashable(1))

    def test_is_hashable_3(self):
        self.assertThat(is_hashable(None))

    def test_is_hashable_4(self):
        self.assertThat(is_hashable(frozenset({1, 2})))

    def test_is_hashable_5(self):
        self.assertThat(is_hashable((1, 2, 'foo')))

    ######################################################
    # SimpleMapping
    ######################################################
    def test_is_simple_dict_1(self):
        self._assertIsSimpleMapping({})

    def test_is_simple_dict_2(self):
        self._assertIsSimpleMapping({'foo': 'bar'})

    def test_is_simple_dict_3(self):
        self._assertIsSimpleMapping({'foo': {'bar': 1, 'baz': 2}})

    def test_is_simple_dict_4(self):
        self._assertIsSimpleMapping({'foo': {'bar': 1, 'baz': [1, 2]}})

    def test_is_not_simple_dict_1(self):
        self._assertIsNotSimpleMapping({'foo': range(1)})
