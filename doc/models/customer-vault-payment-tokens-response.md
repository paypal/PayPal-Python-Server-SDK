
# Customer Vault Payment Tokens Response

Collection of payment tokens saved for a given customer.

## Structure

`CustomerVaultPaymentTokensResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_items` | `int` | Optional | Total number of items.<br><br>**Constraints**: `>= 1`, `<= 50` |
| `total_pages` | `int` | Optional | Total number of pages.<br><br>**Constraints**: `>= 1`, `<= 10` |
| `customer` | [`VaultResponseCustomer`](../../doc/models/vault-response-customer.md) | Optional | This object defines a customer in your system. Use it to manage customer profiles, save payment methods and contact details. |
| `payment_tokens` | [`List[PaymentTokenResponse]`](../../doc/models/payment-token-response.md) | Optional | **Constraints**: *Minimum Items*: `0`, *Maximum Items*: `64` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of related [HATEOAS links](https://developer.paypal.com/api/rest/responses/#hateoas).<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `32` |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.apple_pay_card import ApplePayCard
from paypalserversdk.models.apple_pay_payment_token import ApplePayPaymentToken
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_payment_token_entity import CardPaymentTokenEntity
from paypalserversdk.models.card_response_address import CardResponseAddress
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.customer_response import CustomerResponse
from paypalserversdk.models.customer_vault_payment_tokens_response import CustomerVaultPaymentTokensResponse
from paypalserversdk.models.payment_token_response import PaymentTokenResponse
from paypalserversdk.models.payment_token_response_payment_source import PaymentTokenResponsePaymentSource
from paypalserversdk.models.vault_response_customer import VaultResponseCustomer

customer_vault_payment_tokens_response = CustomerVaultPaymentTokensResponse(
    total_items=42,
    total_pages=10,
    customer=VaultResponseCustomer(
        id='id0',
        merchant_customer_id='merchant_customer_id2'
    ),
    payment_tokens=[
        PaymentTokenResponse(
            id='id4',
            customer=CustomerResponse(
                id='id0',
                merchant_customer_id='merchant_customer_id2'
            ),
            payment_source=PaymentTokenResponsePaymentSource(
                card=CardPaymentTokenEntity(
                    name='name6',
                    brand=CardBrand.CB_NATIONALE,
                    expiry='expiry4',
                    billing_address=CardResponseAddress(
                        country_code='country_code8',
                        address_line_1='address_line_12',
                        address_line_2='address_line_28',
                        admin_area_2='admin_area_28',
                        admin_area_1='admin_area_14',
                        postal_code='postal_code0'
                    )
                ),
                apple_pay=ApplePayPaymentToken(
                    card=ApplePayCard(
                        name='name6',
                        mtype=CardType.UNKNOWN,
                        brand=CardBrand.CB_NATIONALE,
                        billing_address=Address(
                            country_code='country_code8',
                            address_line_1='address_line_12',
                            address_line_2='address_line_28',
                            admin_area_2='admin_area_28',
                            admin_area_1='admin_area_14',
                            postal_code='postal_code0'
                        )
                    )
                )
            )
        ),
        PaymentTokenResponse(
            id='id4',
            customer=CustomerResponse(
                id='id0',
                merchant_customer_id='merchant_customer_id2'
            ),
            payment_source=PaymentTokenResponsePaymentSource(
                card=CardPaymentTokenEntity(
                    name='name6',
                    brand=CardBrand.CB_NATIONALE,
                    expiry='expiry4',
                    billing_address=CardResponseAddress(
                        country_code='country_code8',
                        address_line_1='address_line_12',
                        address_line_2='address_line_28',
                        admin_area_2='admin_area_28',
                        admin_area_1='admin_area_14',
                        postal_code='postal_code0'
                    )
                ),
                apple_pay=ApplePayPaymentToken(
                    card=ApplePayCard(
                        name='name6',
                        mtype=CardType.UNKNOWN,
                        brand=CardBrand.CB_NATIONALE,
                        billing_address=Address(
                            country_code='country_code8',
                            address_line_1='address_line_12',
                            address_line_2='address_line_28',
                            admin_area_2='admin_area_28',
                            admin_area_1='admin_area_14',
                            postal_code='postal_code0'
                        )
                    )
                )
            )
        )
    ]
)
```

