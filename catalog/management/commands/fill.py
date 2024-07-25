from django.core.management import BaseCommand
from catalog.models import Product, Category
from django.db import connection
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog_data.json', 'r', encoding='utf-8') as file:
            data_categories = json.load(file)
        return data_categories

    @staticmethod
    def json_read_products():
        with open('catalog_data.json', 'r', encoding='utf-8') as file:
            data_products = json.load(file)
        return data_products

    def handle(self, *args, **kwargs):
        with connection.cursor() as cur:
            cur.execute("TRUNCATE TABLE catalog_category, catalog_product RESTART IDENTITY;")
        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            if category["model"] == "catalog.category":
                category_for_create.append(Category(id=category["pk"], name=category["fields"]["name"]))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            if product["model"] == "catalog.product":
                product_for_create.append(
                    Product(id=product["pk"], name=product["fields"]["name"],
                            category=Category.objects.get(pk=product["fields"]["category"]),
                            price=product["fields"]["price"]))

        Product.objects.bulk_create(product_for_create)
