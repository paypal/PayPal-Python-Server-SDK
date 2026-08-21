
# Payment Preferences Override

The payment preferences to override at subscription level.

## Structure

`PaymentPreferencesOverride`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_bill_outstanding` | `bool` | Optional | Indicates whether to automatically bill the outstanding amount in the next billing cycle. |
| `setup_fee` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `setup_fee_failure_action` | [`SetupFeeFailureAction`](../../doc/models/setup-fee-failure-action.md) | Optional | The action to take on the subscription if the initial payment for the setup fails.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `payment_failure_threshold` | `int` | Optional | The maximum number of payment failures before a subscription is suspended. For example, if `payment_failure_threshold` is `2`, the subscription automatically updates to the `SUSPEND` state if two consecutive payments fail.<br><br>**Constraints**: `>= 0`, `<= 999` |

## Example

```python
from paypalserversdk.models.money import Money
from paypalserversdk.models.payment_preferences_override import PaymentPreferencesOverride
from paypalserversdk.models.setup_fee_failure_action import SetupFeeFailureAction

payment_preferences_override = PaymentPreferencesOverride(
    auto_bill_outstanding=False,
    setup_fee=Money(
        currency_code='currency_code8',
        value='value4'
    ),
    setup_fee_failure_action=SetupFeeFailureAction.CONTINUE,
    payment_failure_threshold=78
)
```

