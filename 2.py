def pack_luggage(items):
    suitcase = []

    # Step 1: Categorize items
    heavy_items = [item for item in items if item.weight == 'heavy']
    rolled_clothes = [item for item in items if item.pack_method == 'roll']
    folded_clothes = [item for item in items if item.pack_method == 'fold']
    delicate_items = [item for item in items if item.fragile]
    accessories = [item for item in items if item.category == 'accessory']
    quick_access = [item for item in items if item.frequency == 'daily']

    # Step 2: Pack heavy items at the bottom
    for item in heavy_items:
        suitcase.append(place(item, position='bottom'))

    # Step 3: Pack rolled clothes for compression
    for item in rolled_clothes:
        suitcase.append(roll_and_place(item, layer='lower-middle'))

    # Step 4: Cushion and pack delicate items
    for item in delicate_items:
        wrap_with_soft_clothes(item)
        suitcase.append(place(item, layer='middle'))

    # Step 5: Pack folded clothes
    for item in folded_clothes:
        suitcase.append(fold_and_place(item, layer='upper-middle'))

    # Step 6: Fill gaps with accessories
    for item in accessories:
        suitcase.append(place_in_gap(item))

    # Step 7: Pack quick-access items at the top
    for item in quick_access:
        suitcase.append(place(item, position='top'))

    # Step 8: Final compression and balance check
    compress(suitcase)
    ensure_weight_balance(suitcase)

    return suitcase
