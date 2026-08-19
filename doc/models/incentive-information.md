
# Incentive Information

The incentive details.

## Structure

`IncentiveInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `incentive_details` | [`List[IncentiveDetails]`](../../doc/models/incentive-details.md) | Optional | An array of incentive details.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `32767` |

## Example

```python
from paypalserversdk.models.incentive_details import IncentiveDetails
from paypalserversdk.models.incentive_information import IncentiveInformation
from paypalserversdk.models.money import Money

incentive_information = IncentiveInformation(
    incentive_details=[
        IncentiveDetails(
            incentive_type='incentive_type4',
            incentive_code='incentive_code0',
            incentive_amount=Money(
                currency_code='currency_code4',
                value='value0'
            ),
            incentive_program_code='incentive_program_code4'
        ),
        IncentiveDetails(
            incentive_type='incentive_type4',
            incentive_code='incentive_code0',
            incentive_amount=Money(
                currency_code='currency_code4',
                value='value0'
            ),
            incentive_program_code='incentive_program_code4'
        ),
        IncentiveDetails(
            incentive_type='incentive_type4',
            incentive_code='incentive_code0',
            incentive_amount=Money(
                currency_code='currency_code4',
                value='value0'
            ),
            incentive_program_code='incentive_program_code4'
        )
    ]
)
```

