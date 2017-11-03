from pathlib import Path
import csv
import random

from flask import Flask, render_template


app = Flask(__name__)
csvfile = str(Path(__file__).parents[2])
with open(csvfile + '/data/knowledge_pp.csv', encoding='utf8') as f:
    knowledges = list(csv.reader(f))


@app.route('/', methods=['GET', 'POST'])
def index():
    # TODO: 지금 여기서는 POST쓰는게 다시하기밖에 없어서 이렇게 해도 되는데 나중에는 어떻게 될지 모름. 이거 고려해서 좀 더 안정적인 방식으로
    k = random.choice(knowledges)
    return render_template('index.html', data={'keyword': k[0], 'content': k[1]})