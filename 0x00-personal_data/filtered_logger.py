#!/usr/bin/env python3
"""
This module provides a function to obfuscate sensitive data in log messages.
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Replace occurrences of specified field values
    in log message with redaction

    Args:
        fields (list of str): List of fields to obfuscate.
        redaction (str): String representing the obfuscation for fields.
        message (str): Log message to be obfuscated.
        separator (str): Character separating all fields in the log message.

    Returns:
        str: Obfuscated log message.
    """
    return re.sub(
        r'(?<=^|{})(?:{}).*?(?={}|$)'.format(separator, '|'.join(fields),
                                             separator),
        redaction,
        message
    )
