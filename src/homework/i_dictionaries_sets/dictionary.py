def add_inventory(widgets: dict, widget_name: str, quantity: int):
    """
    Adds a widget to the dictionary if not present.
    If present, update the quantity by adding the amount.
    """
    if widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity


def remove_inventory_widget(widgets: dict, widget_name: str):
    """
    Removes widget_name from dictionary.
    Returns:
        'Record deleted' if deleted
        'Item not found' if not in dictionary
    """
    if widget_name in widgets:
        del widgets[widget_name]
        return "Record deleted"
    return "Item not found"