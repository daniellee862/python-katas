def create_counter(base_num):
    def increment():
        nonlocal base_num
        base_num += 1
        return base_num

    def decrement():
        nonlocal base_num
        base_num -= 1
        return base_num

    return {
        'up': increment,
        'down': decrement
    }
