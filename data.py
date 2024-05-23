import requests
from bs4 import BeautifulSoup

url = "https://blog.prepscholar.com/list-of-ap-exams"
r = requests.get(url)

exams = []

soup = BeautifulSoup(r.content, 'html.parser')
results_all = soup.find_all("li")
results_exam_name = results_all[:33]



for exam in results_exam_name:
    exam = str(exam)
    clean_name = exam.lstrip("<li>").rstrip("</li>")
    exams.append(clean_name)

 