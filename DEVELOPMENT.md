Development notes
===

## Jekyll

https://jekyllrb.com/docs/

```
homebrew install ruby
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
gem install jekyll bundler
gem install -n gembin jekyll
# then, add gembin to PATH
# e.g. echo 'export PATH="/Users/levon003/repos/levon003.github.io/gembin:$PATH"' >> ~/.zshrc
./gembin/jekyll new blog
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
