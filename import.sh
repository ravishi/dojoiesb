#!/bin/bash
#
# referência: http://bpeirce.me/moving-one-git-repository-into-another.html
# com algumas modificações no script passado para filter-branch para mover
# também os arquivos invisíveis
CUR=`pwd`
TARGET=$1
NAME=$2
echo $TARGET
echo $NAME
TMP="`mktemp -d`/repo"
git clone "$TARGET" "$TMP"
cd "$TMP"
FILES=`git ls-files`
git filter-branch -f --prune-empty --tree-filter "
tmp=\`mktemp -d\`
mv \`ls -a1 | egrep -v '^\\.+\$' | tr \"\\n\" \" \"\` \"\$tmp\"
mv \"\$tmp\" \"$NAME\"
" -- --all
git gc --aggressive
cd "$CUR"
git remote add "$NAME" "$TMP"
git fetch "$NAME"
git merge "$NAME/master"
git remote rm "$NAME"
git gc --aggressive
