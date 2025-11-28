def get_inverse(nums):
    inverses = []
    for num in nums:
        try:
            inverses.append(1 / num)
        except ZeroDivisionError as e:
            print(f'{e.__class__.__name__}: {e}')
        except TypeError as e:
            print(f'{e.__class__.__name__}: {e}')
   
    return inverses
    
print(get_inverse([1,2,3,4]))
print(get_inverse(['a']))
print(get_inverse([0,1,2]))