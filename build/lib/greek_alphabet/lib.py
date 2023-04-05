"""
Module for providing: Greek alphabet
"""

"""
Upper Case Letter	Lower Case Letter	Greek Letter Name	English Equivalent
Α	α	Alpha	a	
Β	β	Beta	b	
Γ	γ	Gamma	g	
Δ	δ	Delta	d	
Ε	ε	Epsilon	e	
Ζ	ζ	Zeta	z	
Η	η	Eta	h	
Θ	θ	Theta	th	
Ι	ι	Iota	i	
Κ	κ	Kappa	k	
Λ	λ	Lambda	l	
Μ	μ	Mu	m	
Ν	ν	Nu	n	
Ξ	ξ	Xi	x	
Ο	ο	Omicron	o	
Π	π	Pi	p	
Ρ	ρ	Rho	r	
Σ	σ,ς *	Sigma	s	
Τ	τ	Tau	t	
Υ	υ	Upsilon	u	
Φ	φ	Phi	ph	
Χ	χ	Chi	ch	
Ψ	ψ	Psi	ps	
Ω	ω	Omega	o	
"""


from typing import Callable


class AlphabetChar:
    """
    Represents a single character in the Greek alphabet
    Contains:
        lower: Lower case letter
        upper: Upper case letter
        name: Greek letter name
        english: English equivalent
    """

    def __init__(self, lower: str, upper: str, name: str, english: str):
        self.lower = lower
        self.upper = upper
        self.name = name
        self.english = english

    def __repr__(self):
        return f"AlphabetChar(lower={self.lower}, upper={self.upper}, name={self.name}, english={self.english})"

    def __str__(self):
        return self.lower


class Alphabet:
    "Contains the Greek alphabet"
    Alpha = AlphabetChar("α", "Α", "Alpha", "a")
    Beta = AlphabetChar("β", "Β", "Beta", "b")
    Gamma = AlphabetChar("γ", "Γ", "Gamma", "g")
    Delta = AlphabetChar("δ", "Δ", "Delta", "d")
    Epsilon = AlphabetChar("ε", "Ε", "Epsilon", "e")
    Zeta = AlphabetChar("ζ", "Ζ", "Zeta", "z")
    Eta = AlphabetChar("η", "Η", "Eta", "h")
    Theta = AlphabetChar("θ", "Θ", "Theta", "th")
    Iota = AlphabetChar("ι", "Ι", "Iota", "i")
    Kappa = AlphabetChar("κ", "Κ", "Kappa", "k")
    Lambda = AlphabetChar("λ", "Λ", "Lambda", "l")
    Mu = AlphabetChar("μ", "Μ", "Mu", "m")
    Nu = AlphabetChar("ν", "Ν", "Nu", "n")
    Xi = AlphabetChar("ξ", "Ξ", "Xi", "x")
    Omicron = AlphabetChar("ο", "Ο", "Omicron", "o")
    Pi = AlphabetChar("π", "Π", "Pi", "p")
    Rho = AlphabetChar("ρ", "Ρ", "Rho", "r")
    Sigma = AlphabetChar("σ", "Σ", "Sigma", "s")
    Tau = AlphabetChar("τ", "Τ", "Tau", "t")
    Upsilon = AlphabetChar("υ", "Υ", "Upsilon", "u")
    Phi = AlphabetChar("φ", "Φ", "Phi", "ph")
    Chi = AlphabetChar("χ", "Χ", "Chi", "ch")
    Psi = AlphabetChar("ψ", "Ψ", "Psi", "ps")
    Omega = AlphabetChar("ω", "Ω", "Omega", "o")

    # Methods

    @classmethod
    def get_list(cls) -> list[AlphabetChar]:
        "Returns a list of all Greek alphabet characters"
        return [
            cls.Alpha,
            cls.Beta,
            cls.Gamma,
            cls.Delta,
            cls.Epsilon,
            cls.Zeta,
            cls.Eta,
            cls.Theta,
            cls.Iota,
            cls.Kappa,
            cls.Lambda,
            cls.Mu,
            cls.Nu,
            cls.Xi,
            cls.Omicron,
            cls.Pi,
            cls.Rho,
            cls.Sigma,
            cls.Tau,
            cls.Upsilon,
            cls.Phi,
            cls.Chi,
            cls.Psi,
            cls.Omega,
        ]

    @classmethod
    def get_dict(
        cls, 
        key: Callable[[AlphabetChar], str] = lambda char: char.name,
        value: Callable[[AlphabetChar], str | AlphabetChar] = lambda char: char,
    ) -> dict[str, AlphabetChar]:
        """Returns a dictionary of all Greek alphabet characters
        key: The key to use for the dictionary (default: greek name of character)
        """
        return {key(char): value(char) for char in cls.get_list()}

    # Utility methods

    @classmethod
    def upper(cls, lower_char: str) -> str:
        "Returns the upper case letter of a lower case letter"
        return cls.get_dict(key=lambda char: char.lower)[lower_char].upper

    @classmethod
    def lower(cls, upper_char: str) -> str:
        "Returns the lower case letter of an upper case letter"
        return cls.get_dict(key=lambda char: char.upper)[upper_char].lower


