
# Payment Collection

The collection of payments, or transactions, for a purchase unit in an order. For example, authorized payments, captured payments, and refunds.

## Structure

`PaymentCollection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorizations` | [`List[AuthorizationWithAdditionalData]`](../../doc/models/authorization-with-additional-data.md) | Optional | An array of authorized payments for a purchase unit. A purchase unit can have zero or more authorized payments. |
| `captures` | [`List[OrdersCapture]`](../../doc/models/orders-capture.md) | Optional | An array of captured payments for a purchase unit. A purchase unit can have zero or more captured payments. |
| `refunds` | [`List[Refund]`](../../doc/models/refund.md) | Optional | An array of refunds for a purchase unit. A purchase unit can have zero or more refunds. |

## Example

```python
from paypalserversdk.models.authorization_incomplete_reason import AuthorizationIncompleteReason
from paypalserversdk.models.authorization_status_details import AuthorizationStatusDetails
from paypalserversdk.models.authorization_with_additional_data import AuthorizationWithAdditionalData
from paypalserversdk.models.capture_incomplete_reason import CaptureIncompleteReason
from paypalserversdk.models.capture_status_details import CaptureStatusDetails
from paypalserversdk.models.money import Money
from paypalserversdk.models.orders_capture import OrdersCapture
from paypalserversdk.models.payment_collection import PaymentCollection
from paypalserversdk.models.refund import Refund
from paypalserversdk.models.refund_incomplete_reason import RefundIncompleteReason
from paypalserversdk.models.refund_status_details import RefundStatusDetails

payment_collection = PaymentCollection(
    authorizations=[
        AuthorizationWithAdditionalData(
            status_details=AuthorizationStatusDetails(
                reason=AuthorizationIncompleteReason.PENDING_REVIEW
            ),
            amount=Money(
                currency_code='currency_code6',
                value='value0'
            )
        ),
        AuthorizationWithAdditionalData(
            status_details=AuthorizationStatusDetails(
                reason=AuthorizationIncompleteReason.PENDING_REVIEW
            ),
            amount=Money(
                currency_code='currency_code6',
                value='value0'
            )
        ),
        AuthorizationWithAdditionalData(
            status_details=AuthorizationStatusDetails(
                reason=AuthorizationIncompleteReason.PENDING_REVIEW
            ),
            amount=Money(
                currency_code='currency_code6',
                value='value0'
            )
        )
    ],
    captures=[
        OrdersCapture(
            status_details=CaptureStatusDetails(
                reason=CaptureIncompleteReason.VERIFICATION_REQUIRED
            ),
            amount=Money(
                currency_code='currency_code6',
                value='value0'
            )
        ),
        OrdersCapture(
            status_details=CaptureStatusDetails(
                reason=CaptureIncompleteReason.VERIFICATION_REQUIRED
            ),
            amount=Money(
                currency_code='currency_code6',
                value='value0'
            )
        )
    ],
    refunds=[
        Refund(
            status_details=RefundStatusDetails(
                reason=RefundIncompleteReason.ECHECK
            ),
            amount=Money(
                currency_code='currency_code6',
                value='value0'
            )
        ),
        Refund(
            status_details=RefundStatusDetails(
                reason=RefundIncompleteReason.ECHECK
            ),
            amount=Money(
                currency_code='currency_code6',
                value='value0'
            )
        )
    ]
)
```

