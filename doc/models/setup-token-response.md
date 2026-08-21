
# Setup Token Response

Minimal representation of a cached setup token.

## Structure

`SetupTokenResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The PayPal-generated ID for the vaulted payment source. This ID should be stored on the merchant's server so the saved payment source can be used for future transactions.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9a-zA-Z_-]+$` |
| `customer` | [`Customer`](../../doc/models/customer.md) | Optional | This object defines a customer in your system. Use it to manage customer profiles, save payment methods and contact details. |
| `status` | [`PaymentTokenStatus`](../../doc/models/payment-token-status.md) | Optional | The status of the payment token.<br><br>**Default**: `"CREATED"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `payment_source` | [`SetupTokenResponsePaymentSource`](../../doc/models/setup-token-response-payment-source.md) | Optional | The setup payment method details. |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of related [HATEOAS links](https://developer.paypal.com/api/rest/responses/#hateoas).<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `32` |

## Example

```python
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_response_address import CardResponseAddress
from paypalserversdk.models.customer import Customer
from paypalserversdk.models.payment_token_status import PaymentTokenStatus
from paypalserversdk.models.setup_token_response import SetupTokenResponse
from paypalserversdk.models.setup_token_response_card import SetupTokenResponseCard
from paypalserversdk.models.setup_token_response_payment_source import SetupTokenResponsePaymentSource

setup_token_response = SetupTokenResponse(
    id='id0',
    customer=Customer(
        id='id0',
        merchant_customer_id='merchant_customer_id2'
    ),
    status=PaymentTokenStatus.CREATED,
    payment_source=SetupTokenResponsePaymentSource(
        card=SetupTokenResponseCard(
            name='name6',
            brand=CardBrand.CB_NATIONALE,
            expiry='expiry4',
            billing_address=CardResponseAddress(
                country_code='country_code8',
                address_line_1='address_line_12',
                address_line_2='address_line_28',
                admin_area_2='admin_area_28',
                admin_area_1='admin_area_14',
                postal_code='postal_code0'
            )
        )
    )
)
```

