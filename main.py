#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Übungsblatt 07"""


import re


CORPUS_TEXT = (
    "Stocks jumped on Friday, building on strong weekly gains, as "
    "weak economic data strongly increased the odds of easier monetary policy "
    "from the Federal Reserve. The Dow Jones Industrial Average traded 350 points "
    "higher, led by gains in Microsoft and Apple. The stock index broke above "
    "26,000 for the first time in nearly a month. The S&P climbed 1.4% as the "
    "tech sector outperformed. The Nasdaq Composite gained 1.95%. The U.S. "
    "economy added 75,000 jobs in May, marking the second straight month of "
    "monthly jobs growth lying below 100,000. Economists polled by Dow Jones "
    "expected an increase of 180,000 jobs. Wage growth also considerably slowed. "
    "'The market’s got a conundrum here. That’s a bad report. Just on the report "
    "itself, I think people would want to sell the market. However, the fact that "
    "it really makes the case for a rate cut, I think is why you’re seeing the "
    "market hang in there,' said JJ Kinahan, chief market strategist at TD "
    "Ameritrade. Market expectations for a Fed rate cut in June rose to 27.5% "
    "from 16.7% after the data release, according to the CME Group’s FedWatch "
    "tool. The market is also pricing in a 79% chance of lower Fed rates by August."
)

EXAMPLE_LINES = """
abc
xyz
123
x456x
789x
"""


# Aufgabe 1:

def complicated_search(pattern, text, mode):
    """

    :param pattern:
    :param text:
    :param mode: die Funktion, die benutzt wird
    :return:
    """
    functions = {
        1: re.match,
        2: re.findall,
        3: re.search,
    }
    result = functions[mode](pattern, text)
    if isinstance(result, getattr(re, "Match")):
        result = result.group()
    return result


# Aufgabe 2:

def check_vowels(text):
    """
    Überprüft, ob ein als Parameter gegebener String Vokale enthält
    wir gehen dabei davon aus, dass der String nur aus Kleinbuchstaben besteht.


    :param text:
    :return: True zurückgeben, wenn der gegebene
            String mindestens einen der folgenden
            fünf Charaktere enthält: a, o, e, i oder u

            Enthält der gegebene String keinen der genannten Charaktere, soll check_vowels
            den Wert False zurückgeben.
    """
    if re.search(r"[aoeiu]", text) is None:
        return False
    return True


# Aufgabe 3:

def count_adverbs(text):
    """
    die Funktion zählt in einem gegebenen String Wörter,
    die mit dem Suffix -ly enden

    :param text:
    :return: die Anzahl dieser Wörter
            als Integer zurückgegeben.
    :rtype: int
    """
    result = re.findall(r"[a-zA-Z]+ly\s", text)
    return len(result)


# Aufgabe 4:

def remove_numbers(text):
    """
    ersetzt in einem gegebenen Text jegliche Vorkommen von Zahlen und Prozenten
    durch den Platzhalter "[DD]"

    :param text:
    :return: eine Version des Textes,
            in der alle Zahlen und Prozentangaben
            durch den Platzhalter ersetzt wurden
    """
    return re.sub(r"\d{1,3}(,?\d{3})*(\.\d+)?%?", "[DD]", text)


# Aufgabe 5:

def begin_x(text):
    """
    gibt alle Zeilen zurück, die mit einem “x” beginnen

    :param text:
    :return:
    """

    return re.findall(r"^x.*", text, flags=re.MULTILINE)

def begin_end_x(text):
    """
    gibt alle Zeilen zurück, die mit einem “x” beginnen und/oder mit einem “x” enden.

    :param text:
    :return:
    """

    return re.findall(r"^x.*|.*x$", text, flags=re.MULTILINE)

# Aufgabe 6:

def logging_examples():
    """
    das logging Modul von Python näher kennenlernen.

    :return:
    """
    import logging

    logging.basicConfig(
        format="%(asctime)s :: %(levelname)-8s :: %(name)s :: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="beispiel.log",
        filemode="a",
        level=logging.DEBUG
    )
    logger = logging.getLogger(name="Beispiel")

    logger.info("Es geht los")
    logger.debug("Vielleicht ein Problem")
    logger.error("Leider ein Fehler")


# Testaufrufe

if __name__ == "__main__":

    print(check_vowels("hello"))
    print(check_vowels("xyz"))

    print(count_adverbs("He was carefully disguised but captured quickly by police"))

    print(remove_numbers(CORPUS_TEXT))

    print(begin_x(EXAMPLE_LINES))
    print(begin_end_x(EXAMPLE_LINES))

    logging_examples()
