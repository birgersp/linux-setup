export XDG_DATA_DIRS="$XDG_DATA_DIRS:/var/lib/snapd/desktop"

alias pull-dev="git pull"
alias push-dev="git push"
alias pull-master="git pull origin master"
alias push-master="git push origin server-dev:master"
alias clipboard='xclip -sel clip'
alias autocommit='git commit -m "(Automatic commit)"'
alias dpull='drive pull -directories -depth 2 -no-prompt'
alias git-gui='git gui & disown'
alias dpush='drive push -no-prompt'
alias gcola='git cola > /dev/null 2>&1& disown'

export PATH=$PATH:$TOOLS_PATH/scripts
