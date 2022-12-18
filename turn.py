import openpyxl

# Define the paragraph as a string
paragraph = "Studi kelayakan terhadap rencana investasi proyek teknologi informasi (TI) berbeda dengan studi kelayakan investasi barang modal (capital goods) lainnya. Pada investasi barang modal lebih mudah ditentukan manfaat (benefit) dari investasi tersebut. Sedangkan pada investasi TI sering sulit ditentukan manfaat yang dihasilkan. Karena manfaat TI lebih sering bersifat non-finansial sehingga metode penilaian dikembangkan para ahli dengan mempertimbangkan manfaat finansil maupun non-finansial, berwujud (tangible benefit) maupun tak berwujud (intangibel benefit). Salah satu metode yang populer adalah metode information economics (IE). Pada metode ini terdapat banyak variabel yang harus ditentukan nilainya dan menggunakan scoring. Bila hal ini dilakukan secara manul akan terdapat kesulitan dalam hal perhitungan maupun dalam simulasi nilai, skor dan bobot masing-masing varibel. Penggunaan sebuah sistem yaitu sistem pendukung keputusan (SPK) atau decision support system (DSS) merupakan solusi terbaik yang dapat menganalisis alternatif-alternatif untuk mendapatkan alternatif terbaik. Penelitian ini menghasilkan sebuah SPK InTI (investasi TI) yang dapat digunakan untuk 1). melakukan simulasi pada satu alternatif untuk menilai alternatif tersebut berdasarkan kebutuhan anggaran dan kemungkinan manfaat yang diperoleh; 2). membandingkan antar alternatif rencana investasi TI untuk menentukan prioritas investasi TI dari beberapa rencana."

# Split the paragraph into words using the split() method
words = paragraph.split()

# Create a new Excel workbook
wb = openpyxl.Workbook()

# Get the active worksheet
ws = wb.active

# Write the words to the first column of the worksheet
for i, word in enumerate(words):
    ws.cell(row=i+1, column=1).value = word

# Use the range() function to generate a sequence of numbers from 1 to 10

# Save the workbook
wb.save("words.xlsx")