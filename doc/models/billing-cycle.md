
# Billing Cycle

The billing cycle providing details of the billing frequency, amount, duration and if the billing cycle is a free, discounted or regular billing cycle. The sequence of the billing cycle will be in the following order - free trial billing cycle(s), discounted trial billing cycle(s), regular billing cycle(s).

## Structure

`BillingCycle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tenure_type` | [`TenureType`](../../doc/models/tenure-type.md) | Required | The tenure type of the billing cycle identifies if the billing cycle is a trial(free or discounted) or regular billing cycle.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Optional | The pricing scheme details. |
| `total_cycles` | `int` | Optional | The number of times this billing cycle gets executed. Trial billing cycles can only be executed a finite number of times (value between 1 and 999 for total_cycles). Regular billing cycles can be executed infinite times (value of 0 for total_cycles) or a finite number of times (value between 1 and 999 for total_cycles).<br><br>**Default**: `1`<br><br>**Constraints**: `>= 0`, `<= 999` |
| `sequence` | `int` | Optional | The order in which this cycle is to run among other billing cycles. For example, a trial billing cycle has a `sequence` of `1` while a regular billing cycle has a `sequence` of `2`, so that trial cycle runs before the regular cycle.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1`, `<= 3` |
| `start_date` | `str` | Optional | The stand-alone date, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). To represent special legal values, such as a date of birth, you should use dates with no associated time or time-zone data. Whenever possible, use the standard `date_time` type. This regular expression does not validate all dates. For example, February 31 is valid and nothing is known about leap years.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[1-2][0-9]\|3[0-1])$` |
| `frequency` | [`CycleFrequency`](../../doc/models/cycle-frequency.md) | Optional | The frequency of the terms reset cycle. |

## Example

```python
from paypalserversdk.models.billing_cycle import BillingCycle
from paypalserversdk.models.cycle_frequency import CycleFrequency
from paypalserversdk.models.frequency_interval_unit import FrequencyIntervalUnit
from paypalserversdk.models.money import Money
from paypalserversdk.models.pricing_model import PricingModel
from paypalserversdk.models.pricing_scheme import PricingScheme
from paypalserversdk.models.tenure_type import TenureType

billing_cycle = BillingCycle(
    tenure_type=TenureType.REGULAR,
    pricing_scheme=PricingScheme(
        pricing_model=PricingModel.AUTO_RELOAD,
        price=Money(
            currency_code='currency_code8',
            value='value4'
        ),
        reload_threshold_amount=Money(
            currency_code='currency_code0',
            value='value6'
        )
    ),
    total_cycles=1,
    sequence=1,
    start_date='start_date2',
    frequency=CycleFrequency(
        interval_unit=FrequencyIntervalUnit.LIFETIME,
        interval_count=94
    )
)
```

