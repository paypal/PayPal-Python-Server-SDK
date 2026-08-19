
# Net Amount Breakdown Item

The net amount. Returned when the currency of the refund is different from the currency of the PayPal account where the merchant holds their funds.

## Structure

`NetAmountBreakdownItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payable_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `converted_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `exchange_rate` | [`ExchangeRate`](../../doc/models/exchange-rate.md) | Optional, Read-only | The exchange rate that determines the amount to convert from one currency to another currency. |

## Example

```python
from paypalserversdk.models.money import Money
from paypalserversdk.models.net_amount_breakdown_item import NetAmountBreakdownItem

net_amount_breakdown_item = NetAmountBreakdownItem(
    payable_amount=Money(
        currency_code='currency_code8',
        value='value4'
    ),
    converted_amount=Money(
        currency_code='currency_code0',
        value='value6'
    )
)
```

