
# Google Pay Request

Information needed to pay using Google Pay.

## Structure

`GooglePayRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The full name representation like Mr J Smith.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `300` |
| `email_address` | `str` | Optional | The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern verifies that an unquoted @ sign exists.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `254`, *Pattern*: ``^(?:[A-Za-z0-9!#$%&'*+/=?^_`{\|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{\|}~-]+)*\|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]\|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\|\[(?:(?:25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?\|[A-Za-z0-9-]*[A-Za-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]\|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$`` |
| `phone_number` | [`PhoneNumberWithCountryCode`](../../doc/models/phone-number-with-country-code.md) | Optional | The phone number in its canonical international [E.164 numbering plan format](https://www.itu.int/rec/T-REC-E.164/en). |
| `card` | [`GooglePayRequestCard`](../../doc/models/google-pay-request-card.md) | Optional | The payment card used to fund a Google Pay payment. Can be a credit or debit card. |
| `decrypted_token` | [`GooglePayDecryptedTokenData`](../../doc/models/google-pay-decrypted-token-data.md) | Optional | Details shared by Google for the merchant to be shared with PayPal. This is required to process the transaction using the Google Pay payment method. |
| `assurance_details` | [`AssuranceDetails`](../../doc/models/assurance-details.md) | Optional | Information about cardholder possession validation and cardholder identification and verifications (ID&V). |
| `experience_context` | [`GooglePayExperienceContext`](../../doc/models/google-pay-experience-context.md) | Optional | Customizes the payer experience during the approval process for the payment. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.google_pay_authentication_method import GooglePayAuthenticationMethod
from paypalserversdk.models.google_pay_card import GooglePayCard
from paypalserversdk.models.google_pay_decrypted_token_data import GooglePayDecryptedTokenData
from paypalserversdk.models.google_pay_payment_method import GooglePayPaymentMethod
from paypalserversdk.models.google_pay_request import GooglePayRequest
from paypalserversdk.models.google_pay_request_card import GooglePayRequestCard
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode

google_pay_request = GooglePayRequest(
    name='name6',
    email_address='email_address4',
    phone_number=PhoneNumberWithCountryCode(
        country_code='country_code2',
        national_number='national_number6'
    ),
    card=GooglePayRequestCard(
        name='name6',
        mtype=CardType.UNKNOWN,
        brand=CardBrand.CB_NATIONALE,
        billing_address=Address(
            country_code='country_code8',
            address_line_1='address_line_12',
            address_line_2='address_line_28',
            admin_area_2='admin_area_28',
            admin_area_1='admin_area_14',
            postal_code='postal_code0'
        )
    ),
    decrypted_token=GooglePayDecryptedTokenData(
        payment_method=GooglePayPaymentMethod.CARD,
        card=GooglePayCard(
            name='name6',
            number='number6',
            expiry='expiry4',
            mtype=CardType.UNKNOWN
        ),
        authentication_method=GooglePayAuthenticationMethod.PAN_ONLY,
        message_id='message_id0',
        message_expiration='message_expiration2',
        cryptogram='cryptogram6',
        eci_indicator='eci_indicator0'
    )
)
```

