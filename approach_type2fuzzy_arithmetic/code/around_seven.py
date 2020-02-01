from type2fuzzy import GeneralType2FuzzySet

around_seven_def = '''(1.0/0.3 + 0.5/0.4) /6+
						(1.0/1.0 ) /7+
						(1.0/0.3 + 0.5/0.4) /8'''

around_seven = GeneralType2FuzzySet.from_representation(around_seven_def)

print(around_seven)

around_seven_embedded = around_seven.embedded_type2_sets()

for embedded in around_seven_embedded:
	print(embedded)
