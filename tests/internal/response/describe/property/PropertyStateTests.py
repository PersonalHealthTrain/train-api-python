from tests.base import BaseTest
from pht.internal.response.describe.property import PROPERTY_AVAILABLE, PropertyUnavailable


class PropertyStateTests(BaseTest):

    def setUp(self):
        self.avail1 = PROPERTY_AVAILABLE
        self.avail2 = PROPERTY_AVAILABLE
        self.unavail1 = PropertyUnavailable('foo')
        self.unavail2 = PropertyUnavailable('bar')

    ###########################################################################
    # Type Error
    ###########################################################################
    def test_type_1(self):
        self.assertTypeError(lambda: PropertyUnavailable(True))

    def test_type_2(self):
        self.assertTypeError(lambda: PropertyUnavailable(None))

    def test_type_3(self):
        self.assertTypeError(lambda: PropertyUnavailable({}))

    def test_type_4(self):
        self.assertTypeError(lambda: PropertyUnavailable([]))

    def test_type_5(self):
        self.assertTypeError(lambda: PropertyUnavailable(1))

    def test_type_6(self):
        self.assertTypeError(lambda: PropertyUnavailable(2.4))

    ###########################################################################
    # Equals and hash
    ###########################################################################
    def test_equals_1(self):
        self.assertIsEqual(self.avail1, PROPERTY_AVAILABLE)

    def test_equals_2(self):
        self.assertIsEqual(self.avail2, PROPERTY_AVAILABLE)

    def test_equals_3(self):
        self.assertIsEqual(self.unavail1, PropertyUnavailable('foo'))

    def test_equals_4(self):
        self.assertIsEqual(self.unavail2, PropertyUnavailable('bar'))

    def test_unequal(self):
        self.assertNotEqual(self.avail1, self.unavail1)
        self.assertNotEqual(self.avail1, self.unavail2)
        self.assertNotEqual(self.unavail1, self.unavail2)

    ###########################################################################
    # Copy
    ###########################################################################
    def test_copy_1(self):
        self.assertCopiesAreEqual(self.avail1)

    def test_copy_2(self):
        self.assertCopiesAreEqual(self.avail2)

    def test_copy_3(self):
        self.assertCopiesAreEqual(self.unavail1)

    def test_copy_4(self):
        self.assertCopiesAreEqual(self.unavail2)

    ###########################################################################
    # as_dict
    ###########################################################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={'isAvailable': True, 'reason': None},
            actual=self.avail1.as_dict())

    def test_dict_2(self):
        self.checkExpect(
            expect={'isAvailable': True, 'reason': None},
            actual=self.avail2.as_dict())

    def test_dict_3(self):
        self.checkExpect(
            expect={'isAvailable': False, 'reason': 'foo'},
            actual=self.unavail1.as_dict())

    def test_dict_4(self):
        self.checkExpect(
            expect={'isAvailable': False, 'reason': 'bar'},
            actual=self.unavail2.as_dict())
