import json
import subprocess


class StreamlinkCheckOnlineStrategy():
    def check_is_online(self, platform_name, stream_reference):
        cmd = f'streamlink --force --json --stream-url {platform_name}/{stream_reference}'
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = process.communicate()

        decoded_stderr = stderr.decode('ascii')
        if decoded_stderr != "":
            raise Exception(decoded_stderr)


        decoded_stdout = stdout.decode('ascii')
        dict_stdout = json.loads(decoded_stdout)

        if "streams" in dict_stdout:
            return True

        return False


