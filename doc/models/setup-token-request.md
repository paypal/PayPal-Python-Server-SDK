
# Setup Token Request

Setup Token Request where the `source` defines the type of instrument to be stored.

## Structure

`SetupTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`Customer`](../../doc/models/customer.md) | Optional | This object defines a customer in your system. Use it to manage customer profiles, save payment methods and contact details. |
| `payment_source` | [`SetupTokenRequestPaymentSource`](../../doc/models/setup-token-request-payment-source.md) | Required | The payment method to vault with the instrument details. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.apple_pay_request_card import ApplePayRequestCard
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.customer import Customer
from paypalserversdk.models.fulfillment_type import FulfillmentType
from paypalserversdk.models.paypal_payment_token_usage_type import PaypalPaymentTokenUsageType
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypalserversdk.models.setup_token_request import SetupTokenRequest
from paypalserversdk.models.setup_token_request_card import SetupTokenRequestCard
from paypalserversdk.models.setup_token_request_payment_source import SetupTokenRequestPaymentSource
from paypalserversdk.models.shipping_name import ShippingName
from paypalserversdk.models.usage_pattern import UsagePattern
from paypalserversdk.models.vault_apple_pay_request import VaultApplePayRequest
from paypalserversdk.models.vault_paypal_wallet_request import VaultPaypalWalletRequest
from paypalserversdk.models.vault_token_request import VaultTokenRequest
from paypalserversdk.models.vault_token_request_type import VaultTokenRequestType
from paypalserversdk.models.vault_venmo_request import VaultVenmoRequest
from paypalserversdk.models.vaulted_digital_wallet_shipping_details import VaultedDigitalWalletShippingDetails

setup_token_request = SetupTokenRequest(
    payment_source=SetupTokenRequestPaymentSource(
        card=SetupTokenRequestCard(
            name='name6',
            number='number6',
            expiry='expiry4',
            security_code='security_code8',
            brand=CardBrand.CB_NATIONALE
        ),
        paypal=VaultPaypalWalletRequest(
            description='description2',
            usage_pattern=UsagePattern.THRESHOLD_PREPAID,
            shipping=VaultedDigitalWalletShippingDetails(
                name=ShippingName(
                    full_name='full_name6'
                ),
                email_address='email_address2',
                phone_number=PhoneNumberWithCountryCode(
                    country_code='country_code2',
                    national_number='national_number6'
                ),
                mtype=FulfillmentType.SHIPPING,
                address=Address(
                    country_code='country_code6',
                    address_line_1='address_line_16',
                    address_line_2='address_line_26',
                    admin_area_2='admin_area_20',
                    admin_area_1='admin_area_12',
                    postal_code='postal_code8'
                )
            ),
            permit_multiple_payment_tokens=False,
            usage_type=PaypalPaymentTokenUsageType.MERCHANT
        ),
        venmo=VaultVenmoRequest(
            description='description6',
            usage_pattern=UsagePattern.UNSCHEDULED_PREPAID,
            shipping=VaultedDigitalWalletShippingDetails(
                name=ShippingName(
                    full_name='full_name6'
                ),
                email_address='email_address2',
                phone_number=PhoneNumberWithCountryCode(
                    country_code='country_code2',
                    national_number='national_number6'
                ),
                mtype=FulfillmentType.SHIPPING,
                address=Address(
                    country_code='country_code6',
                    address_line_1='address_line_16',
                    address_line_2='address_line_26',
                    admin_area_2='admin_area_20',
                    admin_area_1='admin_area_12',
                    postal_code='postal_code8'
                )
            ),
            permit_multiple_payment_tokens=False,
            usage_type=PaypalPaymentTokenUsageType.MERCHANT
        ),
        apple_pay=VaultApplePayRequest(
            token='token6',
            card=ApplePayRequestCard(
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
        ),
        token=VaultTokenRequest(
            id='id6',
            mtype=VaultTokenRequestType.SETUP_TOKEN
        )
    ),
    customer=Customer(
        id='id0',
        merchant_customer_id='merchant_customer_id2'
    )
)
```

