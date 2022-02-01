def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda pair: (-len(pair[1]), pair[0]))

    result = ''
    for name, quantities in sorted_cheeses:
        result += name + '\n'
        sorted_quantities = sorted(quantities, reverse=True)
        result += '\n'.join(map(str, sorted_quantities)) + '\n'
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)