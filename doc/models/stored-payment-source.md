
# Stored Payment Source

Provides additional details to process a payment using a `payment_source` that has been stored or is intended to be stored (also referred to as stored_credential or card-on-file). Parameter compatibility: `payment_type=ONE_TIME` is compatible only with `payment_initiator=CUSTOMER`. `usage=FIRST` is compatible only with `payment_initiator=CUSTOMER`. `previous_transaction_reference` or `previous_network_transaction_reference` is compatible only with `payment_initiator=MERCHANT`. Only one of the parameters - `previous_transaction_reference` and `previous_network_transaction_reference` - can be present in the request.

## Structure

`StoredPaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_initiator` | [`PaymentInitiator`](../../doc/models/payment-initiator.md) | Required | The person or party who initiated or triggered the payment.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `payment_type` | [`StoredPaymentSourcePaymentType`](../../doc/models/stored-payment-source-payment-type.md) | Required | Indicates the type of the stored payment_source payment.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `usage` | [`StoredPaymentSourceUsageType`](../../doc/models/stored-payment-source-usage-type.md) | Optional | Indicates if this is a `first` or `subsequent` payment using a stored payment source (also referred to as stored credential or card on file).<br><br>**Default**: `"DERIVED"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `previous_network_transaction_reference` | [`NetworkTransaction`](../../doc/models/network-transaction.md) | Optional | Reference values used by the card network to identify a transaction. |

## Example

```python
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.network_transaction import NetworkTransaction
from paypalserversdk.models.payment_initiator import PaymentInitiator
from paypalserversdk.models.stored_payment_source import StoredPaymentSource
from paypalserversdk.models.stored_payment_source_payment_type import StoredPaymentSourcePaymentType
from paypalserversdk.models.stored_payment_source_usage_type import StoredPaymentSourceUsageType

stored_payment_source = StoredPaymentSource(
    payment_initiator=PaymentInitiator.CUSTOMER,
    payment_type=StoredPaymentSourcePaymentType.RECURRING,
    usage=StoredPaymentSourceUsageType.DERIVED,
    previous_network_transaction_reference=NetworkTransaction(
        id='id6',
        date='date2',
        network=CardBrand.CONFIDIS,
        acquirer_reference_number='acquirer_reference_number8'
    )
)
```

