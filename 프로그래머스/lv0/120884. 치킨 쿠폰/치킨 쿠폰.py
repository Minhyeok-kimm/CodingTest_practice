def solution(chicken):
    my_coupon = int(chicken)
    service = 0
    while True:
        if my_coupon >= 10:
            service_order = my_coupon // 10
            my_coupon -= service_order * 10
            service += service_order
            my_coupon += service_order
        else:
            break
    return service