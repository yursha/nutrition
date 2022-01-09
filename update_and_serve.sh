set -e

bash build.sh
python3 -m http.server -d "$REPO_ROOT/client/public"
