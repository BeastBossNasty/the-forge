#!/bin/bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: scripts/bootstrap_client.sh <client-slug> \"<Client Name>\"" >&2
  exit 1
fi

client_slug="$1"
shift
client_name="$*"

script_dir="$(cd "$(dirname "$0")" && pwd)"
root_dir="$(cd "$script_dir/.." && pwd)"
template_dir="$root_dir/vault/_templates/client"
target_dir="$root_dir/vault/_clients/$client_slug"

if [[ ! -d "$template_dir" ]]; then
  echo "Template directory not found: $template_dir" >&2
  exit 1
fi

if [[ -e "$target_dir" ]]; then
  echo "Target already exists: $target_dir" >&2
  exit 1
fi

cp -R "$template_dir" "$target_dir"

# Remove template files from the live client folder
find "$target_dir" -type f -name "*-template.md" -delete

# Substitute placeholder names
find "$target_dir" -type f -name "*.md" -exec \
  sed -i "s/\[client-name\]/$client_slug/g; s/\[Client Name\]/$client_name/g" {} +

echo "Created client workspace at $target_dir"
