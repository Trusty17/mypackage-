from mypackage import myModule

def test_top_n():
    """
    make sure top_n works correctly 
    """

    assert myModule.top_n([8,3,2,4,5,7], 3) == [8,7,5], 'incorrect'
    assert myModule.top_n([9,2,12,10], 2) == [12,10], 'incorrect'
    assert myModule.top_n([1,2,3,4,5], 5) == [1,2,3,4,5], 'incorrect'