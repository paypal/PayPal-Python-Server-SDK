
# Setup Token Response Card

## Structure

`SetupTokenResponseCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The card holder's name as it appears on the card.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `300`, *Pattern*: `^[A-Za-z ]+$` |
| `last_digits` | `str` | Optional | The last digits of the payment card.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `4`, *Pattern*: `[0-9]{2,}` |
| `brand` | [`CardBrand`](../../doc/models/card-brand.md) | Optional | The card network or brand. Applies to credit, debit, gift, and payment cards.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[A-Z_]+$` |
| `expiry` | `str` | Optional | The year and month, in ISO-8601 `YYYY-MM` date format. See [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6).<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])$` |
| `billing_address` | [`CardResponseAddress`](../../doc/models/card-response-address.md) | Optional | Address request details. |
| `verification_status` | [`CardVerificationStatus`](../../doc/models/card-verification-status.md) | Optional | Verification status of Card.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `verification` | [`CardVerificationDetails`](../../doc/models/card-verification-details.md) | Optional | Card Verification details including the authorization details and 3D SECURE details. |
| `network_transaction_reference` | [`NetworkTransactionReferenceEntity`](../../doc/models/network-transaction-reference-entity.md) | Optional | Previous network transaction reference including id in response. |
| `authentication_result` | [`CardAuthenticationResponse`](../../doc/models/card-authentication-response.md) | Optional | Results of Authentication such as 3D Secure. |
| `bin_details` | [`BinDetails`](../../doc/models/bin-details.md) | Optional | Bank Identification Number (BIN) details used to fund a payment. |
| `mtype` | [`CardType`](../../doc/models/card-type.md) | Optional | Type of card. i.e Credit, Debit and so on.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[A-Z_]+$` |

## Example (as JSON)

```json
{
  "name": "name8",
  "last_digits": "last_digits2",
  "brand": "DISCOVER",
  "expiry": "expiry6",
  "billing_address": {
    "address_line_1": "address_line_12",
    "address_line_2": "address_line_28",
    "admin_area_2": "admin_area_28",
    "admin_area_1": "admin_area_14",
    "postal_code": "postal_code0",
    "country_code": "country_code8"
  }
}
```

