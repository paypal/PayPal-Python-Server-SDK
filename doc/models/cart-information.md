
# Cart Information

The cart information.

## Structure

`CartInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_details` | [`List[ItemDetails]`](../../doc/models/item-details.md) | Optional | An array of item details.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `32767` |
| `tax_inclusive` | `bool` | Optional | Indicates whether the item amount or the shipping amount already includes tax.<br><br>**Default**: `False` |
| `paypal_invoice_id` | `str` | Optional | The ID of the invoice. Appears for only PayPal-generated invoices.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^[a-zA-Z0-9_'\-., ":;\!?]*$` |

## Example

```python
from paypalserversdk.models.cart_information import CartInformation
from paypalserversdk.models.item_details import ItemDetails

cart_information = CartInformation(
    item_details=[
        ItemDetails(
            item_code='item_code0',
            item_name='item_name8',
            item_description='item_description4',
            item_options='item_options2',
            item_quantity='item_quantity2'
        ),
        ItemDetails(
            item_code='item_code0',
            item_name='item_name8',
            item_description='item_description4',
            item_options='item_options2',
            item_quantity='item_quantity2'
        ),
        ItemDetails(
            item_code='item_code0',
            item_name='item_name8',
            item_description='item_description4',
            item_options='item_options2',
            item_quantity='item_quantity2'
        )
    ],
    tax_inclusive=False,
    paypal_invoice_id='paypal_invoice_id4'
)
```

