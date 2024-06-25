import os
from concurrent.futures import ThreadPoolExecutor
import logging

# Настройка логирования
logging.basicConfig(filename='file_removal.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


def search_files(ip):
    share_path = f'\\\\{ip}\\c$\\files'

    if not os.path.exists(share_path):
        logging.warning(f'Путь {share_path} не существует или компьютер недоступен.')
        return

    for root, dirs, files in os.walk(share_path):
        for file in files:
            if file.startswith('log-test'):
                file_path = os.path.join(root, file)
                logging.info(f'Удаляем файл: {file_path}')
                try:
                    os.remove(file_path)
                except OSError as e:
                    logging.error(f'Не удалось удалить файл: {file_path}, ошибка: {e}')
    logging.info(f'Успешно проверили и сделали: {ip}')


def main():
    with open('ips.txt', 'r') as file:
        ips = file.readlines()
        ips = [line.strip() for line in ips]
    logging.info(f'IP-адреса для обработки: {ips}')

    # Создаем ThreadPoolExecutor с 4-мя потоками (можно изменить число потоков)
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Запускаем задачи и получаем результаты
        executor.map(search_files, ips)


if __name__ == '__main__':
    main()
