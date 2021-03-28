from flask import Flask, render_template
app = Flask(__name__)

boxers = [
    {
        'ranking': 'Place #1',
        'name': 'Muhammad Ali',
        'birth': 'January 17th 1942',
        'died': 'June 3rd 2016',
        'wins': 56,
        'losses': 5,
        'picture': 'https://networthcelebrities.com/wp-content/uploads/2015/11/Muhammad-Ali_1.jpg'
    },
    {
        'ranking': 'Place #2',
        'name': 'Sugar Ray Robinson',
        'birth': 'May 3, 1921',
        'died': 'April 12, 1989',
        'wins': 173,
        'losses': 19,
        'picture': 'https://vignette.wikia.nocookie.net/boxing/images/f/f6/Sugar_Ray_Robinson.jpeg/revision/latest?cb=20160504191513'
    },
    {
        'ranking': 'Place #3',
        'name': 'Myke Tyson',
        'birth': 'June 30, 1966',
        'died': '-',
        'wins': 50,
        'losses': 6,
        'picture': 'https://xdigitalnews.com/wp-content/uploads/2020/05/Tyson-2-GettyImages-139051548.jpg'
    }
]

        
def filter_by_name(dics, boxer_name):
    for dic in dics:
        for value in dic.values():
            if value == boxer_name:
                return dic

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', boxers=boxers)

@app.route("/<boxer_name>")
def boxer(boxer_name):
    boxer_dic = filter_by_name(boxers, boxer_name)
    return render_template('boxer.html', boxer=boxer_dic)

if __name__ == '__main__':
    app.run(debug=True)
