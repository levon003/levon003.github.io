Development notes
===

## Jekyll

Jekyll docs: https://jekyllrb.com/docs/

View the Minima 2.5 docs here: https://github.com/jekyll/minima/tree/2.5-stable

```
homebrew install ruby
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
gem install jekyll bundler
gem install -n gembin jekyll
# then, add gembin to PATH
# e.g. echo 'export PATH="/Users/levon003/repos/levon003.github.io/gembin:$PATH"' >> ~/.zshrc
./gembin/jekyll new .
bundle add webrick
```

Using RVM:

```bash
# install rvm
\curl -sSL https://get.rvm.io | bash -s stable
# install older version of Ruby that works with Jekyll
rvm install 3.1.7 --with-openssl-dir=$(brew --prefix openssl@1.1)
# use that version of ruby
rvm use 3.1.7
# set that version of ruby as the default
echo "3.1.7" > .ruby-version
# use this ruby version to install bundler
gem install bundler
# install from Gemfile
bundle install
# generate jekyll executable
bundle binstubs --all
```

To update:

```bash
bundle update github-pages
```

To build:
```
bundle install
bundle binstubs --all
bin/jekyll serve
# or bin/jekyll build
```

Why is a post not building?
```
bin/jekyll build --verbose
```

## Other notes

Get theme path: `bundle info --path minima`

To override a layout, for example:

```bash
THEME_PATH=$(bundle info --path minima)
cp $THEME_PATH/_layouts/default.html _layouts/default.html
```

### jekyll-seo-tag

The Minima theme includes the [`jekyll-seo-tag`](https://jekyll.github.io/jekyll-seo-tag/) plugin, which will generate [Open Graph](https://ogp.me/) metadata.

Advanced usage: <https://jekyll.github.io/jekyll-seo-tag/advanced-usage/#customizing-image-output>

To include an image in a post preview on social media, add `image: images/filename.png` to the front matter.

### Python

Virtual environment recommended for local development:
```bash
python3 -m venv .venv
source .venv/bin/activate
```