from src.word_count import mapper, reducer, shuffler, splitter


def test_map_reduce_naive(mock_input_data):
    splitter_result = splitter(text=mock_input_data)
    mapping_result = mapper(splitted_data=splitter_result)
    shuffling_result = shuffler(mapped_data=mapping_result)
    reducer_result = reducer(shuffled_data=shuffling_result)
    assert reducer_result == [
        ("dante", 2),
        ("nel", 1),
        ("mezzo", 1),
        ("del", 1),
        ("cammin", 1),
        ("di", 1),
        ("nostra", 1),
        ("vita", 1),
    ]
