from aenum import Enum, NoAlias

class CheckResult(Enum):
    _settings_ = NoAlias
    NOT_HOLDS = False
    HOLDS = True
    NON_GENERAL_POSITION = True
    CONTRACTS = True