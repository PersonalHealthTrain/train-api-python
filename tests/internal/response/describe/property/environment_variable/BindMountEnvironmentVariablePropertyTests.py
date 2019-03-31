from unittest.mock import patch
from pht.internal.response.describe.property.environment_variable import bind_mount_by_name
from pht.internal.response.describe.property.environment_variable.BindMountEnvironmentVariableProperty import MountType
from tests.base import BaseTest


class BindMountEnvironmentVariablePropertyTests(BaseTest):

    def setUp(self):
        self.mount1 = bind_mount_by_name('FOO', mount_type=MountType.FILE)
        self.mount2 = bind_mount_by_name('BAR', mount_type=MountType.FILE)
        self.mount3 = bind_mount_by_name('FOO', mount_type=MountType.DIRECTORY)
        self.mount4 = bind_mount_by_name('BAR', mount_type=MountType.DIRECTORY)

    def assert_invalid_env_name(self, name):
        with self.assertRaises(ValueError):
            bind_mount_by_name(name, MountType.FILE)

    ###########################################################
    # TypeError
    ###########################################################
    def test_type_error_1(self):
        self.assertTypeError(lambda: bind_mount_by_name(True, MountType.FILE))

    def test_type_error_2(self):
        self.assertTypeError(lambda: bind_mount_by_name({}, MountType.FILE))

    def test_type_error_3(self):
        self.assertTypeError(lambda: bind_mount_by_name([], MountType.DIRECTORY))

    def test_type_error_4(self):
        self.assertTypeError(lambda: bind_mount_by_name(1, MountType.DIRECTORY))

    def test_type_error_5(self):
        self.assertTypeError(lambda: bind_mount_by_name(0.9661, MountType.FILE))

    ###########################################################
    # Value Error
    ###########################################################
    def test_valid_error_1(self):
        self.assertValueError(lambda: bind_mount_by_name('adaf', MountType.FILE))

    def test_valid_error_2(self):
        self.assertValueError(lambda: bind_mount_by_name(None, MountType.DIRECTORY))

    def test_invalid_environment_variables_1(self):
        self.assert_invalid_env_name("")

    def test_invalid_environment_variables_2(self):
        self.assert_invalid_env_name("_")

    def test_invalid_environment_variables_3(self):
        self.assert_invalid_env_name(" ")

    def test_invalid_environment_variables_4(self):
        self.assert_invalid_env_name("AR_")

    def test_invalid_environment_variables_5(self):
        self.assert_invalid_env_name("sadsf")

    def test_invalid_environment_variables_6(self):
        self.assert_invalid_env_name("_HSGJD")

    def test_invalid_environment_variables_7(self):
        self.assert_invalid_env_name("HSG__JD")

    def test_invalid_environment_variables_8(self):
        self.assert_invalid_env_name(None)

    ###########################################################
    # Equals and not equals
    ###########################################################
    def test_eq_1(self):
        self.assertIsEqual(self.mount1, bind_mount_by_name('FOO', mount_type=MountType.FILE))

    def test_eq_2(self):
        self.assertIsEqual(self.mount2, bind_mount_by_name('BAR', mount_type=MountType.FILE))

    def test_eq_3(self):
        self.assertIsEqual(self.mount3, bind_mount_by_name('FOO', mount_type=MountType.DIRECTORY))

    def test_eq_4(self):
        self.assertIsEqual(self.mount4, bind_mount_by_name('BAR', mount_type=MountType.DIRECTORY))

    def test_unequal(self):
        self.assertUnequalCominationPairs([
            self.mount1, self.mount2, self.mount3, self.mount4])

    ###########################################################
    # Copy
    ###########################################################
    def test_copy_1(self):
        self.assertCopiesAreEqualOf(self.mount1)

    def test_copy_2(self):
        self.assertCopiesAreEqualOf(self.mount2)

    def test_copy_3(self):
        self.assertCopiesAreEqualOf(self.mount3)

    def test_copy_4(self):
        self.assertCopiesAreEqualOf(self.mount4)

    ###########################################################
    # dict
    ###########################################################
    def test_as_simple_dict_1(self):
        self.checkExpect(
            expect={
                'description': '',
                'mountType': 'file',
                'environmentVariableName': 'FOO',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'FOO\' not set'},
                '@type': ['BindMountEnvironmentVariableProperty',
                          'EnvironmentVariableProperty',
                          'Property'],
                '@typeName': 'BindMountEnvironmentVariableProperty',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.mount1.as_simple_mapping())

    def test_as_simple_dict_2(self):
        self.checkExpect(
            expect={
                'description': '',
                'mountType': 'file',
                'environmentVariableName': 'BAR',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'BAR\' not set'},
                '@type': ['BindMountEnvironmentVariableProperty',
                          'EnvironmentVariableProperty',
                          'Property'],
                '@typeName': 'BindMountEnvironmentVariableProperty',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.mount2.as_simple_mapping())

    def test_as_simple_dict_3(self):
        self.checkExpect(
            expect={
                'description': '',
                'mountType': 'directory',
                'environmentVariableName': 'FOO',
                'state': {
                    'isAvailable': False,
                    'reason': "Environment variable 'FOO' not set"
                },
                '@type': ['BindMountEnvironmentVariableProperty',
                          'EnvironmentVariableProperty',
                          'Property'],
                '@typeName': 'BindMountEnvironmentVariableProperty',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.mount3.as_simple_mapping())

    def test_as_simple_dict_4(self):
        self.checkExpect(
            expect={
                'description': '',
                'mountType': 'directory',
                'environmentVariableName': 'BAR',
                'state': {
                    'isAvailable': False,
                    'reason': "Environment variable 'BAR' not set"},
                '@type': ['BindMountEnvironmentVariableProperty',
                          'EnvironmentVariableProperty',
                          'Property'],
                '@typeName': 'BindMountEnvironmentVariableProperty',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.mount4.as_simple_mapping())

    def test_as_simple_dict_5(self):
        with patch.dict('os.environ', {'FOO': 'not a file'}):
            self.checkExpect(
                expect={
                    'description': '',
                    'mountType': 'file',
                    'environmentVariableName': 'FOO',
                    'state': {
                        'isAvailable': False,
                        'reason': 'The value \'not a file\' is not an existing path in the file system'
                    },
                    '@type': ['BindMountEnvironmentVariableProperty',
                              'EnvironmentVariableProperty',
                              'Property'],
                    '@typeName': 'BindMountEnvironmentVariableProperty',
                    "@typeSystem": {
                        'name': 'pythonclass',
                        'version': '1.0'
                    },
                },
                actual=self.mount1.as_simple_mapping())

    @patch.dict('os.environ', {'BAR': 'I am not a file'})
    def test_as_simple_dict_6(self):
        self.checkExpect(
            expect={
                'description': '',
                'mountType': 'file',
                'environmentVariableName': 'BAR',
                'state': {
                    'isAvailable': False,
                    'reason': 'The value \'I am not a file\' is not an existing path in the file system'
                },
                '@type': ['BindMountEnvironmentVariableProperty',
                          'EnvironmentVariableProperty',
                          'Property'],
                '@typeName': 'BindMountEnvironmentVariableProperty',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.mount2.as_simple_mapping())

    @patch.dict('os.environ', {'FOO': 'I am not a directory'})
    def test_as_simple_dict_7(self):
        self.checkExpect(
            expect={
                'description': '',
                'mountType': 'directory',
                'environmentVariableName': 'FOO',
                'state': {
                    'isAvailable': False,
                    'reason': 'The value \'I am not a directory\' is not an existing path in the file system'
                },
                '@type': ['BindMountEnvironmentVariableProperty',
                          'EnvironmentVariableProperty',
                          'Property'],
                '@typeName': 'BindMountEnvironmentVariableProperty',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
                },
            actual=self.mount3.as_simple_mapping())

    @patch.dict('os.environ', {'BAR': 'not a directory'})
    def test_as_simple_dict_8(self):
        self.checkExpect(
            expect={
                'description': '',
                'mountType': 'directory',
                'environmentVariableName': 'BAR',
                'state': {
                    'isAvailable': False,
                    'reason': 'The value \'not a directory\' is not an existing path in the file system'
                },
                '@type': ['BindMountEnvironmentVariableProperty',
                          'EnvironmentVariableProperty',
                          'Property'],
                '@typeName': 'BindMountEnvironmentVariableProperty',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.mount4.as_simple_mapping())

    ###########################################################
    # type
    ###########################################################
    def test_type_1(self):
        self.checkExpect(
            expect=['BindMountEnvironmentVariableProperty',
                    'EnvironmentVariableProperty',
                    'Property'],
            actual=self.mount1.type)

    def test_type_2(self):
        self.checkExpect(
            expect=['BindMountEnvironmentVariableProperty',
                    'EnvironmentVariableProperty',
                    'Property'],
            actual=self.mount2.type)

    def test_type_3(self):
        self.checkExpect(
            expect=['BindMountEnvironmentVariableProperty',
                    'EnvironmentVariableProperty',
                    'Property'],
            actual=self.mount3.type)

    def test_type_4(self):
        self.checkExpect(
            expect=['BindMountEnvironmentVariableProperty',
                    'EnvironmentVariableProperty',
                    'Property'],
            actual=self.mount4.type)

    ###########################################################
    # display
    ###########################################################
    def test_type_name_1(self):
        self.checkExpect(
            expect='BindMountEnvironmentVariableProperty',
            actual=self.mount1.type_name)

    def test_type_name_2(self):
        self.checkExpect(
            expect='BindMountEnvironmentVariableProperty',
            actual=self.mount2.type_name)

    def test_type_name_3(self):
        self.checkExpect(
            expect='BindMountEnvironmentVariableProperty',
            actual=self.mount3.type_name)

    def test_type_name_4(self):
        self.checkExpect(
            expect='BindMountEnvironmentVariableProperty',
            actual=self.mount4.type_name)

    ###########################################################
    # data
    ###########################################################
    def test_data_1(self):
        self.checkExpect(
            expect={
                'mountType': 'file',
                'description': '',
                'environmentVariableName': 'FOO',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'FOO\' not set'}},
            actual=self.mount1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={
                'description': '',
                'mountType': 'file',
                'environmentVariableName': 'BAR',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'BAR\' not set'}},
            actual=self.mount2.data)

    def test_data_3(self):
        self.checkExpect(
            expect={
                'description': '',
                'mountType': 'directory',
                'environmentVariableName': 'FOO',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'FOO\' not set'}},
            actual=self.mount3.data)

    def test_data_4(self):
        self.checkExpect(
            expect={
                'description': '',
                'mountType': 'directory',
                'environmentVariableName': 'BAR',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'BAR\' not set'}},
            actual=self.mount4.data)

    def test_data_5(self):
        with patch.dict('os.environ', {'FOO': 'not a file'}):
            self.checkExpect(
                expect={
                    'description': '',
                    'mountType': 'file',
                    'environmentVariableName': 'FOO',
                    'state': {
                        'isAvailable': False,
                        'reason': 'The value \'not a file\' is not an existing path in the file system'
                    }
                },
                actual=self.mount1.data)

    def test_data_6(self):
        with patch.dict('os.environ', {'BAR': 'not a file'}):
            self.checkExpect(
                expect={
                    'description': '',
                    'mountType': 'file',
                    'environmentVariableName': 'BAR',
                    'state': {
                        'isAvailable': False,
                        'reason': 'The value \'not a file\' is not an existing path in the file system'
                    }
                },
                actual=self.mount2.data)

    def test_data_7(self):
        with patch.dict('os.environ', {'FOO': 'not a directory'}):
            self.checkExpect(
                expect={
                    'description': '',
                    'mountType': 'directory',
                    'environmentVariableName': 'FOO',
                    'state': {
                        'isAvailable': False,
                        'reason': 'The value \'not a directory\' is not an existing path in the file system'
                    }
                },
                actual=self.mount3.data)

    def test_data_8(self):
        with patch.dict('os.environ', {'BAR': 'not a directory'}):
            self.checkExpect(
                expect={
                    'description': '',
                    'mountType': 'directory',
                    'environmentVariableName': 'BAR',
                    'state': {
                        'isAvailable': False,
                        'reason': 'The value \'not a directory\' is not an existing path in the file system'
                    }
                },
                actual=self.mount4.data)

    ###########################################################
    # is available
    ###########################################################
    @patch.dict('os.environ', {'FOO': 'value'})
    def test_is_available_11(self):
        self.assertFalse(self.mount1.is_available())

    def test_is_available_12(self):
        self.assertFalse(self.mount1.is_available())

    @patch.dict('os.environ', {'BAR': 'value'})
    def test_is_available_21(self):
        self.assertFalse(self.mount2.is_available())

    def test_is_available_22(self):
        self.assertFalse(self.mount2.is_available())

    @patch.dict('os.environ', {'FOO': 'value'})
    def test_is_available_31(self):
        self.assertFalse(self.mount3.is_available())

    def test_is_available_32(self):
        self.assertFalse(self.mount3.is_available())

    @patch.dict('os.environ', {'BAR': 'value'})
    def test_is_available_41(self):
        self.assertFalse(self.mount4.is_available())

    def test_is_available_42(self):
        self.assertFalse(self.mount4.is_available())


    ###########################################################
    # __str__
    ###########################################################
    def test_str_1(self):
        self.checkExpect(
            expect='BindMount[name=FOO,mountType=file]',
            actual=str(self.mount1))

    def test_str_2(self):
        self.checkExpect(
            expect='BindMount[name=BAR,mountType=file]',
            actual=str(self.mount2))

    def test_str_3(self):
        self.checkExpect(
            expect='BindMount[name=FOO,mountType=directory]',
            actual=str(self.mount3))

    def test_str_4(self):
        self.checkExpect(
            expect='BindMount[name=BAR,mountType=directory]',
            actual=str(self.mount4))

    ###########################################################
    # __repr__
    ###########################################################
    def test_repr_1(self):
        self.checkExpect(
            expect='BindMount[name=FOO,mountType=file]',
            actual=repr(self.mount1))

    def test_repr_2(self):
        self.checkExpect(
            expect='BindMount[name=BAR,mountType=file]',
            actual=repr(self.mount2))

    def test_repr_3(self):
        self.checkExpect(
            expect='BindMount[name=FOO,mountType=directory]',
            actual=repr(self.mount3))

    def test_repr_4(self):
        self.checkExpect(
            expect='BindMount[name=BAR,mountType=directory]',
            actual=repr(self.mount4))

    ###########################################################
    # get_value
    ###########################################################
    def test_get_value_1(self):
        with patch.dict('os.environ', {'FOO': 'value1'}):
            self.checkExpect(
                expect='value1',
                actual=self.mount1.get_value())

    def test_get_value_2(self):
        with patch.dict('os.environ', {'BAR': ''}):
            self.checkExpect(
                expect='',
                actual=self.mount2.get_value())

    def test_get_value_3(self):
        with self.assertRaises(KeyError):
            self.checkExpect(
                expect='',
                actual=self.mount3.get_value())

    def test_get_value_4(self):
        with self.assertRaises(KeyError):
            self.checkExpect(
                expect='',
                actual=self.mount4.get_value())
