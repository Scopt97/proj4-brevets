from acp_times import open_time, close_time
import arrow


base_time = arrow.get("2018-01-01T00:00:00")

def test_basic():
    print(open_time(100, 200, base_time.isoformat()))
    print(base_time.shift(hours=+2, minutes=+56).isoformat())
    print(base_time.isoformat())
    #assert open_time(100, 200, arrow.now().isoformat()) == arrow.now().shift(hours=+2, minutes=+56).isoformat()
    #assert clsoe_time(100, 200, arrow.now().isoformat()) == arrow.now().shift(hours=+6, munutes=+40).isoformat()
    open_test = open_time(100, 200, base_time.isoformat())
    open_actual = base_time.shift(hours=+2, minutes=+56).isoformat()
    close_test =  close_time(100, 200, base_time.isoformat())
    close_actual = base_time.shift(hours=+6, minutes=+40).isoformat()

    assert open_test == open_actual
    assert close_test == close_actual

def test_bound():
    #assert open_time(200, 200, arrow.now().isoformat()) == arrow.now().shift(hours=+5, minutes=+53).isoformat()
    #assert clsoe_time(200, 200, arrow.now().isoformat()) == arrow.now().shift(hours=+13, munutes=+30).isoformat()
    open_test = open_time(200, 200, base_time.isoformat())
    open_actual = base_time.shift(hours=+5, minutes=+53).isoformat()
    close_test = close_time(200, 200, base_time.isoformat())
    close_actual = base_time.shift(hours=+13, minutes=+30).isoformat()

    print(open_test)
    print(open_actual)

    assert open_test == open_actual
    assert close_test == close_actual

def test_extension():
    #assert open_time(240, 200, arrow.now().isoformat()) == arrow.now().shift(hours=+5, minutes=+53).isoformat()
    #assert clsoe_time(240, 200, arrow.now().isoformat()) == arrow.now().shift(hours=+13, munutes=+30).isoformat()
    open_test = open_time(240, 200, base_time.isoformat())
    open_actual = base_time.shift(hours=+5, minutes=+53).isoformat()
    close_test = close_time(240, 200, base_time.isoformat())
    close_actual = base_time.shift(hours=13, minutes=+30).isoformat()

    print(open_test)
    print(open_actual)
    print(close_test)
    print(close_actual)

    assert open_test == open_actual
    assert close_test == close_actual
