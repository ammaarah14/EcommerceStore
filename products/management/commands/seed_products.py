from decimal import Decimal

from django.core.management.base import BaseCommand

from products.models import Product

# Edit names, descriptions, prices (in Rand) and stock here. Existing products
# (matched by name) are left untouched, so edits made in /admin/ are kept.
PRODUCTS = [
    ("Insulated Water Bottle", "Matte black stainless steel bottle with a carry handle. Keeps drinks cold or hot all day.", "349.00", 40, "products/163abcdd-b6ac-4ecd-a868-ca1223914b93.png"),
    ("Hardcover Notebook", "Black hardcover notebook with an elastic closure and ribbon bookmark.", "159.00", 60, "products/ChatGPT_Image_Sep_20_2026_06_26_06_PM.png"),
    ("Gel Pen 0.5", "Smooth-writing 0.5mm black gel pen with a comfortable rubber grip.", "29.00", 200, "products/ChatGPT_Image_Sep_20_2026_06_27_43_PM.png"),
    ("Everyday Backpack", "Lightweight black backpack with a padded back, front pocket and room for a laptop.", "699.00", 25, "products/ChatGPT_Image_Sep_20_2026_06_28_44_PM.png"),
    ("Wireless Headphones", "White over-ear Bluetooth headphones with soft cushioned ear cups.", "1299.00", 15, "products/ChatGPT_Image_Sep_20_2026_06_30_45_PM.png"),
    ("Aluminium Laptop Stand", "Sturdy ergonomic aluminium stand that raises your laptop to eye level.", "499.00", 30, "products/ChatGPT_Image_Sep_20_2026_06_31_58_PM.png"),
]


class Command(BaseCommand):
    help = "Create the starter products if they don't exist yet."

    def handle(self, *args, **options):
        created = 0
        for name, desc, price, stock, image in PRODUCTS:
            _, was_created = Product.objects.get_or_create(
                name=name,
                defaults={
                    "description": desc,
                    "price": Decimal(price),
                    "stock": stock,
                    "image": image,
                },
            )
            created += was_created
        self.stdout.write(self.style.SUCCESS(f"Seeded {created} new product(s)."))
