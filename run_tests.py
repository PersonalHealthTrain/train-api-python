import unittest
import os
import re

SPACES_FRONT = re.compile(r'^[ ]*')
TEST_METHOD = re.compile(r'^\s*def\s+test_')


def indent_of(line: str):
    return len(SPACES_FRONT.match(line.replace('\t', ' ' * 4))[0])


def is_test_method(method_line):
    return TEST_METHOD.match(method_line) is not None


def list_rows_of_test_functions(dirname):
    python_files = (os.path.join(root, file_name)
                    for root, _, files in os.walk(dirname)
                    for file_name in files
                    if file_name.endswith('py'))
    result = []

    def record_method(file_name, method_name, line_count):
        if method_name is not None:
            result.append((file_name, method_name, line_count))

    for python_file in python_files:
        with open(python_file, 'r') as f:
            test_method_indent = None
            method_name = None
            line_count = 0
            for line in f:
                indent = indent_of(line)
                line = line.strip()
                # New method
                if is_test_method(line):
                    test_method_indent = indent + 4
                    method_name = line
                    line_count = 0
                # End of method
                elif method_name is not None and indent < test_method_indent:
                    record_method(python_file, method_name, line_count)
                    method_name = None
                    test_method_indent = None
                # In method
                elif indent == test_method_indent:
                    line_count += 1
            record_method(python_file, method_name, line_count)
    return result


def assert_that_test_methods_have_only_one_line(skip_files=None):
    if skip_files is None:
        skip_files = set()
    else:
        skip_files = set(skip_files)

    def too_many_lines(row):
        return row[2] > 1
    rows = [row for row in list_rows_of_test_functions('tests') if os.path.basename(row[0]) not in skip_files]
    total_violations = sum(too_many_lines(row) for row in rows)
    for row in rows:
        nlines = row[2]
        if too_many_lines(row):
            raise AssertionError(
                'Method {} in file {} has {} line, not 1. Total violations: {}'.format(
                    row[1], row[0], nlines, total_violations))


if __name__ == '__main__':
    assert_that_test_methods_have_only_one_line(skip_files=['builder.py'])
    unittest.main('tests')
