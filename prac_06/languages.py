"""CP1404/CP5632 Practical - Programming language"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    print(languages)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic() is True:
            print(language.field)


if __name__ == '__main__':
    main()
