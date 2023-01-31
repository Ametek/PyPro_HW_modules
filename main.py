from application.salary import calculate_salary
import application.db.people
from datetime import datetime
# from coordinates.converter import CoordinateConverter as conv, WGS84


def main():
    today = datetime.today()  # Получаем текущую дату
    data = '{}.{}.{}'.format(today.day, today.month, today.year)  # Преобразуем в удобоваримый формат
    print(f'Сегодня {data}. Вызываем функции из пакетов:')
    calculate_salary()  # Вызываем функцию. Пробуем разный импорт
    application.db.people.get_employees()  # Вызываем функцию. Пробуем разный импорт
    print('\nПробуем импортированный конвертер координат:')
    # wgs_point = WGS84(lat=59.39528, long=24.66410)  # координаты в формате WGS84
    # print(conv.wgs84_to_l_est97(wgs_point))  # Конвертируем в формат L-Est97 и выводим
    print('Работает, но ругается на несогласованные форматы координат. Поэтому закомментирован')


if __name__ == '__main__':
    main()
