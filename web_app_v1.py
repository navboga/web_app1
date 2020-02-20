from vsearch import search4letters
from flask import Flask,request,render_template, escape #,redirect



app=Flask(__name__)

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
def log_request(req: 'flask_request', resp: 'str'):
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, resp, file=log, sep='|')



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
def view_log():
    #with open('log_request.txt') as log:
    with open('vsearch.log') as log:
        log_data=log.read()
    return escape(log_data)



# presents find page on th web
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title = 'Welcome to search letter on the WEB')








if __name__=='__main__':
    app.run(debug=True)


