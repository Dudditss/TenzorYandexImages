from YandexPages import ImagesHelper


def test_yandex_search(browser):
    # Запускаем тест
    yandex_main_page = ImagesHelper(browser)
    yandex_main_page.go_to_site()

    # Проверка на наличие Картинок на панели навигации и открытие ссылки на Картинки
    elements = yandex_main_page.check_navigation_bar()
    assert 'Картинки' in elements

    # Переключились на другое окно и сделали его активным
    yandex_main_page.new_window()

    # Убедились в правильном переходе по ссылке
    assert 'https://yandex.ru/images/' in yandex_main_page.current_url()

    # Открываем первую категорию картинок и сразу сравниваем с полем ввода
    assert yandex_main_page.images_bar() == yandex_main_page.search()

    # Открываем первую картинку в категории и фиксируем ее в качестве элемента
    yandex_main_page.images_result()
    image_first = yandex_main_page.mini_images()

    # Переходим к следующей картинке и фиксируем ее в качестве элемента
    yandex_main_page.button_next_click()
    image_second = yandex_main_page.mini_images()

    # Сравниваем первую и вторую картинку, убеждаемся что они отличаются
    assert image_first is not image_second

    # Возвращаемся назад к первой картинке и фиксируем ее в качестве элемента
    yandex_main_page.button_prev_click()
    image_third = yandex_main_page.mini_images()

    # Сравниваем итоговую и изначальную картинку, убеждаемся что это одна и та же
    assert image_third == image_first
