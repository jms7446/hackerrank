
from util.gen_sample import list_to_string, merge_to_lines


def test_list_to_string():
    assert list_to_string([1, 2, 3]) == '1 2 3'
    assert list_to_string([]) == ''
    assert list_to_string([1]) == '1'
    assert list_to_string(['a']) == 'a'


def test_merge_to_lines():
    assert merge_to_lines([
        [1, 2],
        3,
        'a',
        'b\nc'
    ]) == '1 2\n3\na\nb\nc'
