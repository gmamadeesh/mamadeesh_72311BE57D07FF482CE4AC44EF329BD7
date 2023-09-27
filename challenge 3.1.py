def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = ["rose", "lotus", "lilly", "jasmin", "rose", "lris", "sunflower"]
target = "rose"
target2 = 'orange'
result = linearSearchProduct(products, target)
print(result)