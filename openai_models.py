from enum import Enum, unique

@unique
class OpenAIModels(Enum):
    DAVINCI = "text-davinci-003"
    CURIE = "text-curie-001"
    BABBAGE = "text-babbage-001"
    ADA = "text-ada-001"
    DAVINCI_CODEx = "code-davinci-002"
    CURIE_CODEx = "code-curie-002"

    def __str__(self):
        return self.value