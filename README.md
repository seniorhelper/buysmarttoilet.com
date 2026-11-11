# buysmarttoilet.com (static, replaces the Shopify store "My Store")
Build: `python -I _src/build.py <products.json>`. Product data comes from the Shopify export in
`_overnight-reports/shopify-exports/buysmarttoilet.com-products.json`. Product pages keep the
old Shopify paths (/products/<handle>/), so old links keep working. No checkout: buttons open the
quote form (/pages/contact/), which posts through assets/lead-send.js to the Eye To Ad lead server.
Images are still served from cdn.shopify.com; copy them into /assets/img before the store is closed.
