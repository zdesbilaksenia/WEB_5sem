class File:
    def __init__(self, id, name, size, extension, id_catalog):
        self.id = id
        self.name = name
        self.size = size
        self.extension = extension
        self.id_catalog = id_catalog

    def full_name(self):
        return f'{self.name}{self.extension}'


class Catalog:
    def __init__(self, id, name, ):
        self.id = id
        self.name = name


class FileCatalog:
    def __init__(self, file_id, catalog_id):
        self.file_id = file_id
        self.catalog_id = catalog_id


files = [
    File(1, 'Реферат', 310, '.docx', 5),
    File(2, 'Фото1', 63, '.png', 2),
    File(3, 'Песня', 46, '.mp3', 4),
    File(4, 'Методичка', 22450, '.pdf', 3),
    File(5, 'Фото2', 78, '.png', 2),
    File(6, 'Отчет', 458, '.docx', 5),
    File(7, 'Фильм', 24780, '.mp4', 1),
    File(8, 'Фото3', 57, '.png', 3),
]

catalogs = [
    Catalog(1, 'Видео'),
    Catalog(2, 'Изображения'),
    Catalog(3, 'Загрузки'),
    Catalog(4, 'Музыка'),
    Catalog(5, 'Документы'),
]

file_catalog = [
    FileCatalog(1, 3),
    FileCatalog(1, 5),
    FileCatalog(2, 1),
    FileCatalog(2, 3),
    FileCatalog(3, 2),
    FileCatalog(4, 3),
    FileCatalog(4, 5),
    FileCatalog(5, 1),
    FileCatalog(5, 3),
    FileCatalog(6, 3),
    FileCatalog(8, 5),
    FileCatalog(8, 1),
]


def main():
    print('Задание Б1')
    res = sorted([(f.name, c.name) for f in
                  files for c in catalogs if c.id == f.id_catalog], key=lambda x: x[0])
    for r in res:
        print(r)

    print('\nЗадание Б2')
    res = sorted({c.name: len(list(filter(lambda x: x.id_catalog == c.id, files))) for c in catalogs}.items(),
                 key=lambda x: x[1],
                 reverse=True)
    for r in res:
        print(r)

    print('\nЗадание Б3')
    res = {f.full_name(): [c.name for c in catalogs if c.id in
                           [f_c.catalog_id for f_c in file_catalog if
                            f_c.file_id == f.id]] for f in files if
           str(f.full_name()).endswith('.png')}.items()
    for r in res:
        print(r)


if __name__ == '__main__':
    main()
