
# Subscription Amount with Breakdown

The breakdown details for the amount. Includes the gross, tax, fee, and shipping amounts.

## Structure

`SubscriptionAmountWithBreakdown`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gross_amount` | [`Money`](../../doc/models/money.md) | Required | The currency and amount for a financial transaction, such as a balance or payment due. |
| `total_item_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `fee_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `shipping_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `tax_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `net_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |

## Example

```python
from paypalserversdk.models.money import Money
from paypalserversdk.models.subscription_amount_with_breakdown import SubscriptionAmountWithBreakdown

subscription_amount_with_breakdown = SubscriptionAmountWithBreakdown(
    gross_amount=Money(
        currency_code='currency_code4',
        value='value0'
    ),
    total_item_amount=Money(
        currency_code='currency_code8',
        value='value4'
    ),
    fee_amount=Money(
        currency_code='currency_code2',
        value='value4'
    ),
    shipping_amount=Money(
        currency_code='currency_code0',
        value='value6'
    ),
    tax_amount=Money(
        currency_code='currency_code2',
        value='value8'
    ),
    net_amount=Money(
        currency_code='currency_code6',
        value='value2'
    )
)
```

