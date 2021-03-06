import enum


class TicketStatus(enum.IntEnum):
    ToDo = 1
    InProgress = 2
    Done = 3

    @classmethod
    def get_choices(cls):
        return tuple((x.value, x.name) for x in cls)


class SkillTags(enum.IntEnum):
    JavaScript = 1
    Python = 2
    c = 3
    cpp = 4

    @classmethod
    def get_choices(cls):
        return tuple((x.value, x.name) for x in cls)
