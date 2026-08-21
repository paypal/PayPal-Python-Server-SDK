
# Capture Request

Captures either a portion or the full authorized amount of an authorized payment.

## Structure

`CaptureRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `invoice_id` | `str` | Optional | The API caller-provided external invoice number for this order. Appears in both the payer's transaction history and the emails that the payer receives.<br><br>**Constraints**: *Maximum Length*: `127` |
| `final_capture` | `bool` | Optional | Indicates whether you can make additional captures against the authorized payment. Set to `true` if you do not intend to capture additional payments against the authorization. Set to `false` if you intend to capture additional payments against the authorization.<br><br>**Default**: `False` |
| `payment_instruction` | [`CapturePaymentInstruction`](../../doc/models/capture-payment-instruction.md) | Optional | Any additional payment instructions to be consider during payment processing. This processing instruction is applicable for Capturing an order or Authorizing an Order. |
| `note_to_payer` | `str` | Optional | An informational note about this settlement. Appears in both the payer's transaction history and the emails that the payer receives.<br><br>**Constraints**: *Maximum Length*: `255` |
| `soft_descriptor` | `str` | Optional | The payment descriptor on the payer's account statement.<br><br>**Constraints**: *Maximum Length*: `22` |

## Example

```python
from paypalserversdk.models.capture_payment_instruction import CapturePaymentInstruction
from paypalserversdk.models.capture_request import CaptureRequest
from paypalserversdk.models.disbursement_mode import DisbursementMode
from paypalserversdk.models.money import Money
from paypalserversdk.models.payee_base import PayeeBase
from paypalserversdk.models.platform_fee import PlatformFee

capture_request = CaptureRequest(
    amount=Money(
        currency_code='currency_code6',
        value='value0'
    ),
    invoice_id='invoice_id6',
    final_capture=False,
    payment_instruction=CapturePaymentInstruction(
        platform_fees=[
            PlatformFee(
                amount=Money(
                    currency_code='currency_code6',
                    value='value0'
                ),
                payee=PayeeBase(
                    email_address='email_address4',
                    merchant_id='merchant_id6'
                )
            ),
            PlatformFee(
                amount=Money(
                    currency_code='currency_code6',
                    value='value0'
                ),
                payee=PayeeBase(
                    email_address='email_address4',
                    merchant_id='merchant_id6'
                )
            ),
            PlatformFee(
                amount=Money(
                    currency_code='currency_code6',
                    value='value0'
                ),
                payee=PayeeBase(
                    email_address='email_address4',
                    merchant_id='merchant_id6'
                )
            )
        ],
        disbursement_mode=DisbursementMode.INSTANT,
        payee_receivable_fx_rate_id='payee_receivable_fx_rate_id0'
    ),
    note_to_payer='note_to_payer8'
)
```

