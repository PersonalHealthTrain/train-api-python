from tests.base import BaseTest
from pht.internal.response.describe.property.PropertyState import PropertyState


class PropertyStateTests(BaseTest):

    def setUp(self):
        self.avail1 = PropertyState(is_satisfied=True)
        self.avail2 = PropertyState(is_satisfied=True)
        self.unavail1 = PropertyState(is_satisfied=False, reason='foo')
        self.unavail2 = PropertyState(is_satisfied=False, reason='bar')

    ###########################################################################
    # Type Error
    ###########################################################################
    def test_type_1(self):
        self.assertTypeError(lambda: PropertyState(is_satisfied=True, reason=True))

    def test_type_2(self):
        self.assertTypeError(lambda: PropertyState(is_satisfied=True, reason=None))

    def test_type_3(self):
        self.assertTypeError(lambda: PropertyState(is_satisfied=True, reason={}))

    def test_type_4(self):
        self.assertTypeError(lambda: PropertyState(is_satisfied=True, reason=[]))

    def test_type_5(self):
        self.assertTypeError(lambda: PropertyState(is_satisfied=True, reason=1))

    def test_type_6(self):
        self.assertTypeError(lambda: PropertyState(is_satisfied=True, reason=2.4))

    ###########################################################################
    # Equals and hash
    ###########################################################################
    def test_equals_1(self):
        self.assertIsEqual(self.avail1, PropertyState(is_satisfied=True))

    def test_equals_2(self):
        self.assertIsEqual(self.avail2, PropertyState(is_satisfied=True))

    def test_equals_3(self):
        self.assertIsEqual(self.unavail1, PropertyState(is_satisfied=False, reason='foo'))

    def test_equals_4(self):
        self.assertIsEqual(self.unavail2, PropertyState(is_satisfied=False, reason='bar'))

    def test_unequal_1(self):
        self.assertUnequalCominationPairs([
            self.avail1, self.unavail1, self.unavail2])

    def test_unequal_2(self):
        self.assertUnequalCominationPairs([
            self.avail2, self.unavail1, self.unavail2])

    ###########################################################################
    # Copy
    ###########################################################################
    def test_copy_1(self):
        self.assertCopiesAreEqualOf(self.avail1)

    def test_copy_2(self):
        self.assertCopiesAreEqualOf(self.avail2)

    def test_copy_3(self):
        self.assertCopiesAreEqualOf(self.unavail1)

    def test_copy_4(self):
        self.assertCopiesAreEqualOf(self.unavail2)

    ###########################################################################
    # as_dict
    ###########################################################################
    def test_as_simple_dict_1(self):
        self.checkExpect(
            expect={'isAvailable': True, 'reason': ''},
            actual=self.avail1.as_simple_mapping())

    def test_as_simple_dict_2(self):
        self.checkMapping(
            expect={'isAvailable': True, 'reason': ''},
            actual=self.avail2.as_simple_mapping())

    def test_simple_dict_3(self):
        self.checkMapping(
            expect={'isAvailable': False, 'reason': 'foo'},
            actual=self.unavail1.as_simple_mapping())

    def test_simple_dict_4(self):
        self.checkMapping(
            expect={'isAvailable': False, 'reason': 'bar'},
            actual=self.unavail2.as_simple_mapping())
