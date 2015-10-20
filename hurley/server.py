#!/usr/bin/env python

from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import SelectField

from hurley.podcasts import pairings, podcasters, graph, find_links


app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'no really tis must dosidhksjdfgnvkyjrhmstbgnemr,test secret key'


MYCACHE = {}


class PodcastForm(Form):
    choices = [("", "")] + [(p, p) for p in sorted(podcasters)]
    src = SelectField('src', choices=choices)
    dst = SelectField('dst', choices=choices)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = PodcastForm()
    result = None
    print MYCACHE
    if form.validate_on_submit() and form.src.data and form.dst.data:
        pairings = MYCACHE.setdefault((form.src.data, form.dst.data), graph.dijkstra(form.src.data, form.dst.data))
        if form.src.data == form.dst.data:
            result = ['identical']
        elif len(pairings) == 1:
            result = ["disconnected"]
        else:
            result = find_links(pairings)

    return render_template('index.html',
                           form=form,
                           src=form.src.data,
                           dst=form.dst.data,
                           result=result)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', title="Privacy")
