from flask import Flask, render_template
import requests
import tempfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)


def filter(data, var):
    # get survival rates by given variable
    count = {}  # number of people by given variable
    survivors = {}  # survivors by given variable

    for passenger in data:
        if passenger[var] == '':
            continue
        if float(passenger[var]) in count:
            count[float(passenger[var])] += 1
        else:
            count[float(passenger[var])] = 1
        if float(passenger[var]) in survivors:
            survivors[float(passenger[var])] += float(passenger["survived"])
        else:
            survivors[float(passenger[var])] = float(passenger["survived"])
    rates = {}
    for var in count:
        rates[var] = survivors[var]/count[var]
    return rates

def bySex(data):
    # get survival rates by sex
    count = {}  # number of people by sex
    survivors = {}  # survivors by sex

    for passenger in data:
        if passenger["sex"] == '':
            continue
        if passenger["sex"] in count:
            count[passenger["sex"]] += 1
        else:
            count[passenger["sex"]] = 1
        if passenger["sex"] in survivors:
            survivors[passenger["sex"]] += int(passenger["survived"])
        else:
            survivors[passenger["sex"]] = int(passenger["survived"])
    rates = {}
    for cl in count:
        rates[cl] = survivors[cl]/count[cl]

    return rates


@app.route('/')
def index():
    data = requests.get('https://titanic.businessoptics.biz/survival').json()
    rates_age = filter(data, "age")
    plt.bar(rates_age.keys(), rates_age.values(), 0.5, color='g')
    tmp = tempfile.NamedTemporaryFile(dir='static/temp', suffix='.png',
                                      delete=False)
    plt.xlabel("Age")
    plt.ylabel("Survival rate")
    plt.savefig(tmp)
    plt.close()
    tmp.close()
    age_graph = tmp.name.split('/')[-1]
    rates_age = [(k, rates_age[k]) for k in sorted(rates_age.keys())]

    rates_class = filter(data, "class")
    plt.bar(list(rates_class.keys()), rates_class.values(), color='g', align='center')
    tmp_class = tempfile.NamedTemporaryFile(dir='static/temp', suffix='.png',
                                            delete=False)
    plt.xticks(list(rates_class.keys()), ["First", "Second", "Third"])
    plt.xlabel("Class")
    plt.ylabel("Survival rate")
    plt.savefig(tmp_class)
    plt.close()
    tmp_class.close()
    class_graph = tmp_class.name.split('/')[-1]
    rates_class = [(k, rates_class[k]) for k in sorted(rates_class.keys())]

    rates_sex = bySex(data)
    int_keys = [0 if k == 'male' else 1 for k in rates_sex.keys()]
    plt.bar(int_keys, rates_sex.values(), color='g', align='center')
    tmp_sex = tempfile.NamedTemporaryFile(dir='static/temp', suffix='.png',
                                          delete=False)
    plt.xticks(int_keys, rates_sex.keys())
    plt.xlabel("Sex")
    plt.ylabel("Survival rate")
    plt.savefig(tmp_sex)
    plt.close()
    tmp_sex.close()
    sex_graph = tmp_sex.name.split('/')[-1]
    rates_sex = [(k, rates_sex[k]) for k in sorted(rates_sex.keys())]

    return render_template("index.html", var="Age", rates_age=rates_age,
                           age_graph=age_graph, rates_class=rates_class,
                           class_graph=class_graph, rates_sex=rates_sex,
                           sex_graph=sex_graph)


@app.route('/age')
def graph_age():
    age_graph = session.get('age_graph')
    return render_template('graph.html', graphPNG=age_graph)


@app.route('/sex')
def graph_sex():
    sex_graph = session.get('sex_graph')
    return render_template('graph.html', graphPNG=sex_graph)


@app.route('/class')
def graph_class():
    class_graph = session.get('class_graph')
    return render_template('graph.html', graphPNG=class_graph)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
