# PayPal Python Server SDK API Reference

## Installation
```bash
pip install paypalserversdk
```

## Quick Start

### Client Initialization
```python
from paypalserversdk.paypal_serversdk_client import PaypalServersdkClient
from paypalserversdk.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from paypalserversdk.configuration import Environment

# Initialize client
client = PaypalServersdkClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='your_client_id',
        o_auth_client_secret='your_client_secret'
    ),
    environment=Environment.SANDBOX  # or Environment.PRODUCTION
)
```

## Core API Controllers

### Orders Controller (`client.orders`)
Manage PayPal orders lifecycle.

```python
# Create order
response = client.orders.create_order({
    'body': OrderRequest(...),
    'paypal_request_id': 'unique_request_id'
})

# Get order details
response = client.orders.get_order({
    'id': 'order_id'
})

# Authorize order
response = client.orders.authorize_order({
    'id': 'order_id',
    'body': OrderAuthorizeRequest(...)
})

# Capture order
response = client.orders.capture_order({
    'id': 'order_id',
    'body': OrderCaptureRequest(...)
})

# Update order
response = client.orders.patch_order({
    'id': 'order_id',
    'body': [Patch(...)]
})

# Confirm payment source
response = client.orders.confirm_order({
    'id': 'order_id',
    'body': ConfirmOrderRequest(...)
})

# Add tracking
response = client.orders.create_order_tracking({
    'id': 'order_id',
    'body': OrderTrackerRequest(...)
})

# Update tracking
response = client.orders.update_order_tracking({
    'id': 'order_id',
    'tracker_id': 'tracker_id',
    'body': OrderTrackerRequest(...)
})
```

### Payments Controller (`client.payments`)
Manage payment operations.

```python
# Capture authorized payment
response = client.payments.capture_authorized_payment({
    'authorization_id': 'auth_id',
    'body': CaptureRequest(...)
})

# Get captured payment
response = client.payments.get_captured_payment({
    'capture_id': 'capture_id'
})

# Reauthorize payment
response = client.payments.reauthorize_payment({
    'authorization_id': 'auth_id',
    'body': ReauthorizeRequest(...)
})

# Void authorization
response = client.payments.void_payment({
    'authorization_id': 'auth_id'
})

# Refund captured payment
response = client.payments.refund_captured_payment({
    'capture_id': 'capture_id',
    'body': RefundRequest(...)
})

# Get authorization details
response = client.payments.get_authorized_payment({
    'authorization_id': 'auth_id'
})

# Get refund details
response = client.payments.get_refund({
    'refund_id': 'refund_id'
})
```

### Vault Controller (`client.vault`)
Manage payment method tokens.

```python
# Create setup token
response = client.vault.create_setup_token({
    'body': SetupTokenRequest(...)
})

# Get setup token
response = client.vault.get_setup_token({
    'id': 'setup_token_id'
})

# Create payment token
response = client.vault.create_payment_token({
    'body': PaymentTokenRequest(...)
})

# Get payment token
response = client.vault.get_payment_token({
    'id': 'payment_token_id'
})

# List customer payment tokens
response = client.vault.list_customer_payment_tokens({
    'customer_id': 'customer_id',
    'page_size': 10,
    'page': 1
})

# Delete payment token
response = client.vault.delete_payment_token({
    'id': 'payment_token_id'
})
```

## Core Models

### Money
```python
from paypalserversdk.models.money import Money

money = Money(
    currency_code='USD',  # ISO-4217 currency code
    value='100.00'       # String representation of amount
)
```

### Address
```python
from paypalserversdk.models.address import Address

address = Address(
    country_code='US',           # Required: ISO 3166-1 country code
    address_line_1='123 Main St',
    address_line_2='Apt 4B',
    admin_area_2='San Jose',     # City
    admin_area_1='CA',          # State/Province
    postal_code='95131'
)
```

### Name
```python
from paypalserversdk.models.name import Name

name = Name(
    given_name='John',
    surname='Doe'
)
```

### OrderRequest
```python
from paypalserversdk.models.order_request import OrderRequest
from paypalserversdk.models.checkout_payment_intent import CheckoutPaymentIntent
from paypalserversdk.models.purchase_unit_request import PurchaseUnitRequest
from paypalserversdk.models.amount_with_breakdown import AmountWithBreakdown

order = OrderRequest(
    intent=CheckoutPaymentIntent.CAPTURE,  # or AUTHORIZE
    purchase_units=[
        PurchaseUnitRequest(
            amount=AmountWithBreakdown(
                currency_code='USD',
                value='100.00'
            ),
            reference_id='PUHF',
            description='Sporting Goods'
        )
    ],
    payer=Payer(...),              # Optional
    payment_source=PaymentSource(...),  # Optional
    application_context=OrderApplicationContext(...)  # Optional
)
```

## Payment Sources

### Card Payment
```python
from paypalserversdk.models.card_request import CardRequest
from paypalserversdk.models.payment_source import PaymentSource

card = CardRequest(
    name='John Doe',
    number='4111111111111111',  # Requires PCI compliance
    expiry='2025-12',
    security_code='123',
    billing_address=address
)

payment_source = PaymentSource(card=card)
```

### Apple Pay
```python
from paypalserversdk.models.apple_pay_request import ApplePayRequest
from paypalserversdk.models.payment_source import PaymentSource

apple_pay = ApplePayRequest(
    id='apple_pay_transaction_id',
    name='John Doe',
    email_address='john@example.com',
    decrypted_token=ApplePayDecryptedTokenData(...)
)

payment_source = PaymentSource(apple_pay=apple_pay)
```

