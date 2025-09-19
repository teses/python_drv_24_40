

class FachinformatikerRechner():

    @staticmethod
    def binary_to_decimal(binary: str):
        """

        >>> binary_to_decimal("0")
        0
        >>> binary_to_decimal("1010")
        10
        >>> binary_to_decimal("1111")
        15

        :param binary:
        :return:
        """
        binary = binary[::-1]
        decimalNumber = 0
        for index, value in enumerate(binary):
            decimalNumber += int(value) * (2 ** index)
        return decimalNumber

    @staticmethod
    def dualindez(dual):
        """
        >>> dualindez("0")
        0
        >>> dualindez("1010")
        10
        >>> dualindez("1111")
        15

        :param dual:
        :return:
        """
        dezimal = 0
        laenge = len(dual)

        for i in range(laenge):
            ziffer = int(dual[i])
            exponent = laenge - i - 1
            dezimal += ziffer * (2 ** exponent)

        return dezimal

    @staticmethod
    def dual2dezimal(dual: str) -> int:
        """

        >>> dual2dezimal("0")
        0
        >>> dual2dezimal("1010")
        10
        >>> dual2dezimal("1111")
        15

        :param dual:
        :return:
        """
        dez = 0

        # 0101
        dualRev = dual[::-1]

        # 1010
        for i in range(0, len(dualRev)):
            # additionsverfahren
            dez += int(dualRev[i]) * 2 ** i

        return dez

    @staticmethod
    def decimal_to_binary(dezimal: int):
        """

        >>> decimal_to_binary(0)
        '0'

        >>> decimal_to_binary(15)
        '1111'

        >>> decimal_to_binary(10)
        '1010'

        >>> decimal_to_binary(5)
        '101'

        >>> decimal_to_binary(1)
        '1'

        :param dezimal:
        :return:
        """
        if dezimal == 0:
            return "0"

        dualNumber = ""
        while dezimal > 0:
            dualNumber += str(dezimal % 2)  # Rest
            dezimal = dezimal // 2  # floor division
        return dualNumber[::-1]

    @staticmethod
    def dezimal2dual(dezimal: int) -> str:
        # 0 abfangen
        if dezimal == 0:
            return "0"

        # Ergebnis
        dual = ""

        # verarbeitung
        while dezimal > 0:
            # Berechne den Rest der Division durch 2 (0 oder 1)
            dual += str(dezimal % 2)

            # Teile durch 2 mit komma abschneiden
            dezimal //= 2

        return dual[::-1]

    @staticmethod
    def hex_to_decimal(hex: str):

        """

        >>> hex_to_decimal("A")
        10

        >>> hex_to_decimal("9")
        9

        >>> hex_to_decimal("0")
        0

        >>> hex_to_decimal("ABC")
        2748

        :param hex:
        :return:
        """
        hex = hex[::-1]
        decimalNumber = 0
        for index, i in enumerate(hex):
            if i == "A":
                i = 10
            elif i == "B":
                i = 11
            elif i == "C":
                i = 12
            elif i == "D":
                i = 13
            elif i == "E":
                i = 14
            elif i == "F":
                i = 15
            decimalNumber += int(i) * (16 ** index)
        return decimalNumber

    @staticmethod
    def hex2dezimal(hex: str) -> int:
        dez = 0

        # 05AE
        hexRev = hex[::-1]

        hexzahlen = list(range(0, 10)) + ["A", "B", "C", "D", "E", "F"]

        # EA50
        for i in range(0, len(hexRev)):

            # wert der hexzahl herausfinden
            hexwert = 0
            for j in range(0, len(hexzahlen)):
                if str(hexzahlen[j]) == hexRev[i]:
                    hexwert = j

            # additionsverfahren
            dez += hexwert * 16 ** i

        return dez

    @staticmethod
    def decimal_to_hex(decimal: int):

        if decimal == 0:
            return "0"

        hexNumber = ""
        while decimal > 0:
            if decimal % 16 == 10:
                hexLetter = "A"
            elif decimal % 16 == 11:
                hexLetter = "B"
            elif decimal % 16 == 12:
                hexLetter = "C"
            elif decimal % 16 == 13:
                hexLetter = "D"
            elif decimal % 16 == 14:
                hexLetter = "E"
            elif decimal % 16 == 15:
                hexLetter = "F"
            else:
                hexLetter = decimal % 16

            hexNumber += str(hexLetter)
            decimal = decimal // 16
        return hexNumber[::-1]

    @staticmethod
    def dezimal2hex(dezimal: int) -> str:
        hexaList = list(range(10)) + ["A", "B", "C", "D", "E", "F"]

        # 0 abfangen
        if dezimal == 0:
            return "0"

        # Ergebnis
        hex = ""

        # verarbeitung
        while dezimal > 0:
            # Berechne den Rest der Division durch 16 (0 oder 15)
            rest = dezimal % 16

            # ermittle die passende HEX Ziffer in der Liste und hänge diese an das Ergebnis dran
            hex += str(hexaList[rest])

            # Teile durch 16 mit komma abschneiden
            dezimal //= 16

        return hex[::-1]

    @staticmethod
    def binary_to_hex(binary: str):
        return FachinformatikerRechner.decimal_to_hex(FachinformatikerRechner.binary_to_decimal(binary))

    @staticmethod
    def hex_to_binary(hex: str):
        return FachinformatikerRechner.decimal_to_binary(FachinformatikerRechner.hex_to_decimal(hex))


if __name__ == "__main__":

    print(FachinformatikerRechner.dezimal2hex(230))


