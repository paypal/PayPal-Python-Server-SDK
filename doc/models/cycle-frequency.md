
# Cycle Frequency

The frequency of the terms reset cycle.

## Structure

`CycleFrequency`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `interval_unit` | [`FrequencyIntervalUnit`](../../doc/models/frequency-interval-unit.md) | Required | The interval unit at which the the usage limits will be reset.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `interval_count` | `int` | Optional | The interval count at which the terms will be reset, this is ignored if the unit is LIFETIME.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1`, `<= 365` |

## Example

```python
from paypalserversdk.models.cycle_frequency import CycleFrequency
from paypalserversdk.models.frequency_interval_unit import FrequencyIntervalUnit

cycle_frequency = CycleFrequency(
    interval_unit=FrequencyIntervalUnit.MONTH,
    interval_count=1
)
```

