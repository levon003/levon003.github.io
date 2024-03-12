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

## jekyll-seo-tag

The Minima theme includes the [`jekyll-seo-tag`](https://jekyll.github.io/jekyll-seo-tag/) plugin, which will generate [Open Graph](https://ogp.me/) metadata.

Advanced usage: <https://jekyll.github.io/jekyll-seo-tag/advanced-usage/#customizing-image-output>

To include an image in a post preview on social media, add `image: images/filename.png` to the front matter.
