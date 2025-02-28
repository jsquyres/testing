#!/usr/bin/env python3

import os

for var in ['GITHUB_TOKEN', 'MY_PRECIOUS_ENV_SECRET', 'MY_PRECIOUS_REPO_SECRET']:
    value = os.environ.get(var, None)
    if value is None:
        print(f"Did not find env var {var}")
    else:
        print(f"Got env var {var}: \"{value}\"")
