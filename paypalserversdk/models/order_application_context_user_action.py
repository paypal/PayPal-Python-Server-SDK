# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class OrderApplicationContextUserAction(object):

    """Implementation of the 'Order Application Context User Action' enum.

    DEPRECATED. Configures a <strong>Continue</strong> or <strong>Pay
    Now</strong> checkout flow.  The fields in `application_context` are now
    available in the `experience_context` object under the `payment_source`
    which supports them (eg.
    `payment_source.paypal.experience_context.user_action`). Please specify
    this field in the `experience_context` object instead of the
    `application_context` object.

    Attributes:
        CONTINUE: TODO: type description here.
        PAY_NOW: TODO: type description here.

    """
    CONTINUE = 'CONTINUE'

    PAY_NOW = 'PAY_NOW'

