#Find Ratios using Fuzzy logic and Calculate the levenshtein distance similarity ratios between
#the two strings (Sequence).
from fuzzywuzzy import fuzz
s1="I like soft computing"
s2="I like hard computing"
print("FuzzyWuzzy Ratio: ",fuzz.ratio(s1,s2))
print("FuzzyWuzzy PartialRatio: ",fuzz.partial_ratio(s1,s2))
print("FuzzyWuzzy TokenSortRatio: ",fuzz.token_sort_ratio(s1,s2))
print("FuzzyWuzzy TokenSetRatio: ",fuzz.token_set_ratio(s1,s2))
print("FuzzyWuzzy WRatio: ",fuzz.WRatio(s1,s2),'\n\n')