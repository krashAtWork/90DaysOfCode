import pytest
from problems.day07_move_zeros_2_end import move_0s_to_end

@pytest.mark.parametrize("inp, out",[([0],[0]),
                                     ([0,1,0,3,12], [1,3,12,0,0])])
def test1(inp, out):
    assert move_0s_to_end(inp) ==  out

