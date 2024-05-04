from selene import browser, be, have


def test_solenya_google_search():
    browser.open("https://google.ru")
    browser.element('[name="q"]').should(be.blank).type('Купить соленья').press_enter()
    browser.element('#search').should(have.text('Неурожайный год мог принести в дома голод, поэтому '
                                                'соленья и заготовки всегда выручали и выручают по сей день'))


def test_solenya_google_search_negative():
    browser.open("https://google.ru")
    browser.element('[name="q"]').should(be.blank).type('Купить соленья').press_enter()
    browser.element('#search').should(have.no.text('Неурожайный год мог принести в дома голод, а мог и не принести'))


def test_solenya_yandex_search():
    browser.open("https://ya.ru")
    browser.element('[name="text"]').should(be.blank).type('Купить соленья').press_enter()
    browser.element('#search-result').should(have.text('Соленья - это полезный и вкусный продукт, '
                                                       'который можно купить в интернет магазине'))


def test_solenya_yandex_search_negative():
    browser.open("https://ya.ru")
    browser.element('[name="text"]').should(be.blank).type('Купить соленья').press_enter()
    browser.element('#search-result').should(have.no.text('Соленья - это полезный и вкусный продукт, который '
                                                          'можно купить, а можно и не купить'))
