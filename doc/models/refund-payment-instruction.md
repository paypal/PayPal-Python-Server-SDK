
# Refund Payment Instruction

Any additional payments instructions during refund payment processing. This object is only applicable to merchants that have been enabled for PayPal Commerce Platform for Marketplaces and Platforms capability. Please speak to your account manager if you want to use this capability.

## Structure

`RefundPaymentInstruction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `platform_fees` | [`List[RefundPlatformFee]`](../../doc/models/refund-platform-fee.md) | Optional | Specifies the amount that the API caller will contribute to the refund being processed. The amount needs to be lower than platform_fees amount originally captured or the amount that is remaining if multiple refunds have been processed. This field is only applicable to merchants that have been enabled for PayPal Commerce Platform for Marketplaces and Platforms capability. Please speak to your account manager if you want to use this capability.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `1` |

## Example

```python
from paypalserversdk.models.money import Money
from paypalserversdk.models.refund_payment_instruction import RefundPaymentInstruction
from paypalserversdk.models.refund_platform_fee import RefundPlatformFee

refund_payment_instruction = RefundPaymentInstruction(
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
```

