import re

#task1
sample1 = "ab aaabbbb acb b"

pat1 = 'ab*'

print(re.findall(pat1, sample1))


#task2

sample2 = "ab aaabbbb acb abb, ab"

pat2 = 'ab{2,3}'

print(re.findall(pat2, sample2))

#task3

sample3 = "abcd_efgh, 12345, ali, oliasdhfg"

pat3 = '[a-z]+_[a-z]+'

print(re.findall(pat3, sample3))

#task4

sample4 = "Somerville, MA 02144, USA"

pat4 = r'\b[A-Z]{1}[a-z]+'

print(re.findall(pat4, sample4))

#task5

sample5 = "a(^&#(@)(b, aaaab, a bbb cccc"

pat5 = r'\ba{1}.*b{1}\b'

print(re.findall(pat5, sample5))


#task6

sample6 = "some text, some text, some text, othertext.ali"

pat6 = r'[.,\s]+'

print(re.sub(pat6, ':', sample6))

#task7

def snake_case_to_camelcase(s):

    return s[0].upper() + re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)[1:]

print(snake_case_to_camelcase('travis_scott_is_awesome'))

#task8
sample8 = "AlikhanLovesMakpalButShesDeserveBetter"

ans = re.split(r'(?=[A-Z])', sample8)

print(ans)

#task9

sample9 = "Some crazyStuff and i need KBTU to be capitaLized"

print(re.sub(r'([a-z])([A-Z])', r'\1 \2', sample9))


#task10

def camel_to_snake(camel_str):
    snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()
    return snake_str

print(camel_to_snake('AlikhanLovesMakpalButShesDeserveBetter'))
