# .format formatting

print("Hello {}, your lucky number is {}".format("Stew", 67))
# rewrite
print("Hello {name}, your lucky number is {number}".format(name="Stew", number=42))

# rounding formatting (using :.xf for x decimals)
price = 6.9
price_taxed = price * 1.15

print("Base: ${price:.1f}, Tax Incl.: ${price_taxed:.1f}".format(price=price, price_taxed=price_taxed))

# aligning to the right: ">x" - string occupies x spaces, right-aligned
print("Base: {price:>11.1f}\nTax Incl.: {price_taxed:>6.1f}".format(price=price, price_taxed=price_taxed))
print("Base: {price:>11.1f}\nTax Incl.: {price_taxed:>6.1f}".format(price=price*2, price_taxed=price_taxed*2))
print("Base: {price:>11.1f}\nTax Incl.: {price_taxed:>6.1f}".format(price=price*3, price_taxed=price_taxed*3))
print("Base: {price:>11.1f}\nTax Incl.: {price_taxed:>6.1f}".format(price=price*10, price_taxed=price_taxed*10))

print("{price:>11.1f}".format(price=221.3).__len__())

# aligning to the left: "<x" - string occupies x spaces, left-aligned
# centered string: "^x" - occupies x spaces, shifted to left if cannot be centered