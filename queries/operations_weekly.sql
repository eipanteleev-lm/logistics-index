select * from operations_weekly
where store_id = {store_id} and product_code = {product_code}
order by created;