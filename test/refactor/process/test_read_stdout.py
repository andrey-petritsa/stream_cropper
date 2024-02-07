import subprocess
import unittest


class TestReadStdout(unittest.TestCase):
    cycle_run_process = ['python3', '/Users/acrosspaper/code/repository/my/StreamCropper/test/component/utils/additional/process/always_run_process.py']
    error_throw_process = ['python3', '/Users/acrosspaper/code/repository/my/StreamCropper/test/component/utils/additional/process/error_throw_process.py']

    def test_run(self):
        result = subprocess.run(self.cycle_run_process, stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))

    def test_poll(self):
        proc = subprocess.Popen(['sleep', '30'])
        print(proc.poll())

    def test_communicate(self):
        cmd = ['ls', '-Rla', '/tmp']
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        stdout, stderr = proc.communicate()
        print(stdout)

    def test_read_stdout(self):
        proc = subprocess.Popen(self.cycle_run_process, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        while(True):
            line = proc.stdout.readline()
            print(line)
            if not line:
                break

    def test_read_stderr(self):
        proc = subprocess.Popen(self.error_throw_process, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        stdout = proc.stdout.read()
        stderror = proc.stderr.read()
        print(stdout)
        print(stderror)
        print(proc.poll())
