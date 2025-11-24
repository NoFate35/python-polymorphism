# BEGIN (write your solution here)
def swap_key_value(data):
    iter_data = data.to_dict()

    for key in iter_data:
        data.unset_(key)
    
    for key, value in iter_data.items():
        data.set_(value, key)
    
# END
