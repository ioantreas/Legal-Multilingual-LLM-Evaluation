from datasets import load_dataset

class Dataset:
    """
    Base Dataset class with a factory method to return the appropriate dataset object.
    """

    def get_data(self, language):
        """
        Abstract method to get data in a specific language.
        This should be implemented by child classes.
        """
        raise NotImplementedError("Child class must implement this method")

    @staticmethod
    def get_dataset(name):
        """
        :param name: name of the dataset
        :return: the dataset object
        """
        if name.lower() == 'multi_eurlex':
            return Multi_Eurlex()
        else:
            raise ValueError(f"Dataset '{name}' is not available")


class Multi_Eurlex(Dataset):
    """
    Child class of Dataset representing the Multi-EUR-Lex dataset.
    """
    def __init__(self):
        self.label_options = [
            "POLITICS", "INTERNATIONAL RELATIONS", "EUROPEAN UNION", "LAW", "ECONOMICS",
            "TRADE", "FINANCE", "SOCIAL QUESTIONS", "EDUCATION AND COMMUNICATIONS", "SCIENCE",
            "BUSINESS AND COMPETITION", "EMPLOYMENT AND WORKING CONDITIONS", "TRANSPORT",
            "ENVIRONMENT", "AGRICULTURE, FORESTRY AND FISHERIES", "AGRI-FOODSTUFFS",
            "PRODUCTION, TECHNOLOGY AND RESEARCH", "ENERGY", "INDUSTRY", "GEOGRAPHY",
            "INTERNATIONAL ORGANISATIONS"
        ]

    def get_data(self, language):
        """
        :param language: the language for which data should be retrieved
        :return: the data corresponding to the language parameter
        """
        dataset = load_dataset('multi_eurlex', language, split='test')
        data = []
        if language == 'all_languages':
            data = self.extract_text_all_languages(dataset)
        else:
            data = self.extract_text(dataset)
        return data, self.label_options

    def extract_text_all_languages(self, dataset):
        """
        :param dataset: the dataset containing the text data
        :return: a list of text data from all languages
        """
        data = []
        for item in dataset:
            documents = item['text']
            texts = documents.keys()
            data.append({"text:": text, "labels": item['labels']} for text in texts)
    def extract_text(self, dataset):
        """
        :param dataset: the dataset containing the text data
        :return: a list of text data in the specified language
        """
        data = []
        for item in dataset:
            data.append({"text": item['text'], "labels": item['labels']})
        return data