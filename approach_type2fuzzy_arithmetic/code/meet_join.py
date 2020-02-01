from type2fuzzy import GeneralType2FuzzySet

a_def = '''(0.5/0 + 0.7/0.1 + 0.3/0.2)/1'''
# b_def = '''(0.9/0.1 + 0.7/0.2 + 0.6/0.3)/1'''
b_def = '''(0/0)/1'''

a = GeneralType2FuzzySet.from_representation(a_def)
b = GeneralType2FuzzySet.from_representation(b_def)

c = a.join(b)

print(c)