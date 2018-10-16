import subprocess
from typing import List, Tuple, Union, Sequence


def process(args: Union[bytes, str, Sequence[Union[bytes, str]]])-> Tuple[List[str], List[str]]:

    stdout = []
    stderr = []

    with subprocess.Popen(
            args=args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE) as p, p.stdout as p_stdout, p.stderr as p_stderr:
        def extend():
            stdout.extend(p_stdout.readlines())
            stderr.extend(p_stderr.readlines())

        while p.poll() is None:
            extend()
        extend()
    return stdout, stderr
