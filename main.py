"""
Program untuk menganalisis data dari suatu sumber,
diproses dan ditampilkan hasilnya
"""

from acquire import twitter #, facebook, csv, xlsx, docx
from process import decision_tree #, random,_forest
from views import text #, image, chart

data = twitter.get_data() #acquire
result = decision_tree.process_data(data) #process
display = text.as_text(result) #views

print(display)
