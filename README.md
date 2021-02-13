# GeoGH

A proof-of-concept Python script that will autogenerate random functions and commit them to a git repo. It will continue to do this in random intervals (which can be configured) across multiple files until stopped.

Why do this? For fun, mostly. The other reason is based on personal experience with certain management styles that have sought to use coding metrics as a way to evaluate developers. This script shows how trivial it is to game such systems. If you happen to have had such a system inflicted upon you, my sympathies.

Assumptions:
- Your repo already exists
- You have a branch to which you can push
- You can run from a terminal (with no need to sign into anything, etc)
