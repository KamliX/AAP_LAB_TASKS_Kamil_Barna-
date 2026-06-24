
import re

POS_WORDS = {"good","great","excellent","wonderful","love","best","amazing","brilliant","perfect"}
NEG_WORDS = {"bad","worst","awful","terrible","hate","boring","waste","poor","horrible"}

def sentiment_score(text: str) -> int:
    """CPU-bound: tokenizuj, policz pozytywne minus negatywne."""
    # TODO Zadanie 2.1: zaimplementuj
    # 1. lowercase, regex \w+ -> lista slow
    # 2. zliczyc ile slow w POS_WORDS, ile w NEG_WORDS
    # 3. zwrocic roznice
    words = re.findall(r"\w+", text.lower())
    pos = sum(1 for w in words if w in POS_WORDS)
    neg = sum(1 for w in words if w in NEG_WORDS)
    return pos - neg
