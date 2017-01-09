from handler import handle

def test_vegas_cart_under_40():
    event = dict(
        subtotal = 30,
        city = 'Las Vegas',
        state = 'NV'
    )

    result = handle(event, None)

    assert result['freeShipping'] == False
    assert result['shippingCost'] == 5

def test_vegas_cart_at_40():
    event = dict(
        subtotal = 40,
        city = 'Las Vegas',
        state = 'NV'
    )

    result = handle(event, None)

    assert result['freeShipping'] == True

def test_henderson_cart_under_40():
    event = dict(
        subtotal = 30,
        city = 'Henderson',
        state = 'NV'
    )

    result = handle(event, None)

    assert result['freeShipping'] == False
    assert result['shippingCost'] == 5

def test_henderson_cart_at_40():
    event = dict(
        subtotal = 40,
        city = 'Henderson',
        state = 'NV'
    )

    result = handle(event, None)

    assert result['freeShipping'] == True


def test_boulder_city_cart_under_40():
    event = dict(
        subtotal = 30,
        city = 'Boulder City',
        state = 'NV'
    )

    result = handle(event, None)

    assert result['freeShipping'] == False
    assert result['shippingCost'] == 10

def test_boulder_city_cart_at_40():
    event = dict(
        subtotal = 40,
        city = 'Boulder City',
        state = 'NV'
    )

    result = handle(event, None)

    assert result['freeShipping'] == False
    assert result['shippingCost'] == 10
