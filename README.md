# Mediumish - Jekyll Theme

[Live Demo](https://wowthemesnet.github.io/mediumish-theme-jekyll/) &nbsp; | &nbsp; [Download](https://github.com/wowthemesnet/mediumish-theme-jekyll/archive/master.zip) &nbsp; | &nbsp; [Documentation](https://bootstrapstarter.com/template-mediumish-bootstrap-jekyll/) &nbsp; | &nbsp; [Buy me a coffee](https://www.wowthemes.net/donate/)

![mediumish](assets/images/mediumish-jekyll-template.png)


### Copyright

Copyright (C) 2019 Sal, https://www.wowthemes.net

**Mediumish for Jekyll** is designed and developed by [Sal](https://www.wowthemes.net) and it is *free* under MIT license. 

<a href="https://www.wowthemes.net/donate/" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

### Contribute

1. [Fork the repo](https://github.com/wowthemesnet/mediumish-theme-jekyll).
2. Clone a copy of your fork on your local
3. Create a branch off of master and give it a meaningful name (e.g. my-new-mediumish-feature).
4. Make necessary changes, commit, push and open a pull request on GitHub.

Thank you!


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
git clone git@github.com:flashreads/mediumish-theme-jekyll.git
```

Then cd into the theme repository directory:

```bash
cd mediumish-theme-jekyll
```

Install dependencies for `posts.py` script with Python3 pip:

```bash
pip install scripts/requirements.txt
```

Then run the script to transform and generate the blog posts into `_posts`:

```bash
python scripts/posts.py --source ~/projects/flashreads/blogs --dest _posts/ --featured featured.txt
```

That's it. Then run or build jekyll.