### Google Pay
```python
from paypalserversdk.models.google_pay_request import GooglePayRequest
from paypalserversdk.models.payment_source import PaymentSource

google_pay = GooglePayRequest(
    name='John Doe',
    email_address='john@example.com',
    decrypted_token=GooglePayDecryptedTokenData(...)
)

payment_source = PaymentSource(google_pay=google_pay)
```

### PayPal Wallet
```python
from paypalserversdk.models.paypal_wallet import PaypalWallet
from paypalserversdk.models.payment_source import PaymentSource

paypal_wallet = PaypalWallet(
    email_address='customer@example.com',
    name=name,
    phone=phone_with_type,
    address=address
)

payment_source = PaymentSource(paypal=paypal_wallet)
```

## Request Models

### CaptureRequest
```python
from paypalserversdk.models.capture_request import CaptureRequest

capture = CaptureRequest(
    invoice_id='INV-001',
    note_to_payer='Payment for order #123',
    amount=Money(currency_code='USD', value='50.00'),
    final_capture=True,
    soft_descriptor='MYSTORE'
)
```

### RefundRequest
```python
from paypalserversdk.models.refund_request import RefundRequest

refund = RefundRequest(
    amount=Money(currency_code='USD', value='25.00'),  # Partial refund
    custom_id='REFUND-001',
    invoice_id='INV-001',
    note_to_payer='Refund for damaged item'
)
```

## Error Handling

```python
from paypalserversdk.exceptions.api_exception import ApiException
from paypalserversdk.exceptions.error_exception import ErrorException

try:
    response = client.orders.create_order(options)
    order = response.body
except ApiException as e:
    print(f'API Error: {e.response_code} - {e.reason_phrase}')
    print(f'Error details: {e.response_body}')
except ErrorException as e:
    print(f'Error: {e.reason}')
    print(f'Error details: {e.error}')
```

## Response Handling

```python
# All API methods return ApiResponse objects
response = client.orders.create_order(options)

# Access response data
order = response.body
status_code = response.status_code
headers = response.headers

# Check if successful
if response.status_code == 201:
    print(f'Order created: {order.id}')
    print(f'Status: {order.status}')
    print(f'Links: {order.links}')
```

## Configuration Options

### Environment
```python
from paypalserversdk.configuration import Environment

# Sandbox (default)
client = PaypalServersdkClient(
    environment=Environment.SANDBOX,
    # ... other options
)

# Production
client = PaypalServersdkClient(
    environment=Environment.PRODUCTION,
    # ... other options
)
```

### HTTP Configuration
```python
client = PaypalServersdkClient(
    timeout=30,                    # Connection timeout
    max_retries=3,                # Retry attempts
    backoff_factor=2,             # Backoff multiplier
    retry_statuses=[408, 429, 500, 502, 503, 504],
    retry_methods=['GET', 'PUT'],
    # ... other options
)
```

### Logging
```python
from paypalserversdk.logging.configuration.api_logging_configuration import ApiLoggingConfiguration

logging_config = ApiLoggingConfiguration(
    log_level='INFO',
    enable_request_logging=True,
    enable_response_logging=True
)

client = PaypalServersdkClient(
    logging_configuration=logging_config,
    # ... other options
)
```

## Common Patterns

### Create and Capture Order
```python
# 1. Create order
order_request = OrderRequest(
    intent=CheckoutPaymentIntent.CAPTURE,
    purchase_units=[...],
    payment_source=payment_source
)

response = client.orders.create_order({
    'body': order_request,
    'paypal_request_id': str(uuid.uuid4())
})

order = response.body

# 2. Capture immediately (if payment source provided)
if order.status == 'APPROVED':
    capture_response = client.orders.capture_order({
        'id': order.id
    })
    captured_order = capture_response.body
```

### Authorize and Capture Later
```python
# 1. Create order with AUTHORIZE intent
order_request = OrderRequest(
    intent=CheckoutPaymentIntent.AUTHORIZE,
    purchase_units=[...]
)

order_response = client.orders.create_order({
    'body': order_request
})

# 2. Customer approves payment (redirect flow)
# 3. Authorize the order
auth_response = client.orders.authorize_order({
    'id': order_response.body.id
})

# 4. Capture authorized payment later
auth_id = auth_response.body.purchase_units[0].payments.authorizations[0].id
capture_response = client.payments.capture_authorized_payment({
    'authorization_id': auth_id,
    'body': CaptureRequest(...)
})
```

### Vault Payment Method
```python
# 1. Create setup token
setup_response = client.vault.create_setup_token({
    'body': SetupTokenRequest(
        payment_source=PaymentSource(card=CardRequest(...))
    )
})

# 2. Customer completes setup (redirect flow)
# 3. Create payment token
token_response = client.vault.create_payment_token({
    'body': PaymentTokenRequest(
        payment_source=PaymentSource(...)
    )
})

# 4. Use vaulted payment method
order_request = OrderRequest(
    intent=CheckoutPaymentIntent.CAPTURE,
    purchase_units=[...],
    payment_source=PaymentSource(
        card=CardRequest(vault_id=token_response.body.id)
    )
)
```

This SDK provides comprehensive access to PayPal's REST APIs with automatic OAuth2 authentication, retry logic, and robust error handling.
