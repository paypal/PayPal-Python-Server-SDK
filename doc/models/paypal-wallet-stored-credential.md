
# Paypal Wallet Stored Credential

Provides additional details to process a payment using the PayPal wallet billing agreement or a vaulted payment method that has been stored or is intended to be stored.

## Structure

`PaypalWalletStoredCredential`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_initiator` | [`PaymentInitiator`](../../doc/models/payment-initiator.md) | Required | The person or party who initiated or triggered the payment.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `charge_pattern` | [`UsagePattern`](../../doc/models/usage-pattern.md) | Optional | DEPRECATED. Expected business/pricing model for the billing agreement, Please use usage_pattern instead.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `30`, *Pattern*: `^[A-Z0-9_]+$` |
| `usage_pattern` | [`UsagePattern`](../../doc/models/usage-pattern.md) | Optional | Expected business/pricing model for the billing agreement.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `30`, *Pattern*: `^[A-Z0-9_]+$` |
| `usage` | [`StoredPaymentSourceUsageType`](../../doc/models/stored-payment-source-usage-type.md) | Optional | Indicates if this is a `first` or `subsequent` payment using a stored payment source (also referred to as stored credential or card on file).<br><br>**Default**: `"DERIVED"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |

## Example

```python
from paypalserversdk.models.payment_initiator import PaymentInitiator
from paypalserversdk.models.paypal_wallet_stored_credential import PaypalWalletStoredCredential
from paypalserversdk.models.stored_payment_source_usage_type import StoredPaymentSourceUsageType
from paypalserversdk.models.usage_pattern import UsagePattern

paypal_wallet_stored_credential = PaypalWalletStoredCredential(
    payment_initiator=PaymentInitiator.CUSTOMER,
    charge_pattern=UsagePattern.UNSCHEDULED_PREPAID,
    usage_pattern=UsagePattern.UNSCHEDULED_PREPAID,
    usage=StoredPaymentSourceUsageType.DERIVED
)
```

