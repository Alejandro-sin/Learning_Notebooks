#■■■■■■■■■■■■■■■■■■■■■■■■■■■ REVIEW CHAPTER.
print("Practice everything")
print('You\'d need to know\'s bout escapes with\\that do:')
print('\n newlines and \t tabs.')

poem ="""
\t The lovely worl with logic so firmly panted cannot discern \n the needs of love
nor comprehend passion from intuition and requires an explanation\n\t twhere there is none
"""
print("■■■■■■■■■■■■■■■")
print(poem)
print("■■■■■■■■■■■■■■■")

def secret_formula (started):
    jelly = started*320
    jars = jelly/1000
    crates = jars/3
    return jelly, jars, crates


st = 1000
jacinto,jars,crates = secret_formula(st)

print("With a starting point of: {}".format(st))
print(f'jelly: {jacinto}, jars: {jars},crates:{crates}')


formula =secret_formula(st)
print(type(formula))
print('jelly: {}, jars: {},crates:{}'.format(*formula))