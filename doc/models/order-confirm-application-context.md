
# Order Confirm Application Context

Customizes the payer confirmation experience.

## Structure

`OrderConfirmApplicationContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand_name` | `str` | Optional | Label to present to your payer as part of the PayPal hosted web experience.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127` |
| `locale` | `str` | Optional | The [language tag](https://tools.ietf.org/html/bcp47#section-2) for the language in which to localize the error-related strings, such as messages, issues, and suggested actions. The tag is made up of the [ISO 639-2 language code](https://www.loc.gov/standards/iso639-2/php/code_list.php), the optional [ISO-15924 script tag](https://www.unicode.org/iso15924/codelists.html), and the [ISO-3166 alpha-2 country code](https://developer.paypal.com/api/rest/reference/country-codes/) or [M49 region code](https://unstats.un.org/unsd/methodology/m49/).<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `10`, *Pattern*: `^[a-z]{2}(?:-[A-Z][a-z]{3})?(?:-(?:[A-Z]{2}\|[0-9]{3}))?$` |
| `return_url` | `str` | Optional | The URL where the customer is redirected after the customer approves the payment.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `4000` |
| `cancel_url` | `str` | Optional | The URL where the customer is redirected after the customer cancels the payment.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `4000` |
| `stored_payment_source` | [`StoredPaymentSource`](../../doc/models/stored-payment-source.md) | Optional | Provides additional details to process a payment using a `payment_source` that has been stored or is intended to be stored (also referred to as stored_credential or card-on-file). Parameter compatibility: `payment_type=ONE_TIME` is compatible only with `payment_initiator=CUSTOMER`. `usage=FIRST` is compatible only with `payment_initiator=CUSTOMER`. `previous_transaction_reference` or `previous_network_transaction_reference` is compatible only with `payment_initiator=MERCHANT`. Only one of the parameters - `previous_transaction_reference` and `previous_network_transaction_reference` - can be present in the request. |

## Example

```python
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.network_transaction import NetworkTransaction
from paypalserversdk.models.order_confirm_application_context import OrderConfirmApplicationContext
from paypalserversdk.models.payment_initiator import PaymentInitiator
from paypalserversdk.models.stored_payment_source import StoredPaymentSource
from paypalserversdk.models.stored_payment_source_payment_type import StoredPaymentSourcePaymentType
from paypalserversdk.models.stored_payment_source_usage_type import StoredPaymentSourceUsageType

order_confirm_application_context = OrderConfirmApplicationContext(
    brand_name='brand_name2',
    locale='locale2',
    return_url='return_url0',
    cancel_url='cancel_url2',
    stored_payment_source=StoredPaymentSource(
        payment_initiator=PaymentInitiator.CUSTOMER,
        payment_type=StoredPaymentSourcePaymentType.RECURRING,
        usage=StoredPaymentSourceUsageType.FIRST,
        previous_network_transaction_reference=NetworkTransaction(
            id='id6',
            date='date2',
            network=CardBrand.CONFIDIS,
            acquirer_reference_number='acquirer_reference_number8'
        )
    )
)
```

