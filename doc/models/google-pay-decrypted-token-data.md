
# Google Pay Decrypted Token Data

Details shared by Google for the merchant to be shared with PayPal. This is required to process the transaction using the Google Pay payment method.

## Structure

`GooglePayDecryptedTokenData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_id` | `str` | Optional | A unique ID that identifies the message in case it needs to be revoked or located at a later time.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `250`, *Pattern*: `^.*$` |
| `message_expiration` | `str` | Optional | Date and time at which the message expires as UTC milliseconds since epoch. Integrators should reject any message that's expired.<br><br>**Constraints**: *Minimum Length*: `13`, *Maximum Length*: `13`, *Pattern*: `\d{13}` |
| `payment_method` | [`GooglePayPaymentMethod`](../../doc/models/google-pay-payment-method.md) | Required | The type of the payment credential. Currently, only CARD is supported.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4` |
| `card` | [`GooglePayCard`](../../doc/models/google-pay-card.md) | Required | The payment card used to fund a Google Pay payment. Can be a credit or debit card. |
| `authentication_method` | [`GooglePayAuthenticationMethod`](../../doc/models/google-pay-authentication-method.md) | Required | Authentication Method which is used for the card transaction.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `cryptogram` | `str` | Optional | Base-64 cryptographic identifier used by card schemes to validate the token verification result. This is a conditionally required field if authentication_method is CRYPTOGRAM_3DS.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2000` |
| `eci_indicator` | `str` | Optional | Electronic Commerce Indicator may not always be present. It is only returned for tokens on the Visa card network. This value is passed through in the payment authorization request.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `256`, *Pattern*: `^.*$` |

## Example

```python
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.google_pay_authentication_method import GooglePayAuthenticationMethod
from paypalserversdk.models.google_pay_card import GooglePayCard
from paypalserversdk.models.google_pay_decrypted_token_data import GooglePayDecryptedTokenData
from paypalserversdk.models.google_pay_payment_method import GooglePayPaymentMethod

google_pay_decrypted_token_data = GooglePayDecryptedTokenData(
    payment_method=GooglePayPaymentMethod.CARD,
    card=GooglePayCard(
        name='name6',
        number='number6',
        expiry='expiry4',
        mtype=CardType.UNKNOWN
    ),
    authentication_method=GooglePayAuthenticationMethod.PAN_ONLY,
    message_id='message_id2',
    message_expiration='message_expiration0',
    cryptogram='cryptogram8',
    eci_indicator='eci_indicator2'
)
```

