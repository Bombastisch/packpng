from pathlib import Path
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('./data/seeds.json', encoding="utf8") as seeds_json:
        with open('./data/what_we_know.json', encoding="utf8") as wwk_json:
            seeds = json.load(seeds_json)
            what_we_know = json.load(wwk_json)
            return render_template('index.html', seeds=seeds, what_we_know=what_we_know)


@app.route('/faq/')
def faq():
    with open('./data/faq.json', encoding="utf8") as faq_json:
            faq = json.load(faq_json)
            return render_template('faq.html', faq=faq)

@app.route('/contributors/')
def contributors():
    with open('./data/contributors.json', encoding="utf8") as contrib_json:
            contributors = json.load(contrib_json)
            return render_template('contributors.html', contributors=contributors)

@app.route('/google_doc/')
def google_doc():
    return render_template('google_doc.html')

@app.route('/timeline/')
def timeline():
    return render_template('timeline.html')

@app.route('/gallery/')
def gallery():
    staticdir = Path('./static/')
    images = list((staticdir / "gallery").glob('**/*'))
    thumbs = [staticdir / "thumbnails" / str("thumbnail_"+p.name) for p in images]
    images = map(lambda x: x.relative_to(staticdir).as_posix(), images)
    thumbs = map(lambda x: x.relative_to(staticdir).as_posix(), thumbs)
    imthumbs = list(zip(images, thumbs))
    return render_template('gallery.html', images=imthumbs)


if __name__ == '__main__':
    extra_files = [str(p.resolve()) for p in Path('./').glob('**/*')] # list of all files in the project, so flask knows where to look for changes
    app.run(extra_files=extra_files, debug=True)