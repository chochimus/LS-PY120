
def fetch_6th(nums):
    if len(nums) > 5:
        return nums[5]
    else:
        return None
    
def fetch_6th2(nums):
    try:
        return nums[5]
    except IndexError:
        return None
    
numbers = [1, 2, 3, 4, 5]
print(fetch_6th([1, 2, 3, 4, 5]))
print(fetch_6th2([1, 2, 3, 4, 5]))