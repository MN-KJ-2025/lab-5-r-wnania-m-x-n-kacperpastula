# =================================  TESTY  ===================================
# Testy do tego pliku zostały podzielone na dwie kategorie:
#
#  1. `..._invalid_input`:
#     - Sprawdzające poprawną obsługę nieprawidłowych danych wejściowych.
#
#  2. `..._correct_solution`:
#     - Weryfikujące poprawność wyników dla prawidłowych danych wejściowych.
# =============================================================================
import numpy as np
from typing import Tuple
from typing import Union

def spare_matrix_Abt(m: int, n: int) -> Union[Tuple[np.ndarray, np.ndarray] , None]:
    
    if not (isinstance(m, int) and isinstance(n, int)):
        return None
    if m <=0 or n <=0:
        return None
    
    t = np.linspace(0,1,m, endpoint = True)
    A = np.vander(t,n,increasing = True)
    b = np.cos(4 * t)
    return A,b
    """Funkcja tworząca zestaw składający się z macierzy A (m,n) i
    wektora b (m,) na podstawie pomocniczego wektora t (m,).

    Args:
        m (int): Liczba wierszy macierzy A.
        n (int): Liczba kolumn macierzy A.

    Returns:
        (tuple[np.ndarray, np.ndarray]):
            - Macierz A o rozmiarze (m,n),
            - Wektor b (m,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    pass


def square_from_rectan(
    A: np.ndarray, b: np.ndarray
) -> Union[Tuple[np.ndarray, np.ndarray] , None]:
    if not (isinstance(A, np.ndarray) and isinstance(b, np.ndarray)):
        return None
    if A.shape[0] != b.shape[0]:
        return None
    ATA = A.T @ A
    ATb = A.T @ b
    return ATA, ATb 
    """Funkcja przekształcająca układ równań z prostokątną macierzą współczynników
    na kwadratowy układ równań.
    A^T * A * x = A^T * b  ->  A_new * x = b_new

    Args:
        A (np.ndarray): Macierz A (m,n) zawierająca współczynniki równania.
        b (np.ndarray): Wektor b (m,) zawierający współczynniki po prawej stronie równania.

    Returns:
        (tuple[np.ndarray, np.ndarray]):
            - Macierz A_new o rozmiarze (n,n),
            - Wektor b_new (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    pass


def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray) -> Union[float, None]:

    if not (isinstance(A, np.ndarray) and isinstance(x, np.ndarray) and isinstance(b, np.ndarray)):
        return None
    if (A.shape)[1] != x.shape[0]:
        return None
    
    return np.linalg.norm(b - (A @ x))

    """Funkcja obliczająca normę residuum dla równania postaci:
    Ax = b

    Args:
        A (np.ndarray): Macierz A (m,n) zawierająca współczynniki równania.
        x (np.ndarray): Wektor x (n,) zawierający rozwiązania równania.
        b (np.ndarray): Wektor b (m,) zawierający współczynniki po prawej stronie równania.

    Returns:
        (float): Wartość normy residuum dla podanych parametrów.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    pass
def svd_solve(A, b):
    U, S, VT = np.linalg.svd(A, full_matrices=False)
    S = np.diag(S)
    V = VT.T
    return V @ np.linalg.solve(S, U.T @ b)