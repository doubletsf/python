from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# print(favorite_languages)
# print("Sarah's favorite language is " +
#     favorite_languages['sarah'].title() +
#     ".")
for name, language in favorite_languages.items():
    print(name + "'s favorite language is " +
          language + "."
          )
