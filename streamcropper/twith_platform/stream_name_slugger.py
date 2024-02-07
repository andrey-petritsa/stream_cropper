import re


class StreamNameSlugger:
    def __init(self):
        pass

    def slug(self, stream_name):
        name_without_bad_symbols = re.sub("[^ А-Яа-я0-9A-Za-z]", "", stream_name)
        name_without_space = name_without_bad_symbols.replace(" ", "_")
        return name_without_space
