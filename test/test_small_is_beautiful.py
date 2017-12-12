from test_project.small_is_beautiful import what_a_wonderful_world


def test_world_is_working_wonderfully():
    a = what_a_wonderful_world()
    assert sum(a) == 0
