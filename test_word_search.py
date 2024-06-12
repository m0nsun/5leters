from word_search import search_words

def test_search_words():
    mask = '????т'
    excluded_letters = 'кроаеин'
    required_letters = 'слт'
    
    expected_result = ['текст']
    
    assert search_words(mask, excluded_letters, required_letters) == expected_result