def main():
    player_first = [*map(int, input().split())]
    player_second = [*map(int, input().split())]
    front_first, tail_first = 0, len(player_first)
    front_second, tail_second = 0, len(player_first)
    step = 0
    while step < 10 ** 6:
        if front_second == tail_second:
            return 'first', step
        if front_first == tail_first:
            return 'second', step
        cart_first = player_first[front_first]
        cart_second = player_second[front_second]
        swap = False
        if cart_first == 0 and cart_second == 9 or cart_first == 9 and cart_second == 0:
            cart_first, cart_second = cart_second, cart_first
            swap = True
        if cart_first > cart_second:
            if swap:
                cart_first, cart_second = cart_second, cart_first
            player_first.append(cart_first)
            player_first.append(cart_second)
            tail_first += 2
        else:
            if swap:
                cart_first, cart_second = cart_second, cart_first
            player_second.append(cart_first)
            player_second.append(cart_second)
            tail_second += 2
        front_second += 1
        front_first += 1
        step += 1
    return ('botva',)


print(*main())
