import pandas as pd
import re
from collections import Counter
try:
    with open(r"C:\Users\Administrator\Desktop\Python Training\Assignments\Milestone-1\Othello.txt",encoding='utfa') as file:
        novdata=file.read()
except FileNotFoundError as e:
    print("No such file present")
words_count_by_charact=re.findall(r"\b[w'-]+\b",novdata)
wordscount=Counter(words_count_by_charact)
print(pd.DataFrame(wordscount.items(),columns=["word","count"]))

