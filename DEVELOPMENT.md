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
bundle exec ../bin/jekyll serve
```
