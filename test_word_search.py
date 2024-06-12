from word_search import search_words

def test_search_words():
    mask = '????т'
    excluded_letters = 'роаин'
    required_letters = 'текс'
    
    expected_result = ['скейт', 'скепт', 'текст']
    
    assert search_words(mask, excluded_letters, required_letters) == expected_result
