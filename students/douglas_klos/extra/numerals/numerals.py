#!/usr/bin/env python3
#pylint: disable=R0912

""" Class to convert between Roman and Arabic numerals """

# Douglas Klos
# March 6th, 2019
# Python 210, Session 8
# numerals.py


class Numerals():
    """
    Class to convert between Roman and Arabic numerals

    Subtractive roman numerals with a standard upper limit of 4999
    """

    ROMAN_NUMERAL_LIST = {'M': 1000,
                          'D': 500,
                          'C': 100,
                          'L': 50,
                          'X': 10,
                          'V': 5,
                          'I': 1}

    def __init__(self, value=0):
        if isinstance(value, int):
            if value > 4999:
                raise ValueError
            self._arabic = value

        if isinstance(value, str):
            self._arabic = self.convert_to_arabic(value)

    def __str__(self):
        return str(self.arabic)

    def convert_to_arabic(self, value):
        """ Given an input Roman Numeral, conert to arabic and set self._arabic """
        return_arabic = 0

        for i in range(len(value)-1):
            if self.ROMAN_NUMERAL_LIST[value[i]] < self.ROMAN_NUMERAL_LIST[value[i + 1]]:
                return_arabic -= self.ROMAN_NUMERAL_LIST[value[i]]
            else:
                return_arabic += self.ROMAN_NUMERAL_LIST[value[i]]
            self.arabic = return_arabic + self.ROMAN_NUMERAL_LIST[value[-1]]
        if self.arabic < 5000:
            return self.arabic
        raise ValueError

    @property
    def arabic(self):
        """ Returns the roman numerals """
        return self._arabic

    @arabic.setter
    def arabic(self, value):
        self._arabic = value

    @property
    def roman(self):
        """ Returns the roman numeral for self._arabic """
        number = self._arabic
        roman_numeral = ''
        while number >= 1000:
            roman_numeral += 'M'
            number -= 1000

        while number >= 900:
            roman_numeral += 'CM'
            number -= 900

        while number >= 500:
            roman_numeral += 'D'
            number -= 500

        while number >= 400:
            roman_numeral += 'CD'
            number -= 400

        while number >= 100:
            roman_numeral += 'C'
            number -= 100

        while number >= 90:
            roman_numeral += 'XC'
            number -= 90

        while number >= 50:
            roman_numeral += 'L'
            number -= 50

        while number >= 40:
            roman_numeral += 'XL'
            number -= 40

        while number >= 10:
            roman_numeral += 'X'
            number -= 10

        while number >= 9:
            roman_numeral += 'IX'
            number -= 10

        while number >= 5:
            roman_numeral += 'V'
            number -= 5

        while number >= 4:
            roman_numeral += 'IV'
            number -= 4

        while number >= 1:
            roman_numeral += 'I'
            number -= 1

        return roman_numeral
