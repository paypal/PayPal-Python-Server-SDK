
# Search Response

The search response information.

## Structure

`SearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_details` | [`List[TransactionDetails]`](../../doc/models/transaction-details.md) | Optional | An array of transaction detail objects.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2147483647` |
| `account_number` | `str` | Optional | The merchant account number.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[a-zA-Z0-9]*$` |
| `start_date` | `str` | Optional | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does not reject all invalid dates.<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `64`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[1-2][0-9]\|3[0-1])[T,t]([0-1][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?([Zz]\|[+-][0-9]{2}:[0-9]{2})$` |
| `end_date` | `str` | Optional | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does not reject all invalid dates.<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `64`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[1-2][0-9]\|3[0-1])[T,t]([0-1][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?([Zz]\|[+-][0-9]{2}:[0-9]{2})$` |
| `last_refreshed_datetime` | `str` | Optional | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does not reject all invalid dates.<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `64`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[1-2][0-9]\|3[0-1])[T,t]([0-1][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?([Zz]\|[+-][0-9]{2}:[0-9]{2})$` |
| `page` | `int` | Optional | A zero-relative index of transactions.<br><br>**Constraints**: `>= 0`, `<= 2147483647` |
| `total_items` | `int` | Optional | The total number of transactions as an integer beginning with the specified `page` in the full result and not just in this response.<br><br>**Constraints**: `>= 0`, `<= 2147483647` |
| `total_pages` | `int` | Optional | The total number of pages, as an `integer`, when the `total_items` is divided into pages of the specified `page_size`.<br><br>**Constraints**: `>= 0`, `<= 2147483647` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related [HATEOAS links](https://developer.paypal.com/api/rest/responses/#hateoas-links).<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `32767` |

## Example

```python
from paypalserversdk.models.cart_information import CartInformation
from paypalserversdk.models.item_details import ItemDetails
from paypalserversdk.models.payer_information import PayerInformation
from paypalserversdk.models.paypal_reference_id_type import PaypalReferenceIdType
from paypalserversdk.models.phone import Phone
from paypalserversdk.models.search_response import SearchResponse
from paypalserversdk.models.shipping_information import ShippingInformation
from paypalserversdk.models.simple_postal_address_coarse_grained import SimplePostalAddressCoarseGrained
from paypalserversdk.models.store_information import StoreInformation
from paypalserversdk.models.transaction_details import TransactionDetails
from paypalserversdk.models.transaction_information import TransactionInformation

search_response = SearchResponse(
    transaction_details=[
        TransactionDetails(
            transaction_info=TransactionInformation(
                paypal_account_id='paypal_account_id4',
                paypal_reference_id='paypal_reference_id2',
                paypal_reference_id_type=PaypalReferenceIdType.ODR,
                transaction_event_code='transaction_event_code6'
            ),
            payer_info=PayerInformation(
                account_id='account_id2',
                email_address='email_address2',
                phone_number=Phone(
                    country_code='country_code2',
                    national_number='national_number6',
                    extension_number='extension_number8'
                ),
                address_status='address_status2',
                payer_status='payer_status2'
            ),
            shipping_info=ShippingInformation(
                name='name0',
                method='method4',
                address=SimplePostalAddressCoarseGrained(
                    line_1='line18',
                    city='city6',
                    country_code='country_code6',
                    line_2='line20',
                    state='state2',
                    postal_code='postal_code8'
                ),
                secondary_shipping_address=SimplePostalAddressCoarseGrained(
                    line_1='line16',
                    city='city4',
                    country_code='country_code4',
                    line_2='line28',
                    state='state0',
                    postal_code='postal_code6'
                )
            ),
            cart_info=CartInformation(
                item_details=[
                    ItemDetails(
                        item_code='item_code0',
                        item_name='item_name8',
                        item_description='item_description4',
                        item_options='item_options2',
                        item_quantity='item_quantity2'
                    ),
                    ItemDetails(
                        item_code='item_code0',
                        item_name='item_name8',
                        item_description='item_description4',
                        item_options='item_options2',
                        item_quantity='item_quantity2'
                    )
                ],
                tax_inclusive=False,
                paypal_invoice_id='paypal_invoice_id6'
            ),
            store_info=StoreInformation(
                store_id='store_id2',
                terminal_id='terminal_id6'
            )
        )
    ],
    account_number='account_number8',
    start_date='start_date4',
    end_date='end_date8',
    last_refreshed_datetime='last_refreshed_datetime2'
)
```

