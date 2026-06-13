class InvalidCouponCodeError(Exception):
    pass


def apply_coupon(code):
    valid_codes = ["SAVE10", "WELCOME20", "FLAT50"]

    try:
        if code not in valid_codes:
            raise InvalidCouponCodeError("Invalid Coupon Code!")
        else:
            print("Coupon Applied Successfully!")

    except InvalidCouponCodeError as e:
        print(e)

apply_coupon("SAVE10")
apply_coupon("ABC123")