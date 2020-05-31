select selling_price, storage_cost, purchase_price
from price
where store_id = {store_id} and product_code = {product_code};