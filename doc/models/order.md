
# Order

The order details.

## Structure

`Order`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `create_time` | `str` | Optional | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does not reject all invalid dates.<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `64`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[1-2][0-9]\|3[0-1])[T,t]([0-1][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?([Zz]\|[+-][0-9]{2}:[0-9]{2})$` |
| `update_time` | `str` | Optional | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does not reject all invalid dates.<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `64`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[1-2][0-9]\|3[0-1])[T,t]([0-1][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?([Zz]\|[+-][0-9]{2}:[0-9]{2})$` |
| `id` | `str` | Optional, Read-only | The ID of the order. |
| `payment_source` | [`PaymentSourceResponse`](../../doc/models/payment-source-response.md) | Optional | The payment source used to fund the payment. |
| `intent` | [`CheckoutPaymentIntent`](../../doc/models/checkout-payment-intent.md) | Optional | The intent to either capture payment immediately or authorize a payment for an order after order creation. |
| `processing_instruction` | [`ProcessingInstruction`](../../doc/models/processing-instruction.md) | Optional | The instruction to process an order. |
| `payer` | [`Payer`](../../doc/models/payer.md) | Optional | DEPRECATED. The customer is also known as the payer. The Payer object was intended to only be used with the `payment_source.paypal` object. In order to make this design more clear, the details in the `payer` object are now available under `payment_source.paypal`. Please use `payment_source.paypal`. |
| `purchase_units` | [`List[PurchaseUnit]`](../../doc/models/purchase-unit.md) | Optional | An array of purchase units. Each purchase unit establishes a contract between a customer and merchant. Each purchase unit represents either a full or partial order that the customer intends to purchase from the merchant.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `status` | [`OrderStatus`](../../doc/models/order-status.md) | Optional | The order status.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related HATEOAS links. To complete payer approval, use the `approve` link to redirect the payer. The API caller has 6 hours (default setting, this which can be changed by your account manager to 24/48/72 hours to accommodate your use case) from the time the order is created, to redirect your payer. Once redirected, the API caller has 6 hours for the payer to approve the order and either authorize or capture the order. If you are not using the PayPal JavaScript SDK to initiate PayPal Checkout (in context) ensure that you include `application_context.return_url` is specified or you will get "We're sorry, Things don't appear to be working at the moment" after the payer approves the payment. |

## Example

```python
from paypalserversdk.models.bancontact_payment_object import BancontactPaymentObject
from paypalserversdk.models.blik_one_click_payment_object import BlikOneClickPaymentObject
from paypalserversdk.models.blik_payment_object import BlikPaymentObject
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_response import CardResponse
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.checkout_payment_intent import CheckoutPaymentIntent
from paypalserversdk.models.eps_payment_object import EpsPaymentObject
from paypalserversdk.models.name import Name
from paypalserversdk.models.order import Order
from paypalserversdk.models.payment_source_response import PaymentSourceResponse
from paypalserversdk.models.paypal_wallet_response import PaypalWalletResponse
from paypalserversdk.models.phone_type import PhoneType

order = Order(
    create_time='create_time2',
    update_time='update_time8',
    payment_source=PaymentSourceResponse(
        card=CardResponse(
            name='name6',
            brand=CardBrand.CB_NATIONALE,
            mtype=CardType.UNKNOWN
        ),
        paypal=PaypalWalletResponse(
            email_address='email_address0',
            account_id='account_id4',
            name=Name(
                given_name='given_name2',
                surname='surname8'
            ),
            phone_type=PhoneType.FAX
        ),
        bancontact=BancontactPaymentObject(
            name='name0',
            country_code='country_code0',
            bic='bic2',
            iban_last_chars='iban_last_chars8',
            card_last_digits='card_last_digits4'
        ),
        blik=BlikPaymentObject(
            name='name2',
            country_code='country_code2',
            email='email4',
            one_click=BlikOneClickPaymentObject(
                consumer_reference='consumer_reference2'
            )
        ),
        eps=EpsPaymentObject(
            name='name6',
            country_code='country_code6',
            bic='bic8'
        )
    ),
    intent=CheckoutPaymentIntent.CAPTURE
)
```

