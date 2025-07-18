codon_table = {
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine",       "UUG": "Leucine",
    "CUU": "Leucine",       "CUC": "Leucine",
    "CUA": "Leucine",       "CUG": "Leucine",

    "AUU": "Isoleucine",    "AUC": "Isoleucine",
    "AUA": "Isoleucine",    "AUG": "Methionine",  # START

    "GUU": "Valine",        "GUC": "Valine",
    "GUA": "Valine",        "GUG": "Valine",

    "UCU": "Serine",        "UCC": "Serine",
    "UCA": "Serine",        "UCG": "Serine",
    "AGU": "Serine",        "AGC": "Serine",

    "CCU": "Proline",       "CCC": "Proline",
    "CCA": "Proline",       "CCG": "Proline",

    "ACU": "Threonine",     "ACC": "Threonine",
    "ACA": "Threonine",     "ACG": "Threonine",

    "GCU": "Alanine",       "GCC": "Alanine",
    "GCA": "Alanine",       "GCG": "Alanine",

    "UAU": "Tyrosine",      "UAC": "Tyrosine",
    "UAA": "Stop",          "UAG": "Stop",         # STOP
    "UGA": "Stop",                                 # STOP

    "CAU": "Histidine",     "CAC": "Histidine",
    "CAA": "Glutamine",     "CAG": "Glutamine",

    "AAU": "Asparagine",    "AAC": "Asparagine",
    "AAA": "Lysine",        "AAG": "Lysine",

    "GAU": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",

    "UGU": "Cysteine",      "UGC": "Cysteine",
    "UGG": "Tryptophan",

    "CGU": "Arginine",      "CGC": "Arginine",
    "CGA": "Arginine",      "CGG": "Arginine",
    "AGA": "Arginine",      "AGG": "Arginine",

    "GGU": "Glycine",       "GGC": "Glycine",
    "GGA": "Glycine",       "GGG": "Glycine"
}
class DNA:
    def transcribe(dna):
        """
        Converts DNA to mRNA by replacing all 'T' with 'U'.
        Example: ATG -> AUG
        """
        try:
            rna = dna.upper().replace("T", "U")
            return {
            "dna": dna,
            "mrna": rna,
            "error": None
            }
        except Exception as e:
            return {
            "dna": None,
            "rna": None,
            "error": str(e)
            }
    def translate(mrna):
        """
        Returns mRNA to amino acid chain using codon tables.
        Example:
            AUGUUU = [Methionine, Phenylalanine]
        """
        try:
            rna = mrna.upper().replace(" ", "")
            codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
            amino_acids = []
            for codon in codons:
                aa = codon_table.get(codon, f"Unknown codon: {codon}")
                if aa == "Stop":
                    break
                amino_acids.append(aa)
            return {
            "mrna": mrna,
            "codons": codons,
            "amino_acids": amino_acids,
            "error": None
            }
        except Exception as e:
            return {
            "mrna": None,
            "codons": None,
            "amino_acids": None,
            "error": str(e)
            }                     