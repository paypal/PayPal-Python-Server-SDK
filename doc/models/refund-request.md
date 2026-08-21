
# Refund Request

Refunds a captured payment, by ID. For a full refund, include an empty request body. For a partial refund, include an amount object in the request body.

## Structure

`RefundRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `custom_id` | `str` | Optional | The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal transactions. Appears in transaction and settlement reports. The pattern is defined by an external party and supports Unicode.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `invoice_id` | `str` | Optional | The API caller-provided external invoice ID for this order. The pattern is defined by an external party and supports Unicode.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `note_to_payer` | `str` | Optional | The reason for the refund. Appears in both the payer's transaction history and the emails that the payer receives. The pattern is defined by an external party and supports Unicode.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^.*$` |
| `payment_instruction` | [`RefundPaymentInstruction`](../../doc/models/refund-payment-instruction.md) | Optional | Any additional payments instructions during refund payment processing. This object is only applicable to merchants that have been enabled for PayPal Commerce Platform for Marketplaces and Platforms capability. Please speak to your account manager if you want to use this capability. |

## Example

```python
from paypalserversdk.models.money import Money
from paypalserversdk.models.refund_payment_instruction import RefundPaymentInstruction
from paypalserversdk.models.refund_platform_fee import RefundPlatformFee
from paypalserversdk.models.refund_request import RefundRequest

refund_request = RefundRequest(
    amount=Money(
        currency_code='currency_code6',
        value='value0'
    ),
    custom_id='custom_id8',
    invoice_id='invoice_id0',
    note_to_payer='note_to_payer2',
    payment_instruction=RefundPaymentInstruction(
        platform_fees=[
            RefundPlatformFee(
                amount=Money(
                    currency_code='currency_code6',
                    value='value0'
                )
            ),
            RefundPlatformFee(
                amount=Money(
                    currency_code='currency_code6',
                    value='value0'
                )
            ),
            RefundPlatformFee(
                amount=Money(
                    currency_code='currency_code6',
                    value='value0'
                )
            )
        ]
    )
)
```

