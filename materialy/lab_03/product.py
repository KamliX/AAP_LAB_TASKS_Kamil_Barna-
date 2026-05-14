# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # TODO: Zapisz atrybuty name, price, quantity
        # Pamietaj o walidacji: price >= 0, quantity >= 0
        if price <0 or quantity < 0:
            raise ValueError("Wartosci nie moga byc ujemne")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        """Dodaje okreslona ilosc produktow do magazynu.

        Raises:
            ValueError: jesli amount jest ujemne
        """
        # TODO: Zaimplementuj dodawanie do magazynu
        if amount <0:
          raise ValueError("Wartosci nie moga byc ujemne")
        self.quantity += amount

    def remove_stock(self, amount: int):
        """Usuwa okreslona ilosc produktow z magazynu.

        Raises:
            ValueError: jesli amount jest ujemne lub wieksze niz dostepna ilosc
        """
        # TODO: Zaimplementuj usuwanie z magazynu
        if  amount < 0:
          raise ValueError("Wartosci nie moga byc ujemne")
        elif amount > self.quantity:
            raise ValueError("Odejmowana wartosc przekracza obecny stan magazynu")

        self.quantity -= amount

    def is_available(self) -> bool:
        """Zwraca True jesli produkt jest dostepny (quantity > 0)."""
        # TODO: Zaimplementuj sprawdzanie dostepnosci
        return self.quantity > 0

    def total_value(self) -> float:
        """Zwraca calkowita wartosc produktow w magazynie (price * quantity)."""
        # TODO: Zaimplementuj obliczanie wartosci
        return self.price * self.quantity


    def apply_discount(self, percent: float):
        """Obniża cenę o podany procent (0-100)."""
        if percent < 0 or percent > 100:
            raise ValueError("Procent musi być między 0 a 100")
        self.price = self.price * (1 - percent / 100)