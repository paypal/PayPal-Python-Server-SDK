
# Apple Pay Payment Data

Information about the decrypted apple pay payment data for the token like cryptogram, eci indicator.

## Structure

`ApplePayPaymentData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cryptogram` | `str` | Optional | Online payment cryptogram, as defined by 3D Secure. The pattern is defined by an external party and supports Unicode.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2000`, *Pattern*: `^.*$` |
| `eci_indicator` | `str` | Optional | ECI indicator, as defined by 3- Secure. The pattern is defined by an external party and supports Unicode.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `256`, *Pattern*: `^.*$` |
| `emv_data` | `str` | Optional | Encoded Apple Pay EMV Payment Structure used for payments in China. The pattern is defined by an external party and supports Unicode.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2000`, *Pattern*: `^.*$` |
| `pin` | `str` | Optional | Bank Key encrypted Apple Pay PIN. The pattern is defined by an external party and supports Unicode.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2000`, *Pattern*: `^.*$` |

## Example (as JSON)

```json
{
  "cryptogram": "cryptogram6",
  "eci_indicator": "eci_indicator0",
  "emv_data": "emv_data0",
  "pin": "pin4"
}
```
