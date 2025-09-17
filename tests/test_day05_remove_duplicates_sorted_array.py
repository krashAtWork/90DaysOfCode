import pytest
from problems.day05_remove_duplicates_sorted_array import remove_duplicates, remove_duplicates_v2


# @pytest.mark.parametrize("inp, out", [([1,1,2,3], [1,2,3,"_"]),
#                                      ([1,2,3,4], [1,2,3,4]),
#                                      ([1,2,5,7,7,8], [1,2,5,7,8, "_"]),
#                                      ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4,"_","_","_","_","_"]),
#                                      ])
# def test_remove_duplicates(inp, out):
#     assert remove_duplicates(inp) == out

@pytest.mark.parametrize("inp, out", [([1,1,2,3], [1,2,3,"_"]),
                                     ([1,2,3,4], [1,2,3,4]),
                                     ([1,2,5,7,7,8], [1,2,5,7,8, "_"]),
                                     ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4,"_","_","_","_","_"]),
                                     ])
def test_remove_duplicates(inp, out):
    assert remove_duplicates_v2(inp) == out

    # assert remove_duplicates(inp) == out