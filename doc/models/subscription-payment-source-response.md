
# Subscription Payment Source Response

The payment source used to fund the payment.

## Structure

`SubscriptionPaymentSourceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`CardResponseWithBillingAddress`](../../doc/models/card-response-with-billing-address.md) | Optional | The payment card used to fund the payment. Card can be a credit or debit card. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.card_response_with_billing_address import CardResponseWithBillingAddress
from paypalserversdk.models.subscription_payment_source_response import SubscriptionPaymentSourceResponse

subscription_payment_source_response = SubscriptionPaymentSourceResponse(
    card=CardResponseWithBillingAddress(
        name='name6',
        billing_address=Address(
            country_code='country_code8',
            address_line_1='address_line_12',
            address_line_2='address_line_28',
            admin_area_2='admin_area_28',
            admin_area_1='admin_area_14',
            postal_code='postal_code0'
        ),
        expiry='expiry4',
        currency_code='currency_code2'
    )
)
```

