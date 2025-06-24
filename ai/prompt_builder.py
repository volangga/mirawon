def build_prompt(topik, jumlah, tingkat):
    if not topik or not isinstance(topik, str):
        raise ValueError('Topik harus berupa string dan tidak boleh kosong.')
    if not isinstance(jumlah, int) or jumlah < 1:
        raise ValueError('Jumlah soal harus bilangan bulat positif.')
    if not tingkat or not isinstance(tingkat, str):
        raise ValueError('Tingkat harus berupa string dan tidak boleh kosong.')
    return f"Buatkan {jumlah} soal pilihan ganda tingkat {tingkat} tentang {topik} beserta jawabannya."
