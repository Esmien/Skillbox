alphabet = 'abcdefg'
result = {1: alphabet[:],
          2: alphabet[::-1],
          3: alphabet[::2],
          4: alphabet[1::2],
          5: alphabet[:1],
          6: alphabet[-1:-2:-1],
          7: alphabet[3:4],
          8: alphabet[-3:],
          9: alphabet[3:5],
          10: alphabet[4:2:-1],
           }
for key, value in result.items():
    print(f'{key}: {value}')