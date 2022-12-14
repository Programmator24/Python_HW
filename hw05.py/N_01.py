# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


print(' '.join(filter(lambda x: not 'abc' in x, 'abc adr tgd'.split())))
