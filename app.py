from flask import Flask, request, render_template, render_template_string
from views import views

app = Flask(__name__)
app.register_blueprint(views,url_prefix="/")

@app.errorhandler(404)
def page_not_found(e):

    template = '''{%% extends "index.html" %%}
    {%% block content %%}
    <div class="center-content error">
    <h1>Oops! That page doesn't exist.</h1>
    <h3>%s</h3>
    </div>
    {%% endblock %%}
    ''' % (request.path)
    return render_template_string(template), 404
# def search(e):
#     url = request.url
#     return render_template("search.html",url=url), 404

if __name__ == '__main__':
    app.run(debug=True)
