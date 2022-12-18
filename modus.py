from collections import Counter

# Define the paragraph as a string
paragraph = "Berkurangnya jumlah mahasiswa baru untuk perguruan tinggi swasta memaksa manajemen khususnya manajemen tingkat atas untuk berpaling untuk membuat sebuah informasi yang dapat membantu dalam membantu mengambil keputusan dalam rangka berkompetisi dengan perguruan tinggi lainnya. Salah satu jalan keluarnya adalah dengan membangun dengan pendekatan teknologi informasi seperti data warehouse untuk mengelola data dan memberikan pembuatan pengambilan keputusan yang paling terbaik. Simple Return on Investment (ROI) digunakan untuk menilai kelayakan proyek. Berdasarkan nilai ROI yang berkisar 698,36% and nilai total aliran uang kas yang mencapai Rp 8.334.901.522, dapat disimpulkan bahwa proyek pengembangan data warehouse pada perguruan tinggi swasta layak untuk diimplementasikan dengan asumsi-asumsi yang ada."

# Split the paragraph into words using the split() method
words = paragraph.split()

# Use the Counter class to count the number of times each word appears
word_counts = Counter(words)

# Print the mode of the paragraph by getting the most common word from the Counter object
print(word_counts.most_common(1)[0][0])