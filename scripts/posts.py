from argparse import ArgumentParser
from datetime import datetime
from os import path, listdir, getcwd, chdir
import subprocess

from dateutil.parser import parse as dt_parse
from ruamel.yaml import YAML


def transform_posts(src_dir, dest_dir, featured_path=None):
    featured = load_featured(featured_path) if featured_path else []
    for p in (src_dir, dest_dir):
        if not path.isdir(p):
            raise Exception('{} is not a directory.'.format(p))
    for dir_name in listdir(src_dir):
        if path.isdir(path.join(src_dir, dir_name)):
            transform_category(dir_name, path.join(src_dir, dir_name), dest_dir, featured)


def transform_category(category, src_dir, dest_dir, featured):
    for file_name in listdir(src_dir):
        if not path.isfile(path.join(src_dir, file_name)):
            continue
        _, file_ext = path.splitext(file_name)
        if file_ext.lower() not in ['.md', '.mdx']:
            continue
        if file_name.lower() in ['readme.md']:
            continue
        try:
            transform_post(category, path.join(src_dir, file_name), dest_dir, featured)
        except Exception as e:
            print('Failed to transform post: ', file_name, 'Error: {}'.format(e))


def transform_post(category, post_file, dest_dir, featured):
    frontmatter, fm_length = read_frontmatter(post_file)
    post_date = frontmatter.get('date')
    if not post_date:
        dt = path.getmtime(post_file)
        post_date = datetime.fromtimestamp(dt)
    else:
        if isinstance(post_date, str):
            post_date = dt_parse(post_date)
    frontmatter['date'] = post_date.isoformat()

    if not frontmatter.get('layout'):
        frontmatter['layout'] = 'post'
    
    categories = frontmatter.get('categories')
    if isinstance(categories, str):
        categories = [categories]
    if category not in categories:
        categories.append(category)
    
    frontmatter['categories'] = categories

    tags = frontmatter.get('tags')
    if isinstance(tags, str):
        tags = [tags]
    frontmatter['tags'] = tags

    try:
        frontmatter['author_email'] = get_email_from_git(post_file)
    except Exception as e:
        print('Failed to get author email: ', e)

    file_name = path.basename(post_file)

    file_name = '{}-{}'.format(
        post_date.strftime('%Y-%m-%d'),
        file_name,
    )

    post_id = frontmatter.get('id')
    if post_id and post_id in featured:
        frontmatter['featured'] = True

    with open(post_file) as pf:
        pf_content = pf.readlines()
        pf_content = pf_content[fm_length:]

        yaml = YAML(typ='safe')

        with open(path.join(dest_dir, file_name), 'w') as tf:
            tf.write('---\n')
            yaml.dump(frontmatter, tf)
            tf.write('---\n')
            tf.write('\n')
            tf.write('\n'.join(pf_content))

def read_frontmatter(post_file):
    frontmatter = []

    reading_fm = False
    read_fm = False

    count = 0
    with open(post_file) as pf:
        for line in pf:
            count += 1
            if line.strip() == '---':
                if reading_fm:
                    read_fm = True
                    reading_fm = False
                    break
                reading_fm = True
                continue
            elif reading_fm:
                frontmatter.append(line)

    if not read_fm:
        if reading_fm:
            raise Exception('Invalid front-matter in post: {}'.format(post_file))
        raise Exception('No front-matter in post: {}'.format(post_file))

    yaml = YAML(typ='safe')
    yaml.allow_duplicate_keys = True
    yaml.allow_unicode = True
    return (yaml.load(''.join(frontmatter)), count)


def get_email_from_git(post_file):
    cwd = getcwd()
    try:
        chdir(path.dirname(post_file))
        file_name = path.basename(post_file)
        #email = exec_cmd(['git', 'log', '-1', '--format=\'%ae\'', '--', file_name])
        # --diff-filter=A
        email = exec_cmd(['git', 'log', '--diff-filter=A', '--format=\'%ae\'', '--', file_name])
        return email.strip().replace("'", '')
    finally:
        chdir(cwd)


def exec_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def load_featured(file_path):
    if path.isfile(file_path):
        featured = []
        with open(file_path) as fp:
            for line in fp:
                featured += [feat.strip() for feat in line.strip().split(',')]
        return featured
    return []


if __name__ == '__main__':
    parser = ArgumentParser(description='Transform the FlashReads posts to Jekyll-style MD posts.')

    parser.add_argument('-s', '--source', type=str, dest='src_dir', help='The source directory where the flash-reads posts are contained.')
    parser.add_argument('-d', '--dest', type=str, dest='dest_dir', help='The destination directory where the Jekyll-style posts will reside - usually <repo>/_posts.')
    parser.add_argument('-f', '--featured', type=str, dest='featured_path', help='File containing the featured posts by id, separated by a comma.')

    args = parser.parse_args()

    transform_posts(args.src_dir, args.dest_dir, args.featured_path)
