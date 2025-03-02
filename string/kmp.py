def compute_lps_array(pattern):
    """
    Preprocesa el patrón para construir la tabla LPS (Longest Prefix Suffix).
    """
    m = len(pattern)
    lps = [0] * m
    length = 0

    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps_array(pattern)
    result = []

    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                # Coincidencia encontrada
                result.append(i - j)
                j = lps[j - 1]  # Reinicia j usando la tabla LPS
        else:
            if j != 0:
                j = lps[j - 1]  # Retrocede j usando la tabla LPS
            else:
                i += 1  # No hay coincidencia, avanza en el texto
    return result


text = "ABABDABACDEABABCABAB"
pattern = "ABABCABAB"
print("Coincidencias encontradas en los índices:", kmp_search(text, pattern))
