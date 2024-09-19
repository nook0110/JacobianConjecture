from aenum import Enum, NoAlias

class CheckResult(Enum):
    _settings_ = NoAlias
    HOLDS = True
    NOT_HOLDS = False
    NON_GENERAL_POSITION = True
    CONTRACTS = True