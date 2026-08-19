
# Seller Receivable Breakdown

The detailed breakdown of the capture activity. This is not available for transactions that are in pending state.

## Structure

`SellerReceivableBreakdown`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gross_amount` | [`Money`](../../doc/models/money.md) | Required | The currency and amount for a financial transaction, such as a balance or payment due. |
| `paypal_fee` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `paypal_fee_in_receivable_currency` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `net_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `receivable_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `exchange_rate` | [`ExchangeRate`](../../doc/models/exchange-rate.md) | Optional, Read-only | The exchange rate that determines the amount to convert from one currency to another currency. |
| `platform_fees` | [`List[PlatformFee]`](../../doc/models/platform-fee.md) | Optional | An array of platform or partner fees, commissions, or brokerage fees that associated with the captured payment.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `1` |

## Example

```python
from paypalserversdk.models.money import Money
from paypalserversdk.models.seller_receivable_breakdown import SellerReceivableBreakdown

seller_receivable_breakdown = SellerReceivableBreakdown(
    gross_amount=Money(
        currency_code='currency_code4',
        value='value0'
    ),
    paypal_fee=Money(
        currency_code='currency_code4',
        value='value2'
    ),
    paypal_fee_in_receivable_currency=Money(
        currency_code='currency_code2',
        value='value8'
    ),
    net_amount=Money(
        currency_code='currency_code6',
        value='value2'
    ),
    receivable_amount=Money(
        currency_code='currency_code2',
        value='value8'
    )
)
```

