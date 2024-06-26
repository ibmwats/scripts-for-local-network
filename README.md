# Различные скрипты для локальной сети

## Массовое удаление файлов на компьютерах локальной сети Windows с Python по маске

Сам скрипт: mass_deletion_of_files_on_the_network_by_mask.py

### Входные данные:

* **ips.txt** - содержит список IP адресов или DNS имена устройств, на которых требуется удалить
* **share_path** - путь, где хранятся файлы, не забываем про экранирование символов
* **file.startswith('log-test')** - маска для удаления файлов. Указывается, с чего начинается имя файла. Можно также
  использовать file.endswith('name_file'), чтобы указывать, чем заканчивается имя файла.

### Логирование:

Скрипт ведет логирование работы в файл file_removal.log. В логе сохраняется информация о процессе удаления, а
также ошибки, возникшие при выполнении.