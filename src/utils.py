import json
import os

from .models import Category, Product


def read_json(file: str) -> dict:
    """Функция для чтения json файла."""
    full_file = os.path.abspath(file)
    with open(full_file, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data


def create_objects_from_json(data: dict):
    """Функция для создания объектов из полученных данных"""
    specs = []
    for spec in data:
        products = []
        for product in spec['products']:
            products.append(Product(**product))
        spec['products'] = products
        specs.append(Category(**spec))

    return specs


if __name__ == "__main__":
    raw_data = read_json("data/products.json")
    specs_data = create_objects_from_json(raw_data)
    print(specs_data)
