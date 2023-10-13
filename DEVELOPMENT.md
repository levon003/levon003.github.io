Development notes
===

## Jekyll

https://jekyllrb.com/docs/

```
homebrew install ruby
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
gem install jekyll bundler
gem install -n bin jekyll
./jekyll new blog
cd blog
bundle add webrick
```

To build:
```
cd blog
bundle install
bundle binstubs --all
bin/jekyll serve
# or bin/jekyll build
```

Why is a post not building?
```
jekyll build --verbose
```
