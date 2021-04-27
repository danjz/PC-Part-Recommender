import json

def export_html(parts, items, num_of_items):
    f = open('data.html', 'w')

    html_start = '''
<!DOCTYPE html>
<html>
   <div itemscope itemtype="https://schema.org/ItemList">
   <span itemprop="name">Recommended component list</span>
   <div itemprop="description">A list containing the recommended computer components for the user's preferences</div>
   <div> <link itemprop="itemListOrder" href="http://schema.org/ItemListUnordered">List is unordered</div>
   <div itemprop="numberOfItems">Number of items in list: {0}</div><br>\n\n'''.format(num_of_items)

    f.write(html_start)

    for item in parts:
        index = parts.index(item)
        category = (list(items)[index].upper())
        for i in item:
            html = """
        <div itemprop="itemListElement" itemscope itemtype="https://schema.org/Product">
            <span itemprop="name">Name: {2} {1}</span>
            <div itemprop="model">Model: {0}</div>
            <div itemprop="category">Component category: {1}</div>

            <div itemprop="Brand" itemscope itemtype="https://schema.org/Brand">
                <span itemprop="name">Brand: {2}</span>
            </div>

            <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">
                <span itemprop="priceCurrency" content="GBP">Price: £</span><span
                itemprop="price" content="{3}">{3}</span>
                <div><link itemprop="availability" href="https://schema.org/InStock" />Stock: In stock</div>   
            </div>
        </div><br>\n\n
          """.format(i.model, category, i.brand, i.price.amount, category)
            f.write(html)

    html_end = '''
    </div>
</html>'''

    f.write(html_end)
    f.close()


def export_json(parts, items, num_of_items):
    data = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Recommended component list",
        "description": "A list containing the recommended computer components for the user's preferences",
        "itemListOrder": "ItemListUnordered",
        "numberOfItems": num_of_items,
        "itemListElement": []
    }
    for item in parts:
        index = parts.index(item)
        category = (list(items)[index].upper())
        for i in item:
            data["itemListElement"].append({
                "@type": "Product",
                "name": i.brand + " " + i.model,
                "category": category,
                "offers": {
                    "@type": "Offer",
                    "availability": "https://schema.org/InStock",
                    "price": str(i.price.amount),
                    "priceCurrency": "GBP"
                },
                "brand": {
                    "@type": "Brand",
                    "name": i.brand,
                },
                "model": i.model
            })

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)