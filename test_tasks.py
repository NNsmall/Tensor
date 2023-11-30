import task_1, task_2, task_3


def test_task_1_force_in_people():
    assert task_1.force_in_people == "Сила в людях"
    print(' Блок "Сила в людях" присутствует на странице')


def test_task_1_url():
    assert task_1.url == "https://tensor.ru/about"
    print(' Ссылка "Подробнее" открывается успешно.', task_1.url)


def test_task_1_images():
    assert task_1.list_images[0] == task_1.list_images[1] == task_1.list_images[2] ==task_1.list_images[3]
    print(" Размер картинок одинаковый.")


def test_task_2_region_yar():
    assert task_2.region_yar == "Ярославская обл."
    print(f" Определился ваш регион {task_2.region_yar}")


def test_task_2_list_partners_yar():
    assert len(task_2.list_partners_yar) > 0
    print(f" Cписок парнеров найден. {task_2.list_partners_yar}")


def test_task_2_list_region_kam():
    assert task_2.region_kam == "Камчатский край"
    print(f" Определился регион {task_2.region_kam}")


def test_task_2_list_change_of_region():
    assert task_2.list_partners_yar != task_2.list_partners_kam
    print(f" Список партнеров изменился. {task_2.list_partners_kam}")


def test_task_2_list_title_url():
    assert task_2.region_kam in task_2.title
    print(f" {task_2.region_kam} есть в title. URL:", task_2.url)


def test_task_3_download_file():
    assert task_3.check_for_file_existence == True
    print(" Плагин скачан успешно.")


def test_task_3_compare_files():
    assert task_3.size_link_file == task_3.size_load_file
    print(f" Скачанный файл совпадает с указанным размером на сайте ({task_3.size_link_file} МБ).")