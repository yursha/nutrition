set -e

REPO_ROOT="$(pwd)"

echo "Repository root is $REPO_ROOT"

cd $REPO_ROOT/database
python3 dump.py
cd $REPO_ROOT/client
python3 generate.py
python3 -m http.server -d "$REPO_ROOT/client/public"
