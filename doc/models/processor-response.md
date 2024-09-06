
# Processor Response

The processor response information for payment requests, such as direct credit card transactions.

## Structure

`ProcessorResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `avs_code` | [`AVSCode`](../../doc/models/avs-code.md) | Optional | The address verification code for Visa, Discover, Mastercard, or American Express transactions. |
| `cvv_code` | [`CVVCode`](../../doc/models/cvv-code.md) | Optional | The card verification value code for for Visa, Discover, Mastercard, or American Express. |
| `response_code` | [`ProcessorResponseCode`](../../doc/models/processor-response-code.md) | Optional | Processor response code for the non-PayPal payment processor errors. |
| `payment_advice_code` | [`PaymentAdviceCode`](../../doc/models/payment-advice-code.md) | Optional | The declined payment transactions might have payment advice codes. The card networks, like Visa and Mastercard, return payment advice codes. |

## Example (as JSON)

```json
{
  "avs_code": "M",
  "cvv_code": "U",
  "response_code": "PPII",
  "payment_advice_code": "01"
}
```

