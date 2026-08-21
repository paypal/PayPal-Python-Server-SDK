
# Amount Breakdown

The breakdown of the amount. Breakdown provides details such as total item amount, total tax amount, shipping, handling, insurance, and discounts, if any.

## Structure

`AmountBreakdown`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_total` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `shipping` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `handling` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `tax_total` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `insurance` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `shipping_discount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `discount` | [`Money`](../../doc/models/money.md) | Optional | The discount amount and currency code. For list of supported currencies and decimal precision, see the PayPal REST APIs Currency Codes. |

## Example

```python
from paypalserversdk.models.amount_breakdown import AmountBreakdown
from paypalserversdk.models.money import Money

amount_breakdown = AmountBreakdown(
    item_total=Money(
        currency_code='currency_code0',
        value='value6'
    ),
    shipping=Money(
        currency_code='currency_code0',
        value='value6'
    ),
    handling=Money(
        currency_code='currency_code2',
        value='value8'
    ),
    tax_total=Money(
        currency_code='currency_code4',
        value='value0'
    ),
    insurance=Money(
        currency_code='currency_code2',
        value='value8'
    )
)
```

