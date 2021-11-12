# Flashreads


## Build or develop

Clone the flashreads blogs repository somewhere in your workspace:

```bash
cd ~/projects/flashreads
git clone git@github.com/flashreads/blogs.git
```

Clone this repository:

```bash
cd ~/projects/flashreads
git clone git@github.com:flashreads:mediumish-theme-jekyll.git
```

Then cd into the theme repository directory:

```bash
cd mediumish-theme-jekyll
```

Install dependencies for `posts.py` script with Python3 pip:

```bash
pip install -r scripts/requirements.txt
```

Then run the script to transform and generate the blog posts into `_posts`:

```bash
python scripts/posts.py --source ~/projects/flashreads/blogs --dest _posts/ --featured featured.txt
```

That's it. Then run or build jekyll as:

```
bundle install --path vendor/bundle
bundle exec jekyll serve
```
The site should be running on http://127.0.0.1:4000.
