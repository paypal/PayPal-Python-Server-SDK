# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.apple_pay_payment_object import ApplePayPaymentObject
from paypalserversdk.models.bancontact_payment_object import BancontactPaymentObject
from paypalserversdk.models.blik_payment_object import BLIKPaymentObject
from paypalserversdk.models.card_response import CardResponse
from paypalserversdk.models.eps_payment_object import EPSPaymentObject
from paypalserversdk.models.giropay_payment_object import GiropayPaymentObject
from paypalserversdk.models.google_pay_wallet_response import GooglePayWalletResponse
from paypalserversdk.models.ideal_payment_object import IdealPaymentObject
from paypalserversdk.models.mybank_payment_object import MybankPaymentObject
from paypalserversdk.models.p_24_payment_object import P24PaymentObject
from paypalserversdk.models.paypal_wallet_response import PaypalWalletResponse
from paypalserversdk.models.sofort_payment_object import SofortPaymentObject
from paypalserversdk.models.trustly_payment_object import TrustlyPaymentObject
from paypalserversdk.models.venmo_wallet_response import VenmoWalletResponse


class PaymentSourceResponse(object):

    """Implementation of the 'Payment Source Response' model.

    The payment source used to fund the payment.

    Attributes:
        card (CardResponse): The payment card to use to fund a payment. Card
            can be a credit or debit card.
        paypal (PaypalWalletResponse): The PayPal Wallet response.
        bancontact (BancontactPaymentObject): Information used to pay
            Bancontact.
        blik (BLIKPaymentObject): Information used to pay using BLIK.
        eps (EPSPaymentObject): Information used to pay using eps.
        giropay (GiropayPaymentObject): Information needed to pay using
            giropay.
        ideal (IdealPaymentObject): Information used to pay using iDEAL.
        mybank (MybankPaymentObject): Information used to pay using MyBank.
        p_24 (P24PaymentObject): Information used to pay using
            P24(Przelewy24).
        sofort (SofortPaymentObject): Information used to pay using Sofort.
        trustly (TrustlyPaymentObject): Information needed to pay using
            Trustly.
        apple_pay (ApplePayPaymentObject): Information needed to pay using
            ApplePay.
        google_pay (GooglePayWalletResponse): Google Pay Wallet payment data.
        venmo (VenmoWalletResponse): Venmo wallet response.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card": 'card',
        "paypal": 'paypal',
        "bancontact": 'bancontact',
        "blik": 'blik',
        "eps": 'eps',
        "giropay": 'giropay',
        "ideal": 'ideal',
        "mybank": 'mybank',
        "p_24": 'p24',
        "sofort": 'sofort',
        "trustly": 'trustly',
        "apple_pay": 'apple_pay',
        "google_pay": 'google_pay',
        "venmo": 'venmo'
    }

    _optionals = [
        'card',
        'paypal',
        'bancontact',
        'blik',
        'eps',
        'giropay',
        'ideal',
        'mybank',
        'p_24',
        'sofort',
        'trustly',
        'apple_pay',
        'google_pay',
        'venmo',
    ]

    def __init__(self,
                 card=APIHelper.SKIP,
                 paypal=APIHelper.SKIP,
                 bancontact=APIHelper.SKIP,
                 blik=APIHelper.SKIP,
                 eps=APIHelper.SKIP,
                 giropay=APIHelper.SKIP,
                 ideal=APIHelper.SKIP,
                 mybank=APIHelper.SKIP,
                 p_24=APIHelper.SKIP,
                 sofort=APIHelper.SKIP,
                 trustly=APIHelper.SKIP,
                 apple_pay=APIHelper.SKIP,
                 google_pay=APIHelper.SKIP,
                 venmo=APIHelper.SKIP):
        """Constructor for the PaymentSourceResponse class"""

        # Initialize members of the class
        if card is not APIHelper.SKIP:
            self.card = card 
        if paypal is not APIHelper.SKIP:
            self.paypal = paypal 
        if bancontact is not APIHelper.SKIP:
            self.bancontact = bancontact 
        if blik is not APIHelper.SKIP:
            self.blik = blik 
        if eps is not APIHelper.SKIP:
            self.eps = eps 
        if giropay is not APIHelper.SKIP:
            self.giropay = giropay 
        if ideal is not APIHelper.SKIP:
            self.ideal = ideal 
        if mybank is not APIHelper.SKIP:
            self.mybank = mybank 
        if p_24 is not APIHelper.SKIP:
            self.p_24 = p_24 
        if sofort is not APIHelper.SKIP:
            self.sofort = sofort 
        if trustly is not APIHelper.SKIP:
            self.trustly = trustly 
        if apple_pay is not APIHelper.SKIP:
            self.apple_pay = apple_pay 
        if google_pay is not APIHelper.SKIP:
            self.google_pay = google_pay 
        if venmo is not APIHelper.SKIP:
            self.venmo = venmo 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        card = CardResponse.from_dictionary(dictionary.get('card')) if 'card' in dictionary.keys() else APIHelper.SKIP
        paypal = PaypalWalletResponse.from_dictionary(dictionary.get('paypal')) if 'paypal' in dictionary.keys() else APIHelper.SKIP
        bancontact = BancontactPaymentObject.from_dictionary(dictionary.get('bancontact')) if 'bancontact' in dictionary.keys() else APIHelper.SKIP
        blik = BLIKPaymentObject.from_dictionary(dictionary.get('blik')) if 'blik' in dictionary.keys() else APIHelper.SKIP
        eps = EPSPaymentObject.from_dictionary(dictionary.get('eps')) if 'eps' in dictionary.keys() else APIHelper.SKIP
        giropay = GiropayPaymentObject.from_dictionary(dictionary.get('giropay')) if 'giropay' in dictionary.keys() else APIHelper.SKIP
        ideal = IdealPaymentObject.from_dictionary(dictionary.get('ideal')) if 'ideal' in dictionary.keys() else APIHelper.SKIP
        mybank = MybankPaymentObject.from_dictionary(dictionary.get('mybank')) if 'mybank' in dictionary.keys() else APIHelper.SKIP
        p_24 = P24PaymentObject.from_dictionary(dictionary.get('p24')) if 'p24' in dictionary.keys() else APIHelper.SKIP
        sofort = SofortPaymentObject.from_dictionary(dictionary.get('sofort')) if 'sofort' in dictionary.keys() else APIHelper.SKIP
        trustly = TrustlyPaymentObject.from_dictionary(dictionary.get('trustly')) if 'trustly' in dictionary.keys() else APIHelper.SKIP
        apple_pay = ApplePayPaymentObject.from_dictionary(dictionary.get('apple_pay')) if 'apple_pay' in dictionary.keys() else APIHelper.SKIP
        google_pay = GooglePayWalletResponse.from_dictionary(dictionary.get('google_pay')) if 'google_pay' in dictionary.keys() else APIHelper.SKIP
        venmo = VenmoWalletResponse.from_dictionary(dictionary.get('venmo')) if 'venmo' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(card,
                   paypal,
                   bancontact,
                   blik,
                   eps,
                   giropay,
                   ideal,
                   mybank,
                   p_24,
                   sofort,
                   trustly,
                   apple_pay,
                   google_pay,
                   venmo)
