import mimetypes
import os

from flask import Flask, abort, redirect, render_template, send_from_directory

mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("image/svg+xml", ".svg")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Each showcase site maps a public URL slug to the folder that holds its
# static files. Decoupling the slug from the folder lets us change public
# URLs without renaming directories.
SHOWCASE_SITES = [
    {
        "slug": "ume-nail-studio",
        "dir": "ume_nail",
        "name": "Ume Nail Studio",
        "tagline": "A boutique nail-art studio website",
    },
    {
        "slug": "ume_sec",
        "dir": "ume_sec",
        "name": "Ume Studio",
        "tagline": "A second boutique studio website",
    },
    {
        "slug": "the-goblet-pub",
        "dir": "the_goblet",
        "name": "The Goblet",
        "tagline": "A traditional Irish pub website",
    },
]

SITES_BY_SLUG = {site["slug"]: site for site in SHOWCASE_SITES}

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", sites=SHOWCASE_SITES)


@app.route("/healthz")
def healthz():
    return {"status": "ok"}, 200


def _serve_site(slug, filename):
    site = SITES_BY_SLUG.get(slug)
    if site is None:
        abort(404)
    site_dir = os.path.join(BASE_DIR, site["dir"])
    return send_from_directory(site_dir, filename)


@app.route("/<slug>")
def site_redirect(slug):
    if slug not in SITES_BY_SLUG:
        abort(404)
    return redirect("/" + slug + "/", code=301)


@app.route("/<slug>/")
def site_index(slug):
    return _serve_site(slug, "index.html")


@app.route("/<slug>/<path:filename>")
def site_asset(slug, filename):
    return _serve_site(slug, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
