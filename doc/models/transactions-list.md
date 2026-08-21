
# Transactions List

The list transactions for a subscription request details.

## Structure

`TransactionsList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transactions` | [`List[SubscriptionTransactionDetails]`](../../doc/models/subscription-transaction-details.md) | Optional | An array of transactions.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `32767` |
| `total_items` | `int` | Optional | The total number of items.<br><br>**Constraints**: `>= 0`, `<= 500000000` |
| `total_pages` | `int` | Optional | The total number of pages.<br><br>**Constraints**: `>= 0`, `<= 100000000` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |

## Example

```python
from paypalserversdk.models.money import Money
from paypalserversdk.models.subscription_amount_with_breakdown import SubscriptionAmountWithBreakdown
from paypalserversdk.models.subscription_payer_name import SubscriptionPayerName
from paypalserversdk.models.subscription_transaction_details import SubscriptionTransactionDetails
from paypalserversdk.models.transactions_list import TransactionsList

transactions_list = TransactionsList(
    transactions=[
        SubscriptionTransactionDetails(
            id=None,
            amount_with_breakdown=SubscriptionAmountWithBreakdown(
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
            ),
            time='time8',
            payer_name=SubscriptionPayerName(
                prefix='prefix8',
                given_name='given_name2',
                surname='surname8',
                middle_name='middle_name0',
                suffix='suffix0'
            ),
            payer_email='payer_email6'
        ),
        SubscriptionTransactionDetails(
            id=None,
            amount_with_breakdown=SubscriptionAmountWithBreakdown(
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
            ),
            time='time8',
            payer_name=SubscriptionPayerName(
                prefix='prefix8',
                given_name='given_name2',
                surname='surname8',
                middle_name='middle_name0',
                suffix='suffix0'
            ),
            payer_email='payer_email6'
        )
    ],
    total_items=8,
    total_pages=44
)
```

