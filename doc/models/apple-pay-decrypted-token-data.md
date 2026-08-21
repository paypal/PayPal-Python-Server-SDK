
# Apple Pay Decrypted Token Data

Information about the Payment data obtained by decrypting Apple Pay token.

## Structure

`ApplePayDecryptedTokenData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `tokenized_card` | [`ApplePayTokenizedCard`](../../doc/models/apple-pay-tokenized-card.md) | Required | The payment card to use to fund a payment. Can be a credit or debit card. |
| `device_manufacturer_id` | `str` | Optional | Apple Pay Hex-encoded device manufacturer identifier. The pattern is defined by an external party and supports Unicode.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2000`, *Pattern*: `^.*$` |
| `payment_data_type` | [`ApplePayPaymentDataType`](../../doc/models/apple-pay-payment-data-type.md) | Optional | Indicates the type of payment data passed, in case of Non China the payment data is 3DSECURE and for China it is EMV.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `16`, *Pattern*: `^[0-9A-Z_]+$` |
| `payment_data` | [`ApplePayPaymentData`](../../doc/models/apple-pay-payment-data.md) | Optional | Information about the decrypted apple pay payment data for the token like cryptogram, eci indicator. |

## Example

```python
from paypalserversdk.models.apple_pay_decrypted_token_data import ApplePayDecryptedTokenData
from paypalserversdk.models.apple_pay_payment_data import ApplePayPaymentData
from paypalserversdk.models.apple_pay_payment_data_type import ApplePayPaymentDataType
from paypalserversdk.models.apple_pay_tokenized_card import ApplePayTokenizedCard
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.money import Money

apple_pay_decrypted_token_data = ApplePayDecryptedTokenData(
    tokenized_card=ApplePayTokenizedCard(
        name='name4',
        number='number2',
        expiry='expiry2',
        mtype=CardType.UNKNOWN
    ),
    transaction_amount=Money(
        currency_code='currency_code6',
        value='value2'
    ),
    device_manufacturer_id='device_manufacturer_id4',
    payment_data_type=ApplePayPaymentDataType.ENUM_3DSECURE,
    payment_data=ApplePayPaymentData(
        cryptogram='cryptogram6',
        eci_indicator='eci_indicator0',
        emv_data='emv_data0',
        pin='pin4'
    )
)
```

