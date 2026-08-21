
# Subscription Billing Information

The billing details for the subscription. If the subscription was or is active, these fields are populated.

## Structure

`SubscriptionBillingInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `outstanding_balance` | [`Money`](../../doc/models/money.md) | Required | The currency and amount for a financial transaction, such as a balance or payment due. |
| `cycle_executions` | [`List[CycleExecution]`](../../doc/models/cycle-execution.md) | Optional, Read-only | The trial and regular billing executions.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `3` |
| `last_payment` | [`LastPaymentDetails`](../../doc/models/last-payment-details.md) | Optional | The details for the last payment. |
| `next_billing_time` | `str` | Optional | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does not reject all invalid dates.<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `64`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[1-2][0-9]\|3[0-1])[T,t]([0-1][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?([Zz]\|[+-][0-9]{2}:[0-9]{2})$` |
| `final_payment_time` | `str` | Optional | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does not reject all invalid dates.<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `64`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[1-2][0-9]\|3[0-1])[T,t]([0-1][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?([Zz]\|[+-][0-9]{2}:[0-9]{2})$` |
| `failed_payments_count` | `int` | Required, Read-only | The number of consecutive payment failures. Resets to `0` after a successful payment. If this reaches the `payment_failure_threshold` value, the subscription updates to the `SUSPENDED` state.<br><br>**Constraints**: `>= 0`, `<= 999` |
| `last_failed_payment` | [`FailedPaymentDetails`](../../doc/models/failed-payment-details.md) | Optional | The details for the failed payment of the subscription. |

## Example

```python
from paypalserversdk.models.failed_payment_details import FailedPaymentDetails
from paypalserversdk.models.last_payment_details import LastPaymentDetails
from paypalserversdk.models.money import Money
from paypalserversdk.models.subscription_billing_information import SubscriptionBillingInformation

subscription_billing_information = SubscriptionBillingInformation(
    outstanding_balance=Money(
        currency_code='currency_code8',
        value='value4'
    ),
    failed_payments_count=None,
    last_payment=LastPaymentDetails(
        amount=Money(
            currency_code='currency_code6',
            value='value0'
        ),
        time='time2'
    ),
    next_billing_time='next_billing_time2',
    final_payment_time='final_payment_time6',
    last_failed_payment=FailedPaymentDetails(
        amount=Money(
            currency_code='currency_code6',
            value='value0'
        ),
        time='time4',
        next_payment_retry_time='next_payment_retry_time6'
    )
)
```

