# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    line=re.sub(r'\ba+\b',r"argh",line,count=1, flags=re.IGNORECASE)
    print(line)