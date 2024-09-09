# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class StandardEntryClassCode(object):

    """Implementation of the 'Standard Entry Class Code' enum.

    NACHA (the regulatory body governing the ACH network) requires that API
    callers (merchants, partners) obtain the consumer’s explicit authorization
    before initiating a transaction. To stay compliant, you’ll need to make
    sure that you retain a compliant authorization for each transaction that
    you originate to the ACH Network using this API. ACH transactions are
    categorized (using SEC codes) by how you capture authorization from the
    Receiver (the person whose bank account is being debited or credited).
    PayPal supports the following SEC codes.

    Attributes:
        TEL: TODO: type description here.
        WEB: TODO: type description here.
        CCD: TODO: type description here.
        PPD: TODO: type description here.

    """
    TEL = 'TEL'

    WEB = 'WEB'

    CCD = 'CCD'

    PPD = 'PPD'

