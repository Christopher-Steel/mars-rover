# see https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425 if
# this set command is unfamiliar to you for a great explanation
#
# They may not all be relevant in the current form of this script but it is
# good practice to always include them so that they are there if the script
# grows and needs them
set -euo pipefail

PYTHONPATH=$(pwd) poetry run python -m mars_rover "$@"
