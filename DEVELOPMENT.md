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
