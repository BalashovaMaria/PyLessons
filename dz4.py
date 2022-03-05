#6
import math, statistics

def my_log(spisokchisla: list) -> list:
    return [math.log(x) if x > 0 else None for x in spisokchisla]


print(my_log([1, 3, 2.5, -1, 9, 0, 2.71]))


#17
import math, statistics

spisok = [1, -100, 10, 50, 56, 7, 0]
minimum = spisok.index(min(spisok))
maximum = spisok.index(max(spisok))
if (maximum > minimum):
    print(statistics.mean(spisok[minimum + 1: maximum]))
else:
    print(spisok[:maximum + 1] + [statistics.median(spisok[maximum + 1: minimum])
                                for x in range(maximum + 1, minimum)] + spisok[minimum])
    
#19
import math, statistics

spisok=[1, 5, 6.3, 6, None, 2.0, -4, None]
srednee = statistics.mean([x for x in spisok if (x != None)])
print(list(map(lambda x: x if (x != None) else srednee, spisok)))
