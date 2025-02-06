from ..utils import get_exe_version


class DenoWrapper:
    @staticmethod
    def _version():
        return get_exe_version('deno', ['-v'], version_re=r'deno\s+([0-9.]+)')

    def __init__(self, extractor, required_version=None, timeout=10000):
        pass
