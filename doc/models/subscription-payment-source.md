
# Subscription Payment Source

The payment source definition. To be eligible to create subscription using debit or credit card, you will need to sign up here (https://www.paypal.com/bizsignup/entry/product/ppcp). Please note, its available only for non-3DS cards and for merchants in US and AU regions.

## Structure

`SubscriptionPaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`SubscriptionCardRequest`](../../doc/models/subscription-card-request.md) | Optional | The payment card to use to fund a payment. Can be a credit or debit card. |

## Example

```python
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.subscription_card_request import SubscriptionCardRequest
from paypalserversdk.models.subscription_payment_source import SubscriptionPaymentSource

subscription_payment_source = SubscriptionPaymentSource(
    card=SubscriptionCardRequest(
        name='name6',
        number='number6',
        expiry='expiry4',
        security_code='security_code8',
        mtype=CardType.UNKNOWN
    )
)
```

