from vsearch import search4letters
from flask import Flask,request,render_template, escape #,redirect
#import mysql.connector
from ConnDb import UseDb


app=Flask(__name__)

app.config['dbconfig'] = {
    'host': '127.0.0.1',
    'user': 'vsearch',
    'password': '123',
    'database': 'vsearchlogDB',
}


# @app.route('/')
# def home() ->'302':
#     return redirect('/entry')

# generator id
def log_request_generator_id(val=0):
    while True:
        yield val
        val+=1
id = log_request_generator_id()

# Add logs requests and response into log file (myself func)

# def log_request(req: 'flask_request', resp: 'str'):
#     with open('log_request.txt', 'a') as file_log:
#         print('id:{}, Request pharase: {}, letters {}, find result {}'.format(next(id),req['phrase'],req['letters'], resp), file = file_log)


# Add logs requests and response into log file (func from the book)
# OLD VERSION
# def log_request(req: 'flask_request', resp: 'str'):
#     with open('vsearch.log', 'a') as log:
#         print(req.form, req.remote_addr, req.user_agent, resp, file=log, sep='|')

# ADD LOGS INTO DB
# OLD_VERSION
# def log_request(req: 'flask_request', resp: 'str'):
#
#     conn = mysql.connector.connect(**dbconfig)
#     cursor = conn.cursor()
#     _SQL = """ insert into log (phrase, letters, ip, browser_string, results)
#     values (%s, %s, %s, %s, %s)
#     """
#     cursor.execute(_SQL,(req.form['phrase'], req.form['letters'],
#                          req.remote_addr, req.user_agent.browser, resp,))
#     conn.commit()
#     cursor.close()
#     conn.close()

# ADD LOGS INTO DB
# NEW VERSION
def log_request(req: 'flask_request', resp: 'str',):
    with UseDb(app.config['dbconfig']) as cursor:
        _SQL = """ insert into log (phrase, letters, ip, browser_string, results)
        values (%s, %s, %s, %s, %s)
        """
        cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],
                             req.remote_addr, req.user_agent.browser, resp,))



# presents the find result page on the web
@app.route('/search4',methods=['POST'])
def do_search():
    input_phrase = request.form['phrase']
    input_letters = request.form['letters']
    the_title = 'You search result here!'
    search_result = str(search4letters(input_phrase, input_letters))
    #log_request(request.form, search_result)
    log_request(request, search_result)
    return render_template('results.html', the_title = the_title, the_phrase = input_phrase, the_letters = input_letters, the_results = search_result)

# presents the log file on the web
@app.route('/viewlog')
# new version 1.2. (get data from db)
def view_log() -> 'HTML':

    with UseDb(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters,ip, browser_string,results from log order by ts desc"""
        cursor.execute(_SQL)
        contents=cursor.fetchall()

    titles=['Phrase','Letters', 'Remote_addr', 'User_agent', 'Results']
    return render_template('viewlog.html',the_title='The log page', the_row_titles=titles, the_data=contents)

#old version 1.1(return list in list log)
# def view_log() -> 'HTML':
#     log_data=[]
#     with open('vsearch.log') as log:
#         for lines in log:
#             log_data.append([])
#             for item in lines.split('|'):
#                 log_data[-1].append(escape(item))
#         titles=['FromData', 'Remote_addr', 'User_agent', 'Results']
#         return render_template('viewlog.html',the_title='The log page', the_row_titles=titles, the_data=log_data)
#old version 1.0:
# def view_log():
#     #with open('log_request.txt') as log:
#     with open('vsearch.log') as log:
#         log_data=log.readlines()
#     return escape(''.join(log_data))



# presents find page on th web
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title = 'Welcome to search letter on the WEB')








if __name__=='__main__':
    app.run(debug=True)


