from PythonPractice.enums.enums import LanguageEnum


# Switch Case Demonstration. Python don't have switches so if, elif, else like are used
# Some Modern versions used Match Case
class Switch:

    def __init__(self, bootcamp_languages):
        self.bootcamp_languages = bootcamp_languages

    def lang_matcher(self):
        language = input('Enter your favorite Language: ')

        if language == LanguageEnum.JS.value:
            filtered_bootcamp = list(filter(lambda lang: lang['language'] == LanguageEnum.JS.value, self.bootcamp_languages))
            return filtered_bootcamp

        elif language == LanguageEnum.JAVA.value:
            filtered_bootcamp = list(
                filter(lambda lang: lang['language'] == LanguageEnum.JAVA.value, self.bootcamp_languages))
            return filtered_bootcamp

        elif language == LanguageEnum.GO.value:
            filtered_bootcamp = list(filter(lambda lang: lang['language'] == LanguageEnum.GO.value, self.bootcamp_languages))
            return filtered_bootcamp

        elif language == LanguageEnum.PHP.value:
            filtered_bootcamp = list(filter(lambda lang: lang['language'] == LanguageEnum.PHP.value, self.bootcamp_languages))
            return filtered_bootcamp
        else:
            return 'NONE OF YOU DESIRED LANGUAGE FOUND IN OUR DATABASE'
