try:
    i = 10 / 0
except ZeroDivisionError as e:
    print(e)
    # raise
finally:
    print('1111')
