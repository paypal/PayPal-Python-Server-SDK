
# Supplementary Data

Supplementary data about a payment. This object passes information that can be used to improve risk assessments and processing costs, for example, by providing Level 2 and Level 3 payment data.

## Structure

`SupplementaryData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`CardSupplementaryData`](../../doc/models/card-supplementary-data.md) | Optional | Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For more information about processing payments, see checkout or multiparty checkout. |
| `risk` | [`RiskSupplementaryData`](../../doc/models/risk-supplementary-data.md) | Optional | Additional information necessary to evaluate the risk profile of a transaction. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.card_supplementary_data import CardSupplementaryData
from paypalserversdk.models.level_2_card_processing_data import Level2CardProcessingData
from paypalserversdk.models.level_3_card_processing_data import Level3CardProcessingData
from paypalserversdk.models.money import Money
from paypalserversdk.models.participant_metadata import ParticipantMetadata
from paypalserversdk.models.risk_supplementary_data import RiskSupplementaryData
from paypalserversdk.models.supplementary_data import SupplementaryData

supplementary_data = SupplementaryData(
    card=CardSupplementaryData(
        level_2=Level2CardProcessingData(
            invoice_id='invoice_id4',
            tax_total=Money(
                currency_code='currency_code4',
                value='value0'
            )
        ),
        level_3=Level3CardProcessingData(
            shipping_amount=Money(
                currency_code='currency_code0',
                value='value6'
            ),
            duty_amount=Money(
                currency_code='currency_code6',
                value='value2'
            ),
            discount_amount=Money(
                currency_code='currency_code2',
                value='value8'
            ),
            shipping_address=Address(
                country_code='country_code0',
                address_line_1='address_line_10',
                address_line_2='address_line_20',
                admin_area_2='admin_area_24',
                admin_area_1='admin_area_16',
                postal_code='postal_code2'
            ),
            ships_from_postal_code='ships_from_postal_code4'
        )
    ),
    risk=RiskSupplementaryData(
        customer=ParticipantMetadata(
            ip_address='ip_address0'
        )
    )
)
```

